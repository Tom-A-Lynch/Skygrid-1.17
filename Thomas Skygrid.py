# SkyGrid Filter by SethBling and @ThomasTruther
# Idea by SethBling, Made by @ThomasTruther
# Feel free to modify and reuse, but credit to SethBling and Thomas would be nice.

import random
import amulet
import amulet_nbt
from amulet.api.chunk import Chunk
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from amulet.api.block import Block
from amulet.utils.world_utils import block_coords_to_chunk_coords
from amulet_nbt import TAG_String, TAG_Int
from amulet.api.block_entity import BlockEntity

level = amulet.load_level("level")
level.platform("java")


nether = {}
b = {}
h = {}
f = {}
#Places block objects randomly on a grid every 4 blocks

def bigBang():
    for x in range(0,100):
        for z in range(0,100):
            genChunk = Chunk(x, z)
            for a in range(0, 4):
                for s in range(0, 4):
                    for y in range(0, 64):
                        (u_b_1, u_b_e_1, u_e_1,
                        ) = level.translation_manager.get_version("java", (1, 17, 1)).block.to_universal(random.choice(b))
                        block_id = level.block_palette.get_add_block(u_b_1)
                        chunk.blocks[a, y, s] = u_b_1



                        
            chunk.changed = True    




f[0] = Block("minecraft", "dandelion")
f[1] = Block("minecraft", "poppy")
f[2] = Block("minecraft", "blue_orchid")
f[3] = Block("minecraft", "allium")
f[4] = Block("minecraft", "azure_bluet")
f[5] = Block("minecraft", "red_tulip")
f[6] = Block("minecraft", "orange_tulip")
f[7] = Block("minecraft", "white_tulip")
f[8] = Block("minecraft", "pink_tulip")
f[9] = Block("minecraft", "oxeye_daisy")
f[10] = Block("minecraft", "cornflower")
f[11] = Block("minecraft", "lilly_of_the_valley")
f[12] = Block("minecraft", "sunflower")
f[13] = Block("minecraft", "lilac")
f[14] = Block("minecraft", "rose_bush")
f[15] = Block("minecraft", "peony")
f[16] = Block("minecraft", "fern")
f[17] = Block("minecraft", "sugar_cane")








#Fills b with weighted amounts of block objects

