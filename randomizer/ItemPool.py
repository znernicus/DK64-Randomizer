"""Contains functions related to setting up the pool of shuffled items."""
import itertools

from randomizer.Enums.Items import Items
from randomizer.Enums.Locations import Locations
from randomizer.Lists.Item import ItemFromKong
from randomizer.Lists.Location import LocationList


def PlaceConstants(settings):
    """Place items which are to be put in a hard-coded location."""
    # Banana Hoard: Pseudo-item used to represent game completion by defeating K. Rool
    LocationList[Locations.BananaHoard].PlaceConstantItem(Items.BananaHoard)
    # Keys kept at key locations so boss completion requires
    LocationList[Locations.JapesKey].PlaceConstantItem(Items.JungleJapesKey)
    LocationList[Locations.AztecKey].PlaceConstantItem(Items.AngryAztecKey)
    LocationList[Locations.FactoryKey].PlaceConstantItem(Items.FranticFactoryKey)
    LocationList[Locations.GalleonKey].PlaceConstantItem(Items.GloomyGalleonKey)
    LocationList[Locations.ForestKey].PlaceConstantItem(Items.FungiForestKey)
    LocationList[Locations.CavesKey].PlaceConstantItem(Items.CrystalCavesKey)
    LocationList[Locations.CastleKey].PlaceConstantItem(Items.CreepyCastleKey)
    LocationList[Locations.HelmKey].PlaceConstantItem(Items.HideoutHelmKey)
    # Helm locations (which are functionally events)
    LocationList[Locations.HelmDonkey1].PlaceConstantItem(Items.HelmDonkey1)
    LocationList[Locations.HelmDonkey2].PlaceConstantItem(Items.HelmDonkey2)
    LocationList[Locations.HelmDiddy1].PlaceConstantItem(Items.HelmDiddy1)
    LocationList[Locations.HelmDiddy2].PlaceConstantItem(Items.HelmDiddy2)
    LocationList[Locations.HelmLanky1].PlaceConstantItem(Items.HelmLanky1)
    LocationList[Locations.HelmLanky2].PlaceConstantItem(Items.HelmLanky2)
    LocationList[Locations.HelmTiny1].PlaceConstantItem(Items.HelmTiny1)
    LocationList[Locations.HelmTiny2].PlaceConstantItem(Items.HelmTiny2)
    LocationList[Locations.HelmChunky1].PlaceConstantItem(Items.HelmChunky1)
    LocationList[Locations.HelmChunky2].PlaceConstantItem(Items.HelmChunky2)
    # Settings-dependent locations
    if settings.training_barrels == "normal":
        LocationList[Locations.IslesVinesTrainingBarrel].PlaceConstantItem(Items.Vines)
        LocationList[Locations.IslesSwimTrainingBarrel].PlaceConstantItem(Items.Swim)
        LocationList[Locations.IslesOrangesTrainingBarrel].PlaceConstantItem(Items.Oranges)
        LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceConstantItem(Items.Barrels)
    elif settings.training_barrels == "startwith":
        LocationList[Locations.IslesVinesTrainingBarrel].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.IslesSwimTrainingBarrel].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.IslesOrangesTrainingBarrel].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.IslesBarrelsTrainingBarrel].PlaceConstantItem(Items.NoItem)
    if settings.unlock_all_kongs:
        LocationList[Locations.DiddyKong].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.LankyKong].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.TinyKong].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.ChunkyKong].PlaceConstantItem(Items.NoItem)
    if settings.unlock_all_moves:
        # Empty all shop locations EXCEPT sniper scope which is still optional
        LocationList[Locations.SimianSlam].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.SuperSimianSlam].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.SuperDuperSimianSlam].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.BaboonBlast].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.StrongKong].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.GorillaGrab].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.ChimpyCharge].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.RocketbarrelBoost].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.SimianSpring].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Orangstand].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.BaboonBalloon].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.OrangstandSprint].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.MiniMonkey].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.PonyTailTwirl].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Monkeyport].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.HunkyChunky].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.PrimatePunch].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.GorillaGone].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.CoconutGun].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.PeanutGun].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.GrapeGun].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.FeatherGun].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.PineappleGun].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.AmmoBelt1].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.HomingAmmo].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.AmmoBelt2].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Bongos].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Guitar].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Trombone].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Saxophone].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.Triangle].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.MusicUpgrade1].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.ThirdMelon].PlaceConstantItem(Items.NoItem)
        LocationList[Locations.MusicUpgrade2].PlaceConstantItem(Items.NoItem)
    if settings.unlock_fairy_shockwave:
        LocationList[Locations.CameraAndShockwave].PlaceConstantItem(Items.NoItem)
    if settings.shuffle_items != "all":
        if settings.shuffle_items == "moves":
            moveLocations = []
            moveLocations.extend(DonkeyMoveLocations)
            moveLocations.extend(DiddyMoveLocations)
            moveLocations.extend(LankyMoveLocations)
            moveLocations.extend(TinyMoveLocations)
            moveLocations.extend(ChunkyMoveLocations)
            moveLocations.extend(SharedMoveLocations)
            locations = [x for x in LocationList if x not in moveLocations]
            for location in locations:
                LocationList[location].PlaceDefaultItem()
        else:
            for location in LocationList:
                LocationList[location].PlaceDefaultItem()


