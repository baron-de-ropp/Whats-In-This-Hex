#! usr/bin/bash
import random

items = ["bowl", "brass bell", "brooch", "carved figurine", "cup", "deck of cards", "long fork", "numbered key", "oil lamp", "old doll", "paint pot", "pencil", "drawing", "foreign coin", "game piece", "glass eye", "glass jar", "hair comb", "purse", "quill pen", "salve", "scissors", "scroll", "sealed letter", "handkerchief", "hinged box", "hourglass", "human tooth", "hunting horn", "loaded dice", "sewing needle", "shaving razor", "silver button", "skull", "tobacco pipe", "wine bottle", "belt", "blouse", "boots", "bracelet", "breastplate", "brigandine", "leather armor", "locket", "mail shirt", "mask", "necklace", "padded armor", "cincture", "cloak", "coat", "dress earring", "eyepatch", "plate mail", "ring", "robe", "sandals", "scarf", "shirt", "gauntlets", "glove", "gown", "hat", "helmet", "hose shoes", "skirt", "slippers", "socks", "trousers", "veil", "arming sword", "backsword", "battleaxe", "blowpipe", "claymore", "club", "longbow", "longsword", "mace", "maul morningstar", "pike", "crossbow", "cutlass", "dagger", "flail", "flanged mace", "glaive", "scimitar", "shortbow", "sickle", "sling", "spear", "staff", "halberd", "hammer", "hatchet", "horsebow", "hunting knife", "lance", "stake", "stiletto", "throwing axe", "warhammer", "warpick", "whip", "acid flask", "bear trap", "bellows", "bolt-cutters", "chain", "chisel", "lens", "lock & key", "lockpicks", "manacles", "metal file", "mortar & pestle", "crowbar", "door ram", "ear trumpet", "fire oil", "fishing hook", "goggles", "needle", "pickaxe", "pitchfork", "pliers", "pole", "pulleys", "grappling hook", "grease", "hacksaw", "hammer", "hand drill", "lantern", "rope", "scissors", "shovel", "spikes", "steel wire", "tongs", "alchemy recipe", "amulet", "astrolabe", "blueprints", "calligraphy", "carpet", "orrery", "painting", "perfume", "prayer book", "printing block", "rare textile", "compass", "contract", "crown", "crystal", "deed", "embroidery", "royal robes", "saints relic", "scrimshaw", "sextant", "sheet music", "signet ring", "fine china", "fine liquor", "instrument", "magical book", "microscope", "music box", "silverware", "spices", "spyglass", "tapestry", "telescope", "treasure map"]

physical_effects = ["animating", "attracting", "binding", "blossoming", "consuming", "creeping", "leitating", "opening", "petrifying", "phasing", "peircing", "pursuing", "crushing", "diminishing", "dividing", "duplicating", "enveloping", "expanding", "reflecting", "regenerating", "rending", "repelling", "resurecting", "screaming", "fusing", "grasping", "hastening", "hindering", "illumiating", "imprisoning", "sealing", "shapeshifting", "sheilding", "spawning", "transmuting", "trasnporting"]

physical_elements = ["acid", "amber", "bark", "blood", "bone", "brine", "clay", "crow", "crystal", "ember", "flesh", "fungus", "glass", "honey", "ice instect", "wood", "lava", "moss", "obsidian", "oil", "poison", "rat", "salt", "sand", "sap", "serpent", "slime", "stone", "tar", "thorn", "vine", "water", "wine", "wood", "worm"]

physical_forms = ["altar", "armor", "arrow", "beast", "blade", "cauldron", "chain", "chariot", "claw", "cloak", "colossus", "crown", "elemental", "eye", "fountain", "gate", "golem", "hammer", "horn", "key", "mask", "monolith", "pit", "prison", "sentinel", "servant", "sheild", "spear", "steed", "swarm", "tentacle", "throne", "torch", "trap", "wall", "web"]

ethereal_effects = ["avenging", "banishing", "bewildering", "blinding", "charming", "communicating", "compelling", "concealing", "defening", "deciving", "deciphering", "disguising", "dispelling", "emobldening", "encodiing", "energizing", "enlightening", "enraging", "excrutiating", "forseeing", "intoxicating", "maddening", "mesmerising", "mindreading", "nullifying", "paralising", "revealing", "revolting", "scrying", "silencing", "soothing", "summoning", "terrifying", "warding", "wearying", "withering"]