def weightedOverworldBlock():
                                                                      #Sum = 3501
    for i in range(0, 300):
        b.append(Block("minecraft", "stone"))                         #300            
    for i in range(0, 100):
        b.append(Block("minecraft", "granite"))                       #100
    for i in range(0, 100):
        b.append(Block("minecraft", "diorite"))                       #100
    for i in range(0, 100):
        b.append(Block("minecraft", "andesite"))                      #100
    for i in range(0, 100):
        b.append(Block("minecraft", "grass_block"))                   #100 
    for i in range(0, 200):
        b.append(Block("minecraft", "dirt"))                          #200
    for i in range(0, 20):
        b.append(Block("minecraft", "coarse_dirt"))                   #20  
    for i in range(0, 10):
        b.append(Block("minecraft", "podzol"))                        #10
    for i in range(0, 300):
        b.append(Block("minecraft", "sand"))                          #300
    for i in range(0, 30):
        b.append(Block("minecraft", "red_sand"))                      #30
    for i in range(0, 100):
        b.append(Block("minecraft", "gravel"))                        #100
    for i in range(0, 20):
        b.append(Block("minecraft", "gold_ore"))                      #20
    for i in range(0, 35):
        b.append(Block("minecraft", "iron_ore"))                      #35
    for i in range(0, 40):
        b.append(Block("minecraft", "coal_ore"))                      #40
    for i in range(0, 60):
        b.append(Block("minecraft", "oak_log"))                       #60
    for i in range(0, 60):
        b.append(Block("minecraft", "spruce_log"))                    #60
    for i in range(0, 60):
        b.append(Block("minecraft", "birch_log"))                     #60
    for i in range(0, 60):
        b.append(Block("minecraft", "jungle_log"))                    #60
    for i in range(0, 60):
        b.append(Block("minecraft", "acacia_log"))                    #60
    for i in range(0, 60):
        b.append(Block("minecraft", "dark_oak_log"))                  #60
    for i in range(0, 50):
        b.append(Block("minecraft", "oak_leaves"))                    #50
    for i in range(0, 50):
        b.append(Block("minecraft", "spruce_leaves"))                 #50
    for i in range(0, 50):
        b.append(Block("minecraft", "birch_leaves"))                  #50
    for i in range(0, 50):
        b.append(Block("minecraft", "jungle_leaves"))                 #50
    for i in range(0, 50):
        b.append(Block("minecraft", "acacia_leaves"))                 #50
    for i in range(0, 50):
        b.append(Block("minecraft", "dark_oak_leaves"))               #50 
    for i in range(0, 3):
        b.append(Block("minecraft", "sponge"))                        #3
    for i in range(0, 13):
        b.append(Block("minecraft", "lapis_ore"))                     #13
    for i in range(0, 50):
        b.append(Block("minecraft", "sandstone"))                     #50
    for i in range(0, 3):
        b.append(Block("minecraft", "note block"))                    #3
    for i in range(0, 40):
        b.append(Block("minecraft", "white_wool"))                    #40
    for i in range(0, 4):
        b.append(Block("minecraft", "orange_wool"))                   #4
    for i in range(0, 4):
        b.append(Block("minecraft", "magenta_wool"))                  #4
    for i in range(0, 4):
        b.append(Block("minecraft", "light_blue_wool"))               #4  
    for i in range(0, 4):
        b.append(Block("minecraft", "yellow_wool"))                   #4
    for i in range(0, 4):
        b.append(Block("minecraft", "lime_wool"))                     #4
    for i in range(0, 4):
        b.append(Block("minecraft", "pink_wool"))                     #4
    for i in range(0, 4):
        b.append(Block("minecraft", "gray_wool"))                     #4
    for i in range(0, 4):
        b.append(Block("minecraft", "light_gray_wool"))               #4  
    for i in range(0, 4):
        b.append(Block("minecraft", "cyan_wool"))                     #4
    for i in range(0, 4):
        b.append(Block("minecraft", "purple_wool"))                   #4
    for i in range(0, 4):
        b.append(Block("minecraft", "blue_wool"))                     #4
    for i in range(0, 4):
        b.append(Block("minecraft", "brown_wool"))                    #4
    for i in range(0, 4):
        b.append(Block("minecraft", "green_wool"))                    #4
    for i in range(0, 4):
        b.append(Block("minecraft", "red_wool"))                      #4
    for i in range(0, 4):
        b.append(Block("minecraft", "black_wool"))                    #4
    for i in range(0, 2):
        b.append(Block("minecraft", "gold_block"))                    #2
    for i in range(0, 4):
        b.append(Block("minecraft", "iron_block"))                    #4
    for i in range(0, 4):
        b.append(Block("minecraft", "bricks"))                        #4
    for i in range(0, 9):
        b.append(Block("minecraft", "tnt"))                           #9
    for i in range(0, 12):
        b.append(Block("minecraft", "bookshelf"))                     #12
    for i in range(0, 11):
        b.append(Block("minecraft", "mossy_cobblestone"))             #11
    for i in range(0, 19):
        b.append(Block("minecraft", "obsidian"))                      #19
    for i in range(0, 11):
        b.append(Block("minecraft", "diamond_ore"))                   #11
    for i in range(0, 1):
        b.append(Block("minecraft", "diamond_block"))                 #1
    for i in range(0, 5):
        b.append(Block("minecraft", "furnace"))                       #5
    for i in range(0, 5):
        b.append(Block("minecraft", "crafting_table"))                #5
    for i in range(0, 18):
        b.append(Block("minecraft", "redstone_ore"))                  #18
    for i in range(0, 40):
        b.append(Block("minecraft", "ice"))                           #40
    for i in range(0, 40):
        b.append(Block("minecraft", "snow_block"))                    #40
    for i in range(0, 16):
        b.append(Block("minecraft", "melon"))                         #16
    for i in range(0, 2):
        b.append(Block("minecraft", "mycelium"))                      #2
    for i in range(0, 24):
        b.append(Block("minecraft", "pumpkin"))                       #24
    for i in range(0, 1):
        b.append(Block("minecraft", "jukebox"))                       #1
    for i in range(0, 2):
        b.append(Block("minecraft", "enchanting_table"))              #2
    for i in range(0, 5):
        b.append(Block("minecraft", "emerald_ore"))                   #5
    for i in range(0, 1):
        b.append(Block("minecraft", "emerald_block"))                 #1
    for i in range(0, 5):
        b.append(Block("minecraft", "redstone_block"))                #5
    for i in range(0, 60):
        b.append(Block("minecraft", "terracotta"))                    #60
    for i in range(0, 10):
        b.append(Block("minecraft", "hay_block"))                     #10
    for i in range(0, 5):
        b.append(Block("minecraft", "coal_block"))                    #5
    for i in range(0, 20):
        b.append(Block("minecraft", "packed_ice"))                   #20
    for i in range(0, 3):
        b.append(Block("minecraft", "slime_block"))                   #3
    for i in range(0, 30):
        b.append(Block("minecraft", "prismarine"))                    #30
    for i in range(0, 5):
        b.append(Block("minecraft", "sea_lantern"))                   #5
    for i in range(0, 2):
        b.append(Block("minecraft", "magma_block"))                   #2
    for i in range(0, 1):
        b.append(Block("minecraft", "white_glazed_terracotta"))       #1
    for i in range(0, 6):
        b.append(Block("minecraft", "blue_ice"))                      #6
    for i in range(0, 20):
        b.append(Block("minecraft", "amethyst_block"))                #20
    for i in range(0, 50):
        b.append(Block("minecraft", "azalea_leaves"))                 #50
    for i in range(0, 10):
        b.append(Block("minecraft", "budding_amethyst"))              #10
    for i in range(0, 150):
        b.append(Block("minecraft", "deepslate"))                     #150
    for i in range(0, 25):
        b.append(Block("minecraft", "calcite"))                       #25
    for i in range(0, 30):
        b.append(Block("minecraft", "copper_ore"))                    #30
    for i in range(0, 4):
        b.append(Block("minecraft", "copper_block"))                  #4
    for i in range(0, 40):
        b.append(Block("minecraft", "deepslate_coal_ore"))            #40
    for i in range(0, 30):
        b.append(Block("minecraft", "deepslate_copper_ore"))          #30
    for i in range(0, 11):
        b.append(Block("minecraft", "deepslate_diamond_ore"))         #11
    for i in range(0, 5):
        b.append(Block("minecraft", "deepslate_emerald_ore"))         #5
    for i in range(0, 35):
        b.append(Block("minecraft", "deepslate_iron_ore"))            #35
    for i in range(0, 20):
        b.append(Block("minecraft", "deepslate_gold_ore"))            #20
    for i in range(0, 13):
        b.append(Block("minecraft", "deepslate_lapis_ore"))           #13
    for i in range(0, 18):
        b.append(Block("minecraft", "deepslate_redstone_ore"))        #18
    for i in range(0, 20):
        b.append(Block("minecraft", "dripstone_block"))               #20
    for i in range(0, 50):
        b.append(Block("minecraft", "flowering_azalea_leaves"))       #50
    for i in range(0, 123):
        b.append(Block("minecraft", "moss_block"))                    #123
    for i in range(0, 6):
        b.append(Block("minecraft", "raw_copper_block"))              #6
    for i in range(0, 4):
        b.append(Block("minecraft", "raw_gold_block"))                #4
    for i in range(0, 6):
        b.append(Block("minecraft", "raw_iron_block"))                #6
    for i in range(0, 20):
        b.append(Block("minecraft", "rooted_dirt"))                   #20
    for i in range(0, 21):
        b.append(Block("minecraft", "tuff"))                         #21
    for i in range(0, 1):
        b.append(Block("minecraft", "orange_glazed_terracotta"))     #1
    for i in range(0, 1):
        b.append(Block("minecraft", "magenta_glazed_terracotta"))    #1
    for i in range(0, 1):
        b.append(Block("minecraft", "light_blue_glazed_terracotta")) #1
    for i in range(0, 1):
        b.append(Block("minecraft", "yellow_glazed_terracotta"))     #1
    for i in range(0, 1):
        b.append(Block("minecraft", "lime_glazed_terracotta"))       #1
    for i in range(0, 1):
        b.append(Block("minecraft", "pink_glazed_terracotta"))       #1
    for i in range(0, 1):
        b.append(Block("minecraft", "gray_glazed_terracotta"))       #1
    for i in range(0, 1):
        b.append(Block("minecraft", "light_gray_glazed_terracotta")) #1
    for i in range(0, 1):
        b.append(Block("minecraft", "cyan_glazed_terracotta"))       #1
    for i in range(0, 1):
        b.append(Block("minecraft", "purple_glazed_terracotta"))     #1
    for i in range(0, 1):
        b.append(Block("minecraft", "blue_glazed_terracotta"))       #1
    for i in range(0, 1):
        b.append(Block("minecraft", "brown_glazed_terracotta"))      #1
    for i in range(0, 1):
        b.append(Block("minecraft", "green_glazed_terracotta"))      #1
    for i in range(0, 1):
        b.append(Block("minecraft", "red_glazed_terracotta"))        #1
    for i in range(0, 1):
        b.append(Block("minecraft", "black_glazed_terracotta"))      #1
    for i in range(0, 1):
        b.append(Block("minecraft", "white_concrete"))               #1
    for i in range(0, 1):
        b.append(Block("minecraft", "blue_concrete"))                #1
    for i in range(0, 1):
        b.append(Block("minecraft", "black_concrete"))               #1
    for i in range(0, 1):
        b.append(Block("minecraft", "red_concrete"))                 #1
    for i in range(0, 1):
        b.append(Block("minecraft", "green_concrete"))               #1
    for i in range(0, 1):
        b.append(Block("minecraft", "pink_concrete"))                #1
    for i in range(0, 1):
        b.append(Block("minecraft", "yellow_concrete"))              #1
    for i in range(0, 1):
        b.append(Block("minecraft", "cyan_concrete"))                #1
    for i in range(0, 1):
        b.append(Block("minecraft", "gray_concrete"))                #1
    for i in range(0, 1):
        b.append(Block("minecraft", "light_gray_concrete"))          #1
    for i in range(0, 1):
        b.append(Block("minecraft", "light_blue_concrete"))          #1
    for i in range(0, 1):
        b.append(Block("minecraft", "lime_concrete"))                #1
    for i in range(0, 1):
        b.append(Block("minecraft", "brown_concrete"))               #1
    for i in range(0, 1):
        b.append(Block("minecraft", "purple_concrete"))              #1
    for i in range(0, 1):
        b.append(Block("minecraft", "magenta_concrete"))             #1
    for i in range(0, 1):
        b.append(Block("minecraft", "orange_concrete"))              #1
    for i in range(0, 25):
        b.append(Block("minecraft", "clay"))                         #25
    for i in range(0, 2):
        b.append(Block("minecraft", "redstone_lamp"))                #2
    for i in range(0, 2):
        b.append(Block("minecraft", "cobweb"))                       #2
    for i in range(0, 2):
        b.append(Block("minecraft", "jack_o_lantern"))               #2
    for i in range(0, 50):
        b.append(Block("minecraft", "water"))                        #50
    for i in range(0, 15):
        b.append(Block("minecraft", "lava"))                         #15