def AllItems(settings):
    """Return all shuffled items."""
    allItems = []
    if settings.shuffle_items:
        allItems.extend(Blueprints(settings))
        allItems.extend(HighPriorityItems(settings))
        allItems.extend(LowPriorityItems(settings))
        allItems.extend(ExcessItems(settings))
    elif settings.shuffle_moves:
        allItems.extend(DonkeyMoves)
        allItems.extend(DiddyMoves)
        allItems.extend(LankyMoves)
        allItems.extend(TinyMoves)
        allItems.extend(ChunkyMoves)
    return allItems


def Blueprints(settings):
    """Return all blueprint items."""
    blueprints = [
        Items.DKIslesDonkeyBlueprint,
        Items.DKIslesDiddyBlueprint,
        Items.DKIslesLankyBlueprint,
        Items.DKIslesTinyBlueprint,
        Items.DKIslesChunkyBlueprint,
        Items.JungleJapesDonkeyBlueprint,
        Items.JungleJapesDiddyBlueprint,
        Items.JungleJapesLankyBlueprint,
        Items.JungleJapesTinyBlueprint,
        Items.JungleJapesChunkyBlueprint,
        Items.AngryAztecDonkeyBlueprint,
        Items.AngryAztecDiddyBlueprint,
        Items.AngryAztecLankyBlueprint,
        Items.AngryAztecTinyBlueprint,
        Items.AngryAztecChunkyBlueprint,
        Items.FranticFactoryDonkeyBlueprint,
        Items.FranticFactoryDiddyBlueprint,
        Items.FranticFactoryLankyBlueprint,
        Items.FranticFactoryTinyBlueprint,
        Items.FranticFactoryChunkyBlueprint,
        Items.GloomyGalleonDonkeyBlueprint,
        Items.GloomyGalleonDiddyBlueprint,
        Items.GloomyGalleonLankyBlueprint,
        Items.GloomyGalleonTinyBlueprint,
        Items.GloomyGalleonChunkyBlueprint,
        Items.FungiForestDonkeyBlueprint,
        Items.FungiForestDiddyBlueprint,
        Items.FungiForestLankyBlueprint,
        Items.FungiForestTinyBlueprint,
        Items.FungiForestChunkyBlueprint,
        Items.CrystalCavesDonkeyBlueprint,
        Items.CrystalCavesDiddyBlueprint,
        Items.CrystalCavesLankyBlueprint,
        Items.CrystalCavesTinyBlueprint,
        Items.CrystalCavesChunkyBlueprint,
        Items.CreepyCastleDonkeyBlueprint,
        Items.CreepyCastleDiddyBlueprint,
        Items.CreepyCastleLankyBlueprint,
        Items.CreepyCastleTinyBlueprint,
        Items.CreepyCastleChunkyBlueprint,
    ]
    return blueprints


