import amulet
from amulet.api.block import Block
from amulet.utils.world_utils import block_coords_to_chunk_coords
from amulet_nbt import TAG_String, TAG_Int


level = amulet.load_level("level")

java_block = Block(
    "minecraft", "green_glazed_terracotta", {"facing": TAG_String("south")}
)


(
    universal_block_1,
    universal_block_entity_1,
    universal_extra_1,
) = level.translation_manager.get_version("java", (1, 17, 1)).block.to_universal(
    java_block
    
)


block_id_1 = level.block_palette.get_add_block(universal_block_1)

x, z = 15, 17
cx, cz = block_coords_to_chunk_coords(x, z)
chunk = level.get_chunk(cx, cz, "minecraft:overworld")
offset_x, offset_z = x - 16 * cx, z - 16 * cz


chunk.blocks[offset_x, 70, offset_z] = block_id_1



for block_entity, location in (
    (universal_block_entity_1, (15, 70, 17)),
    (universal_block_entity_2, (15, 72, 17)),
):
    if block_entity is not None:
    
        chunk.block_entities[location] = block_entity
    elif location in chunk.block_entities:
        
        del chunk.block_entities[location]

chunk.changed = True

level.save()
level.close()