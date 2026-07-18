from collections.abc import Mapping
from typing import Any, TextIO

from worlds.AutoWorld import World

from . import items, locations, regions, rules#, web_world
from . import options as yaml_options

class FantasticFistWorld(World):
    """
    Fantastic Fist is a 2D platformer which uses both keyboard and mouse controls.
    """

    game = "Fantastic Fist"

    #web = web_world.FantasticFistWebWorld()

    options_dataclass = yaml_options.FantasticFistOptions
    options: yaml_options.FantasticFistOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    randomized_entrances: list[regions.Edge] = []
    randomized_doors: list[regions.Edge] = []
    secret_exit_room_order: list[int] = []
    true_coin_amount: int = 0
    secret_coin_requirements: list[int] = []
    boss_coin_requirements: list[int] = []

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.FantasticFistItem:
        return items.create_item_with_correct_classification(self, name)
    
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        options = self.options.as_dict(
            "deathlink",
            "deathlink_amnesty",
            "goal",
            "open_world",
            "roomsanity",
            "checkpointsanity"
        )
        for i in range(7):
            options["secret_coin_req_" + str(i)] = self.secret_coin_requirements[i]
        for i in range(5):
            options["boss_coin_req_" + str(i)] = self.boss_coin_requirements[i]

        options["secret_exit_order"] = self.secret_exit_room_order

        entrances: list[str] = []
        for entrance in self.randomized_entrances:
            entrances.append(entrance.start_node.node_name)
            entrances.append(entrance.end_node.node_name)

        options["entrances"] = entrances

        doors: list[str] = []
        for door in self.randomized_doors:
            doors.append(door.start_node.node_name)
            doors.append(door.end_node.node_name)

        options["doors"] = doors
        return options

    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        spoiler_handle.write("True Coin Amount: " + str(self.true_coin_amount) + "\n")
        spoiler_handle.write("Secret Exit Coin Amount Requirments: [")
        for req in range(len(self.secret_coin_requirements)):
            spoiler_handle.write(str(self.secret_coin_requirements[req]))
            if req == 6:
                spoiler_handle.write("]\n")
            else:
                spoiler_handle.write(", ")

        spoiler_handle.write("Boss Level Coin Amount Requirments: [")
        for req in range(len(self.boss_coin_requirements)):
            spoiler_handle.write(str(self.boss_coin_requirements[req]))
            if req == 4:
                spoiler_handle.write("]\n")
            else:
                spoiler_handle.write(", ")

        spoiler_handle.write("----------MAP----------\n")
        for level_id in regions.ID_TO_LEVEL:
            level: regions.Level = regions.ID_TO_LEVEL[level_id]
            edges: list[regions.Edge] = regions.get_edge_from_start_node_name(self.randomized_entrances, level.level_id)
            spoiler_handle.write(edges[0].start_node.node_name)
            while len(edges) > 0:
                spoiler_handle.write(" -> " + edges[0].end_node.node_name)
                skipped_initial: bool = False
                for edge in edges:
                    if not skipped_initial:
                        skipped_initial = True
                        continue
                    spoiler_handle.write(" & " + edge.end_node.node_name)
                next_node_name: str = edges[0].end_node.node_name
                if next_node_name == "Verticality Room 2B" or next_node_name == "The Five Mile Spire Room 7B":
                    #Side rooms don't have additional pathing
                    next_node_name = edges[1].end_node.node_name
                edges = regions.get_edge_from_start_node_name(self.randomized_doors, next_node_name)
            spoiler_handle.write("\n")