ethereal_elements = ["ash", "chaos", "distortion", "dream", "dust", "echo", "electoplasm", "fire", "fog", "ghost", "harmony", "heat", "light", "lightning", "memory", "mind", "mutation", "negation", "plague", "plasma", "probability", "rain", "rot", "shadow", "smoke", "snow", "soul", "star", "stasis", "steam", "thunder", "time", "void", "warp", "whisper", "wind"]

ethereal_forms = ["aura", "beacon", "beam", "blast", "blog", "bolt", "gaze", "loop", "moment", "nexus", "portal", "pulse", "bubble", "call", "cascade", "circle", "cloud", "coil", "pyramid", "ray", "shard", "sphere", "spray", "storm", "cone", "cube", "dance", "disk", "field", "form", "swarm", "torrent", "touch", "vortex", "wave", "word"]

lost_npcs = ['a lost npc']

civilized_npcs = ['a civilized npc']

stunned_npcs = ['a stunned npc']

underworld_npcs = ['an underworld npc']

wilderness_npcs = ['a wilderness npc']

monster_tactic = ["ambush","call for support","capture","charge","climb foes","compel worship","create barrier","decieve","demand duel","disorieent","encircle","evade","gang up","gather streangth","go berserk","harry","hurl foes","immobilize","manipulate","mock","monolauge","order minion","protect leader","protect self","scatter foes","stalk","steal from","swarm","target insolent","target leader","target nearest","target richest","target strongest","target weakest","toy with","use terrain"]

mutations = ["ages","attracts birds","child-form","corpulence","covered in hair","--animal-- arms","--andimal-- eyes","--animal-- head","--andimal-- legs","--animal-- mouth","--animal-- skin","--animal-- form","cyclops","extra arms","extra eyes","extra legs","forked tongue","gender swap","hunchback",random.choice(items) + "-form","long arms","lose all hair","lose teeth","--monster-- feature","--monster-- trait","no eyes","no mouth", random.choice(physical_elements) + " skin","second face","sheds skin","shrinks","shrivels","skin boils","slime trail","transluescent skin","weeps blood"]

dungeon_traits = ["arcane disaster","army invasion","cannabilism","civil war","collapse","crystal growth","curse","degeneration","earthquake","eruption","evil unearthed","experiments","explosion","famine","fire","flooding","fungus","haunting","ice","--insanity","lava flow","magical sleep","melted","monster attack", random.choice(mutations),"outsider attack","overgrowth","petrification","plauge","planar overlay","poison gas","resources gone","revolt","risden dead","too many traps","war"]

wilderness_regions = ["ashy", "badlands", "bay", "beach", "delta", "desert", "jungle", "lowlands", "mesas", "moor", "mountains", "petrified forest", "dry lands", "dune sea", "dust bowl", "fjords", "flood lands", "foothills", "plains", "rainforest", "riverlands", "salt pan", "savanna", "steppe", "forest", "glaciers", "heath", "highlands", "hills", "ice fields", "tiaga", "thickets", "tundra", "volcanic plain", "wetlands", "woodlands"]

wilderness_activities = ["ambush","argue","birth","build","bury","capture","--city activity","convene","demolish","die","duel","--dungeon activity","eat","excavate","feast","felling","fish","flee","forage","hunt","march","raid","rescue","rest","sacrifice","scout","sing","skin","skirmish","slay","sleep","swim","track","trap","wander","worship"]

spell_effect = random.choice(physical_effects + ethereal_effects + physical_elements + ethereal_elements) + " " + random.choice(physical_forms + ethereal_forms + physical_elements + ethereal_elements)

wilderness_landmarks = ["bog","boulder field","butte","cave","cliff","crag","lakebed","marsh","mesa","moor","pass","pit","crater","creek","crossing","ditch","field","forest","pond","rapids","ravine","ridge","rise","river","grove","hill","hollow","hot springs","lair","lake","rockslide","spring","swamp","thickets","valley","waterfall"]

wilderness_structures = ["altar","aquadeuct","bandit's camp","battleifeld","bonfire","bridge","cairn","crossroads","crypt","dam","dungeon","farm","ford","fortress","gallows","graveyard","hedge","hunter's camp","inn","lumber camp","mine","monastery","monument","orchard","outpost","pasture","ruin","seclusion","shack","shrine","standing stone","temple","village","wall","watchtower","waystone"]