def BlueprintAssumedItems(settings):
    """Items which are assumed to be owned while placing blueprints."""
    return LowPriorityItems(settings) + ExcessItems(settings)


def Keys():
    """Return all key items."""
    keys = [
        Items.JungleJapesKey,
        Items.AngryAztecKey,
        Items.FranticFactoryKey,
        Items.GloomyGalleonKey,
        Items.FungiForestKey,
        Items.CrystalCavesKey,
        Items.CreepyCastleKey,
        Items.HideoutHelmKey,
    ]
    return keys


def Kongs(settings):
    """Return Kong items depending on settings."""
    kongs = []
    if not settings.unlock_all_kongs:
        kongs = [Items.Donkey, Items.Diddy, Items.Lanky, Items.Tiny, Items.Chunky]
        kongs.remove(ItemFromKong(settings.starting_kong))
    return kongs


def Guns(settings):
    """Return all gun items."""
    guns = []
    if not settings.unlock_all_moves:
        guns.extend(
            [
                Items.Coconut,
                Items.Peanut,
                Items.Grape,
                Items.Feather,
                Items.Pineapple,
            ]
        )
    return guns


def Instruments(settings):
    """Return all instrument items."""
    instruments = []
    if not settings.unlock_all_moves:
        instruments.extend(
            [
                Items.Bongos,
                Items.Guitar,
                Items.Trombone,
                Items.Saxophone,
                Items.Triangle,
            ]
        )
    return instruments


def TrainingBarrelAbilities():
    """Return all training barrel abilities."""
    barrelAbilities = [
        Items.Vines,
        Items.Swim,
        Items.Oranges,
        Items.Barrels,
    ]
    return barrelAbilities


def Upgrades(settings):
    """Return all upgrade items."""
    upgrades = []
    # Add training barrel items to item pool if shuffled
    if settings.training_barrels == "shuffled":
        upgrades.extend(TrainingBarrelAbilities())
    # Add either progressive upgrade items or individual ones depending on settings
    if not settings.unlock_all_moves:
        upgrades.extend(itertools.repeat(Items.ProgressiveSlam, 3))
        if settings.progressive_upgrades:
            upgrades.extend(itertools.repeat(Items.ProgressiveDonkeyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveDiddyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveLankyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveTinyPotion, 3))
            upgrades.extend(itertools.repeat(Items.ProgressiveChunkyPotion, 3))
        else:
            upgrades.extend(
                [
                    Items.BaboonBlast,
                    Items.StrongKong,
                    Items.GorillaGrab,
                    Items.ChimpyCharge,
                    Items.RocketbarrelBoost,
                    Items.SimianSpring,
                    Items.Orangstand,
                    Items.BaboonBalloon,
                    Items.OrangstandSprint,
                    Items.MiniMonkey,
                    Items.PonyTailTwirl,
                    Items.Monkeyport,
                    Items.HunkyChunky,
                    Items.PrimatePunch,
                    Items.GorillaGone,
                ]
            )
    if not settings.unlock_fairy_shockwave:
        upgrades.append(Items.CameraAndShockwave)

    return upgrades


def HighPriorityItems(settings):
    """Get all items which are of high importance logically.

    Placing these first prevents fill failures.
    """
    itemPool = []
    itemPool.extend(Kongs(settings))
    itemPool.extend(Guns(settings))
    itemPool.extend(Instruments(settings))
    itemPool.extend(Upgrades(settings))
    return itemPool


def HighPriorityAssumedItems(settings):
    """Items which are assumed to be owned while placing high priority items."""
    return Blueprints(settings) + LowPriorityItems(settings) + ExcessItems(settings)


def LowPriorityItems(settings):
    """While most of these items still have logical value they are not as important."""
    itemPool = []

    itemPool.extend(itertools.repeat(Items.GoldenBanana, 100))
    itemPool.extend(itertools.repeat(Items.BananaFairy, 20))
    itemPool.extend(itertools.repeat(Items.BananaMedal, 15))
    if not settings.crown_door_open:
        itemPool.extend(itertools.repeat(Items.BattleCrown, 4))
    if not settings.coin_door_open:
        itemPool.append(Items.NintendoCoin)
        itemPool.append(Items.RarewareCoin)

    return itemPool