def weightedNetherBlock():
    for i in range(0, 200):
        nether.append(Block("minecraft", "lava"))                         #15
    for i in range(0, 40):
        nether.append(Block("minecraft", "obsidian"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "glowstone"))
    for i in range(0, 500):
        nether.append(Block("minecraft", "netherrack"))
    for i in range(0, 200):
        nether.append(Block("minecraft", "soul_sand"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "nther_quartz_ore"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "magma_block"))
    for i in range(0, 200):
        nether.append(Block("minecraft", "nether_bricks"))
    for i in range(0, 20):
        nether.append(Block("minecraft", "red_nether_bricks"))
    for i in range(0, 10):
        nether.append(Block("minecraft", "nether_wart_block"))
    for i in range(0, 150):
        nether.append(Block("minecraft", "crimson_nylium"))
    for i in range(0, 150):
        nether.append(Block("minecraft", "warped_nylium"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "nether_gold_ore"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "warped_stem"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "crimson_stem"))
    for i in range(0, 100):
        nether.append(Block("minecraft", "soul_soil"))
    for i in range(0, 250):
        nether.append(Block("minecraft", "basalt"))
    for i in range(0, 3):
        nether.append(Block("minecraft", "lodestone"))
    for i in range(0, 30):
        nether.append(Block("minecraft", "ancient_debris"))
    for i in range(0, 20):
        nether.append(Block("minecraft", "crying_obsidian"))
    for i in range(0, 250):
        nether.append(Block("minecraft", "blackstone"))
    for i in range(0, 1):
        nether.append(Block("minecraft", "netherite_block"))
    for i in range(0, 35):
        nether.append(Block("minecraft", "gilded_blackstone"))
    for i in range(0, 86):
        nether.append(Block("minecraft", "shroomlight"))



weightedOverworldBlock()
bigBang()