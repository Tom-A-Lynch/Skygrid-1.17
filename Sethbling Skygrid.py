# SkyGrid Filter by SethBling and Thoams Lynch
# Built By SethBling, updated by Thomas Lynch
# Feel free to modify and reuse, but credit to SethBling would be nice.


from amulet.api.block import Block
from pymclevel import MCSchematic
from pymclevel import TileEntity
from pymclevel import TAG_Compound
from pymclevel import TAG_Short
from pymclevel import TAG_Byte
from pymclevel import TAG_String
import random
import numPy
import array

displayName = "Thomas' Sky Grid"
inputs = (
    ("Grid Length", (4, 1, 100)),
    ("World Type", ("Overworld",
                    "Nether",
                    )),
)

def perform(level, box, options):
    gridlength = options["Grid Length"]
    worldtype = options["World Type"]

    total = 0
    cump = {}

    if worldtype == "Overworld":
        p = normalp()
    elif worldtype == "Nether":
        p = netherp()

    # generate the cumulative distribution
    for key, value in p.iteritems():
        cump[key] = (total, total + value)
        total += value
            
    for x in xrange(box.minx, box.maxx, gridlength):
        for y in xrange(box.miny, box.maxy, gridlength):
            for z in xrange(box.minz, box.maxz, gridlength):
                blockid = pickblock(cump, total)

                if(blockid == 6 or blockid == 31 or blockid == 32 or blockid == 37 or
                   blockid == 38 or blockid == 39 or blockid == 40 or blockid == 83):
                    level.setBlockAt(x, y, z, 3) #dirt
                    if(y < box.maxy):
                        level.setBlockAt(x, y+1, z, blockid)
                    if(blockid == 83): #reeds
                        level.setBlockAt(x+1, y, z, 9) #still water
                elif(blockid == 81): #cactus
                    level.setBlockAt(x, y, z, 12) #sand
                    if(y < box.maxy):
                        level.setBlockAt(x, y+1, z, blockid)
                    if(y > box.miny):
                        level.setBlockAt(x, y-1, z, 106) # vines
                elif(blockid == 115): #netherwart
                    level.setBlockAt(x, y, z, 112)
                    if(y < box.maxy):
                        level.setBlockAt(x, y+1, z, blockid)
                else:
                    level.setBlockAt(x, y, z, blockid)

                if(blockid == 54):
                    fillChestAt(level, x, y, z)

                if(blockid == 52):
                    setSpawnerAt(level, worldtype, x, y, z)

    if worldtype == "Overworld":
        #generate end portal
        dx = box.maxx - box.minx
        dz = box.maxz - box.minz

        middlex = box.minx + int(dx / 2 / gridlength) * gridlength
        middlez = box.minz + int(dz / 2 / gridlength) * gridlength
        
        y = box.miny + gridlength

        if y <= box.maxy and middlex+4 <= box.maxx and middlez+4 <= box.maxz:
            # set portal blocks
            level.setBlockAt(middlex+1, y, middlez, 120)
            level.setBlockAt(middlex+2, y, middlez, 120)
            level.setBlockAt(middlex+3, y, middlez, 120)

            level.setBlockAt(middlex, y, middlez+1, 120)
            level.setBlockAt(middlex, y, middlez+2, 120)
            level.setBlockAt(middlex, y, middlez+3, 120)

            level.setBlockAt(middlex+1, y, middlez+4, 120)
            level.setBlockAt(middlex+2, y, middlez+4, 120)
            level.setBlockAt(middlex+3, y, middlez+4, 120)

            level.setBlockAt(middlex+4, y, middlez+1, 120)
            level.setBlockAt(middlex+4, y, middlez+2, 120)
            level.setBlockAt(middlex+4, y, middlez+3, 120)

            # set damage values
            level.setBlockDataAt(middlex+1, y, middlez, 1)
            level.setBlockDataAt(middlex+2, y, middlez, 1)
            level.setBlockDataAt(middlex+3, y, middlez, 1)

            level.setBlockDataAt(middlex, y, middlez+1, 1)
            level.setBlockDataAt(middlex, y, middlez+2, 1)
            level.setBlockDataAt(middlex, y, middlez+3, 1)

            level.setBlockDataAt(middlex+1, y, middlez+4, 1)
            level.setBlockDataAt(middlex+2, y, middlez+4, 1)
            level.setBlockDataAt(middlex+3, y, middlez+4, 1)

            level.setBlockDataAt(middlex+4, y, middlez+1, 1)
            level.setBlockDataAt(middlex+4, y, middlez+2, 1)
            level.setBlockDataAt(middlex+4, y, middlez+3, 1)
    

    level.markDirtyBox(box)

# returns a weighted probability distribution for blocks in the overworld