wilderness_region_traits = ["ashen","blasted","blighted","broken","consuming","corrupted","creeping","desolate",random.choice(dungeon_traits),"eternal", random.choice(ethereal_effects),"foresaken","frozen","haunted","howling","jagged","lonely","misty","perilous","petrified","phantasmal","ravenous","savage","shadowy","shifting","shivering","sinister","sinking","smoldering","sweltering","frozen","huanted","howling","jagged","loneyly","misty","thorny","thundering","torrential", random.choice(physical_effects),"wandering","withered"]

edible_plants = ["acorns","apples","asparagus","blackberries","blueberries","carrots","cattail","cherries","chickweed","chicory","clover","dandelion","dead-nettle","elderberries","fireweed","gooseberries","hazelenuts","henbit","hickorynuts","honeysuckle","leeks","milkthisle","mint","mulberries","mushrooms","mustard","onion","pecans","persimmons","raspberries","strawberries","walnuts","watercress","wild garlic","wild grapes","wood sorrel"]

poisonous_plants = ["angel's trumpet","baneberry","belladona","blacktruffle","bleedingheart","celandine","cocklebur","columbine","crowncup","deathcap","dumbcane","foxglove","hemlock","hogweed","holly","horse chestnut","hyacinth","ivy","jessamine","kudu","larkspur","mandrake","mangrove","mistletoe","moonflower","nightshadeoleander","ragwort","reindeer lichen","snakeweed","spindle","stinkhorn","waxcap","wine-cap","woflsbane","wormswood"]

city_activities = ["abduct","beg","brawl","burgle","celebrate","chase","construct","cook","dance","deul","execute","extinguish","extort","follow","gamble","haul","interrogate","marry", "--a mission","mourn","party","patrol","perform","play","preach","process","proclaim","protest","release","repair","riot","rob","search","sell",random.choice(wilderness_activities)]

dungeon_activities = ["besiege","capture","collect","construct","ontrol","deliver","demolish","escape","feed","fortify","gaurd","hide","hunt","loot","map","mine",random.choice(monster_tactic),"negotiate","patrol","perform ritual","purge","question","raid","repair","rescue","research","revive","riddle","scavenge","seize","tunnel","unearth","vandalize",random.choice(wilderness_activities),"worship"]

wilderness_discoveries = ["bloodstains","bones","broken weapons","burrow",random.choice(city_activities),random.choice(civilized_npcs),"cut ropes","dead animal",random.choice(dungeon_activities),"food scraps","grave marker","human corpse",random.choice(items),random.choice(lost_npcs),random.choice(spell_effect),"map","message","migration",random.choice(mutations),"nest","portal","resources","rift","strange plant",random.choice(stunned_npcs),"supplies","torn flag","tracks","trap","treasure cache",random.choice(underworld_npcs),random.choice(wilderness_activities),random.choice(wilderness_landmarks),random.choice(wilderness_npcs),"wizard fight"]

city_activities.append(random.choice(dungeon_activities))
dungeon_activities.append(random.choice(city_activities))

print("wilderness region trait", random.choice(wilderness_region_traits))

if random.randint(1,10) == 10:
    print("additional wilderness region trait", random.choice(wilderness_region_traits))

print("wilderness landmark", random.choice(wilderness_landmarks))

if random.randint(1,10) == 10:
    print("additional wilderness landmark", random.choice(wilderness_landmarks))

print("wilderness discovery", random.choice(wilderness_discoveries))

if random.randint(1,10) == 10:
    print("wilderness discovery", random.choice(wilderness_discoveries))

if random.randint(1,2) == 2:
    print("wilderness structure", random.choice(wilderness_structures))

    if random.randint(1,10) == 10:
        print("additional wilderness structure", random.choice(wilderness_structures))

if random.randint(1, 10) == 10:
    print("edible plant", random.choice(edible_plants))

if random.randint(1,10) == 10:
    print("poisonous plant", random.choice(poisonous_plants))

hexgrid = '''
 ___     ___
/0,0\___/2,0\___
\___/1,0\___/3,0\
/0,1\___/2,1\___/
\___/1,1\___/3,1\
/0,2\___/2,2\___/
\___/1,2\___/3,2\
    \___/   \___/

'''