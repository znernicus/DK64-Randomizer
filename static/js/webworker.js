// Worker script for pyodide scripts
onmessage = async function (e) {
  // Read the passed string as JSON
  content = JSON.parse(e.data);
  // Reload Pyodide
  // TODO: We should probably see about caching this load
  importScripts("https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js");
  pyodide = await loadPyodide({
    indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
  });
  // Load Micropip so we can load the importers
  await pyodide.loadPackage("micropip");
  // Load all our website pages uses the origin of this function
  await pyodide.runPythonAsync(
    `
    import micropip
    await micropip.install('pyodide-importer')
    from pyodide_importer import register_hook
    register_hook('` +
      this.location.origin +
      `/')
    `
  );
  // Run the passed function
  resp = pyodide.runPython(content["func"]);
  content.response = resp;
  // Return the response as json
  postMessage(content);
};