def normalp():
    p = {}

    p[0] = Block("minecraft", "stone")
    p[1] = Block("minecraft", "granite")
    p[2] = Block("minecraft", "diorite")
    p[3] = Block("minecraft", "andesite")
    p[4] = Block("minecraft", "grass_block")
    p[5] = Block("minecraft", "dirt")
    p[6] = Block("minecraft", "coarse_dirt")
    p[7] = Block("minecraft", "podzol")
    p[8] = Block("minecraft", "sand")
    p[9] = Block("minecraft", "red_sand")
    p[10] = Block("minecraft", "gravel")
    p[11] = Block("minecraft", "gold_ore")
    p[12] = Block("minecraft", "iron_ore")
    p[13] = Block("minecraft", "coal_ore")
    p[14] = Block("minecraft", "oak_log")
    p[15] = Block("minecraft", "spruce_log")
    p[16] = Block("minecraft", "birch_log")
    p[17] = Block("minecraft", "jungle_log")
    p[18] = Block("minecraft", "acacia_log")
    p[19] = Block("minecraft", "dark_oak_log")
    p[20] = Block("minecraft", "oak_leaves")
    p[21] = Block("minecraft", "spruce_leaves")
    p[22] = Block("minecraft", "birch_leaves")
    p[23] = Block("minecraft", "jungle_leaves")
    p[24] = Block("minecraft", "acacia_leaves")
    p[25] = Block("minecraft", "dark_oak_leaves")
    p[26] = Block("minecraft", "sponge")
    p[27] = Block("minecraft", "lapis_ore")
    p[28] = Block("minecraft", "sandstone")
    p[29] = Block("minecraft", "note block")
    p[30] = Block("minecraft", "white_wool")
    p[31] = Block("minecraft", "orange_wool")
    p[32] = Block("minecraft", "magenta_wool")
    p[33] = Block("minecraft", "light_blue_wool")
    p[34] = Block("minecraft", "yellow_wool")
    p[35] = Block("minecraft", "lime_wool")
    p[36] = Block("minecraft", "pink_wool")
    p[37] = Block("minecraft", "gray_wool")
    p[38] = Block("minecraft", "light_gray_wool")
    p[39] = Block("minecraft", "cyan_wool")
    p[40] = Block("minecraft", "purple_wool")
    p[41] = Block("minecraft", "blue_wool")
    p[42] = Block("minecraft", "brown_wool")
    p[43] = Block("minecraft", "green_wool")
    p[44] = Block("minecraft", "red_wool")
    p[45] = Block("minecraft", "black_wool")
    p[46] = Block("minecraft", "gold_block")
    p[47] = Block("minecraft", "iron_block")
    p[48] = Block("minecraft", "bricks")
    p[49] = Block("minecraft", "tnt")
    p[50] = Block("minecraft", "bookshelf")
    p[51] = Block("minecraft", "mossy_cobblestone")
    p[52] = Block("minecraft", "obsidian")
    p[53] = Block("minecraft", "diamond_ore")
    p[54] = Block("minecraft", "diamond_block")
    p[55] = Block("minecraft", "furnace")
    p[56] = Block("minecraft", "crafting_table")
    p[57] = Block("minecraft", "redstone_ore")
    p[58] = Block("minecraft", "ice")
    p[59] = Block("minecraft", "snow_block")
    p[60] = Block("minecraft", "melon")
    p[61] = Block("minecraft", "mycelium")
    p[62] = Block("minecraft", "pumpkin")
    p[63] = Block("minecraft", "nether_bricks")
    p[64] = Block("minecraft", "enchanting_table")
    p[65] = Block("minecraft", "emerald_ore")
    p[66] = Block("minecraft", "emerald_block")
    p[67] = Block("minecraft", "redstone_block")
    p[68] = Block("minecraft", "terracotta")
    p[69] = Block("minecraft", "hay_block")
    p[70] = Block("minecraft", "coal_block")
    p[71] = Block("minecraft", "packed_ice")
    p[72] = Block("minecraft", "slime_block")
    p[73] = Block("minecraft", "prismarine")
    p[74] = Block("minecraft", "sea_lanter")
    p[75] = Block("minecraft", "magma_block")
    p[76] = Block("minecraft", "red_nether_brick")
    p[77] = Block("minecraft", "blue_ice")
    p[78] = Block("minecraft", "amethyst_block")
    p[79] = Block("minecraft", "azalea_leaves")
    p[80] = Block("minecraft", "budding_amethyst")
    p[81] = Block("minecraft", "deepslate")
    p[82] = Block("minecraft", "calcite")
    p[83] = Block("minecraft", "copper_ore")
    p[84] = Block("minecraft", "copper_block")
    p[85] = Block("minecraft", "deepslate_coal_ore")
    p[86] = Block("minecraft", "deepslate_copper_ore")
    p[87] = Block("minecraft", "deepslate_diamond_ore")
    p[88] = Block("minecraft", "deepslate_emerald_ore")
    p[89] = Block("minecraft", "deepslate_iron_ore")
    p[90] = Block("minecraft", "deepslate_gold_ore")
    p[91] = Block("minecraft", "deepslate_lapis_ore")
    p[92] = Block("minecraft", "deepslate_redstone_ore")
    p[93] = Block("minecraft", "dripstone_block")
    p[94] = Block("minecraft", "flowering_azalea_leaves")
    p[95] = Block("minecraft", "moss_block")
    p[96] = Block("minecraft", "raw_copper_block")
    p[97] = Block("minecraft", "raw_gold_block")
    p[98] = Block("minecraft", "raw_iron_block")
    p[99] = Block("minecraft", "rooted_dirt")
    p[100] = Block("minecraft", "tuff")


    return p