def ExcessItems(settings):
    """Items which either have no logical value or are excess copies of those that do."""
    itemPool = []
    itemPool.append(Items.SniperSight)

    if not settings.unlock_all_moves:
        # Weapon upgrades
        itemPool.append(Items.HomingAmmo)
        itemPool.extend(itertools.repeat(Items.ProgressiveAmmoBelt, 2))

        # Instrument upgrades
        itemPool.extend(itertools.repeat(Items.ProgressiveInstrumentUpgrade, 3))

    # Collectables
    itemPool.extend(itertools.repeat(Items.GoldenBanana, 101))
    itemPool.extend(itertools.repeat(Items.BananaMedal, 25))
    itemPool.extend(itertools.repeat(Items.BattleCrown, 6))
    if settings.crown_door_open:
        itemPool.extend(itertools.repeat(Items.BattleCrown, 4))
    if settings.coin_door_open:
        itemPool.append(Items.NintendoCoin)
        itemPool.append(Items.RarewareCoin)

    return itemPool

DonkeyMoveLocations = [
    Locations.BaboonBlast,
    Locations.StrongKong,
    Locations.GorillaGrab,
    Locations.CoconutGun,
    Locations.Bongos,
]
DiddyMoveLocations = [
    Locations.ChimpyCharge,
    Locations.RocketbarrelBoost,
    Locations.SimianSpring,
    Locations.PeanutGun,
    Locations.Guitar,
]
LankyMoveLocations = [
    Locations.Orangstand,
    Locations.BaboonBalloon,
    Locations.OrangstandSprint,
    Locations.GrapeGun,
    Locations.Trombone,
]
TinyMoveLocations = [
    Locations.MiniMonkey,
    Locations.PonyTailTwirl,
    Locations.Monkeyport,
    Locations.FeatherGun,
    Locations.Saxophone,
]
ChunkyMoveLocations = [
    Locations.HunkyChunky,
    Locations.PrimatePunch,
    Locations.GorillaGone,
    Locations.PineappleGun,
    Locations.Triangle,
]
SharedMoveLocations = [
    Locations.SuperSimianSlam,
    Locations.SuperDuperSimianSlam,
    Locations.SniperSight,
    Locations.HomingAmmo,
    Locations.AmmoBelt1,
    Locations.AmmoBelt2,
    Locations.MusicUpgrade1,
    Locations.ThirdMelon,
    Locations.MusicUpgrade2,
]
DonkeyMoves = [
    Items.Coconut,
    Items.Bongos,
    Items.BaboonBlast,
    Items.StrongKong,
    Items.GorillaGrab,
]
DiddyMoves = [
    Items.Peanut,
    Items.Guitar,
    Items.ChimpyCharge,
    Items.RocketbarrelBoost,
    Items.SimianSpring,
    
]
LankyMoves = [
    Items.Grape,
    Items.Trombone,
    Items.Orangstand,
    Items.BaboonBalloon,
    Items.OrangstandSprint,
    
]
TinyMoves = [
    Items.Feather,
    Items.Saxophone,
    Items.MiniMonkey,
    Items.PonyTailTwirl,
    Items.Monkeyport,
    
]
ChunkyMoves = [
    Items.Pineapple,
    Items.Triangle,
    Items.HunkyChunky,
    Items.PrimatePunch,
    Items.GorillaGone,
    
]
ImportantSharedMoves = [
    Items.ProgressiveSlam,
    Items.ProgressiveSlam,
    Items.SniperSight,
    Items.HomingAmmo,
]
JunkSharedMoves = [
    Items.ProgressiveAmmoBelt,
    Items.ProgressiveAmmoBelt,
    Items.ProgressiveInstrumentUpgrade,
    Items.ProgressiveInstrumentUpgrade,
    Items.ProgressiveInstrumentUpgrade,
]
