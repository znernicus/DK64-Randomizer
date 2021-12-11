"""File containing main UI button events that travel between tabs."""
import js
from ui.bindings import bind
import json
from ui.rando_options import update_disabled_progression
from ui.progress_bar import ProgressBar


@bind("change", "jsonfileloader")
def lanky_file_changed(event):
    """On the event of a lanky file being loaded.

    Args:
        event (event): Javascript event.
    """

    def onload(e):
        # Load the text of the json file
        loaded_json = json.loads(e.target.result)
        # For all the loaded vars set them to the proper value
        # Also set each option to disabled
        for key in loaded_json:
            if loaded_json[key] is True:
                js.document.getElementsByName(key)[0].checked = True
                js.document.getElementsByName(key)[0].disabled = True
            elif loaded_json[key] is False:
                js.document.getElementsByName(key)[0].checked = False
                js.document.getElementsByName(key)[0].disabled = True
            else:
                js.document.getElementsByName(key)[0].value = loaded_json[key]
                js.document.getElementsByName(key)[0].disabled = True

    # Attempt to find what file was loaded
    file = None
    for uploaded_file in js.document.getElementById("jsonfileloader").files:
        file = uploaded_file
        break
    reader = js.FileReader.new()
    # If we loaded a file, set up the event listener to wait for it to be loaded
    if file is not None:
        reader.readAsText(file)
        reader.addEventListener("load", onload)
    # If we unloaded a file, find all element on the form and re-enable it.
    # But also make sure we make sure we re disable progression form options
    else:
        for element in js.document.getElementById("form").elements:
            element.disabled = False
        update_disabled_progression(None)


@bind("click", "generate_lanky_seed")
@bind("click", "generate_seed")
def generate_seed(event):
    """Generate a seed based off the current settings.

    Args:
        event (event): Javascript click event.
    """
    # Check if the rom filebox has a file loaded in it.
    if not js.document.getElementById("input-file-rom").value:
        js.document.getElementById("input-file-rom").select()
    else:
        # Start the progressbar
        ProgressBar().update_progress(0, "Initalizing")
        # Remove all the disabled attributes and store them for later
        disabled_options = []
        for element in js.document.getElementsByTagName("input"):
            if element.disabled:
                disabled_options.append(element)
                element.removeAttribute("disabled")
        for element in js.document.getElementsByTagName("select"):
            if element.disabled:
                disabled_options.append(element)
                element.removeAttribute("disabled")
        # Serialize the form into json
        form = js.jquery("#form").serializeArray()
        form_data = {}
        # Verify each object if its value is a string convert it to a bool
        for obj in form:
            if obj.value.lower() in ["true", "false"]:
                form_data[obj.name] = bool(obj.value)
            else:
                form_data[obj.name] = obj.value
        # find all input boxes and verify their checked status
        for element in js.document.getElementsByTagName("input"):
            if element.type == "checkbox" and not element.checked:
                if not form_data.get(element.name):
                    form_data[element.name] = False
        # Re disable all previously disabled options
        for element in disabled_options:
            element.setAttribute("disabled", "disabled")
        # TODO: This is the entrypoint of builds, we need to make sure we properly set this up
        # print(form_data)
        # print(datetime.now())
        # worker.background(run, ["'assumed'"], test)
        # This is what the returning function used to be
        # patch_files.start_randomizing_seed(dict(data.get("form_data"))


@bind("click", "downloadjson")
def update_seed_text(event):
    # When we click the download json event just change the button text
    if js.document.getElementById("downloadjson").checked:
        js.document.getElementById("generate_seed").value = "Generate Patch File"
    else:
        js.document.getElementById("generate_seed").value = "Generate Seed"


@bind("click", "nav-seed-gen-tab")
@bind("click", "nav-patch-tab")
def disable_input(event):
    """Disable input for the ROM Boxes as we rotate through the navbar.

    Args:
        event (DOMEvent): DOM item that triggered the event.
    """
    # Try to determine of the patch tab was what triggered the event.
    ev_type = False
    try:
        if "patch-tab" in event.target.id:
            ev_type = True
    except Exception:
        pass
    # As we rotate between the tabs, verify our disabled progression status
    # and set our input file box as the correct name so we can use two fileboxes as the same name
    if ev_type is False:
        update_disabled_progression(None)
        try:
            js.document.getElementById("input-file-rom").id = "input-file-rom_2"
        except Exception:
            pass
        js.document.getElementById("input-file-rom_1").id = "input-file-rom"
    else:
        try:
            js.document.getElementById("input-file-rom").id = "input-file-rom_1"
        except Exception:
            pass
        js.document.getElementById("input-file-rom_2").id = "input-file-rom"


disable_input(None)