# returns an unnormalized probability distribution for blocks in the
# nether
def netherp():
    p = {}
    p[11] = 50  #still lava
    p[13] = 30  #gravel
    p[52] = 2   #mob spawner
    p[54] = 1   #chest
    p[87] = 300 #netherack
    p[88] = 100 #soulsand
    p[89] = 50  #glowstone
    p[112] = 30 #netherbrick
    p[113] = 10 #nether fence
    p[114] = 15 #nether stairs
    p[115] = 30 #netherwart

    return p

# picks a random block from a cumulative distribution
def pickblock(cump, size):
    r = random.random() * size
    
    for key, value in cump.iteritems():
        low, high = value
        if r >= low and r < high:
            return key

# creates a randomized mob spawner tile entity at a specified location
def setSpawnerAt(level, worldtype, x, y, z):
    chunk = level.getChunk(x / 16, z / 16)

    if worldtype=="Overworld":
        spawns = overworldSpawns()
    elif worldtype=="Nether":
        spawns = netherSpawns()
        
    spawnindex = randomInRange(0, len(spawns) - 1)

    spawner = TileEntity.Create("MobSpawner")
    TileEntity.setpos(spawner, (x, y, z))
    spawner["Delay"] = TAG_Short(120)
    spawner["EntityId"] = spawns[spawnindex]

    chunk.TileEntities.append(spawner)

def overworldSpawns():
    return ["Creeper",
            "Skeleton",
            "Spider",
            "CaveSpider",
            "Zombie",
            "Slime",
            "Pig",
            "Sheep",
            "Cow",
            "Chicken",
            "Squid",
            "Wolf",
            "Enderman",
            "Silverfish",
            "Villager",
            ]

def netherSpawns():
    return ["PigZombie",
            "Blaze",
            "LavaSlime",
            ]
def waterSpawns():
    return ["GlowSquid",
            "Axolotl",
            "Squid",
            "Turtle",
            "Cod",
            "Salmon",
            "TropicalFish",
            "Pufferfish",
            "Drowned",
            "ElderGuardian",
            "Guardian",

            ]


# fills a chest with random goodies
def fillChestAt(level, x, y, z):
    chunk = level.getChunk(x / 16, z / 16)

    chest = TileEntity.Create("Chest")
    TileEntity.setpos(chest, (x, y, z))

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(256, 294)) #various weapons/random

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(298, 317)) #various armor

    if(random.random() < 0.7):
        chest["Items"].append(createItemInRange(318, 350)) #various food/tools

    if(random.random() < 0.3):
        chest["Items"].append(createItemWithRandomDamage(383, 50, 52)) # various spawn eggs

    if(random.random() < 0.9):
        chest["Items"].append(createItemWithRandomDamage(383, 54, 62)) #various spawn eggs
        
    if(random.random() < 0.4):
        chest["Items"].append(createItemWithRandomDamage(383, 90, 96)) #various spawn eggs

    if(random.random() < 0.1):
        chest["Items"].append(createItemWithRandomDamage(383, 98, 98)) #ocelot spawn egg

    if(random.random() < 0.1):
        chest["Items"].append(createItemWithRandomDamage(383, 120, 120)) #villager spawn egg

    if(random.random() < 0.7):
        itemid = randomInRange(1, 5)
        count = randomInRange(10, 64)
        slot = randomInRange(0, 26)
        blocks = createItem(itemid, count, 0, slot)
        chest["Items"].append(blocks)

    sapling = createItemWithRandomDamage(6, 0, 3)
    sapling["Slot"] = TAG_Byte(randomInRange(0, 26))
    chest["Items"].append(sapling)

    chunk.TileEntities.append(chest)

# creates a random item in an item id range    
def createItemInRange(minid, maxid, count=1):
    itemid = randomInRange(minid, maxid)
    slot = randomInRange(0, 26)

    return createItem(itemid, count, 0, slot)

# creates an item with a randomized damage value
def createItemWithRandomDamage(itemid, mindmg, maxdmg, count=1):
    dmg = randomInRange(mindmg, maxdmg)
    slot = randomInRange(0, 26)
    
    return createItem(itemid, count, dmg, slot)

# creates an item
def createItem(itemid, count=1, damage=0, slot=0):
    item = TAG_Compound()

    item["id"] = TAG_Short(itemid)
    item["Damage"] = TAG_Short(damage)
    item["Count"] = TAG_Byte(count)
    item["Slot"] = TAG_Byte(slot)

    return item

# returns a random integer between minr and maxr, inclusive
def randomInRange(minr, maxr):
    return int(random.random() * (maxr - minr + 1)) + minr