from __future__ import annotations

from typing import TYPE_CHECKING

from . import regions

from BaseClasses import Location, Entrance
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule

if TYPE_CHECKING:
    from .world import FantasticFistWorld

HAS_SMASH_BLOCKS = (Has("Destructible Blocks") | 
                    Has("Progressive Destructible Blocks", count = 1) |
                    Has("Smash Blocks"))
HAS_BURNABLE_BLOCKS = (Has("Destructible Blocks") |
                        Has("Progressive Destructible Blocks", count = 2) |
                        Has("Burnable Blocks"))
HAS_SNAKE_BLOCKS = (Has("Destructible Blocks") |
                    Has("Progressive Destructible Blocks", count = 3) |
                    Has("Snake Blocks"))

HAS_STANDARD_PHYSICS_BLOCKS = (Has("Physics Blocks") |
                                Has("Progressive Physics Blocks", count = 1) |
                                Has("Standard Physics Blocks"))
HAS_ICE_BLOCKS = (Has("Physics Blocks") |
                    Has("Progressive Physics Blocks", count = 2) |
                    Has("Ice Blocks"))
HAS_YELLOW_PHYSICS_BLOCKS = (Has("Physics Blocks") |
                                Has("Progressive Physics Blocks", count = 3) |
                                Has("Yellow Physics Blocks"))
HAS_CONCRETE_BLOCKS = (Has("Physics Blocks") |
                        Has("Progressive Physics Blocks", count = 4) |
                        Has("Concrete Blocks"))
HAS_ELECTRIC_BLOCKS = (Has("Physics Blocks") |
                        Has("Progressive Physics Blocks", count = 5) |
                        Has("Electric Blocks"))
HAS_LINE_BLOCKS = (Has("Physics Blocks") |
                    Has("Progressive Physics Blocks", count = 6) |
                    Has("Line Blocks"))

HAS_STANDARD_SLIDING_BLOCKS = (Has("Sliding Blocks") | 
                                Has("Progressive Sliding Blocks", count = 1) | 
                                Has("Standard Sliding Blocks"))
HAS_YELLOW_SLIDING_BLOCKS = (Has("Sliding Blocks") | 
                                Has("Progressive Sliding Blocks", count = 2) | 
                                Has("Yellow Sliding Blocks"))
HAS_BLUE_SLIDING_BLOCKS = (Has("Sliding Blocks") | 
                            Has("Progressive Sliding Blocks", count = 3) | 
                            Has("Blue Sliding Blocks"))
HAS_CRYSTAL_SLIDING_BLOCKS = (Has("Sliding Blocks") | 
                                Has("Progressive Sliding Blocks", count = 4) | 
                                Has("Crystal Sliding Blocks"))
HAS_GALACTIC_SLIDING_BLOCKS = (Has("Sliding Blocks") | 
                                Has("Progressive Sliding Blocks", count = 5) | 
                                Has("Galactic Sliding Blocks"))

HAS_STANDARD_STAR_BLOCKS = (Has("Boss Blocks") | 
                            Has("Progressive Boss Blocks", count = 1) | 
                            Has("Standard Star Blocks"))
HAS_YELLOW_STAR_BLOCKS = (Has("Boss Blocks") | 
                            Has("Progressive Boss Blocks", count = 2) | 
                            Has("Yellow Star Blocks"))
HAS_BLUE_STAR_BLOCKS = (Has("Boss Blocks") | 
                        Has("Progressive Boss Blocks", count = 3) | 
                        Has("Blue Star Blocks"))
HAS_STANDARD_HEART_BLOCKS = (Has("Boss Blocks") | 
                                Has("Progressive Boss Blocks", count = 4) | 
                                Has("Standard Heart Blocks"))
HAS_SLIDING_HEART_BLOCKS = (Has("Boss Blocks") | 
                            Has("Progressive Boss Blocks", count = 5) | 
                            Has("Sliding Heart Blocks"))
HAS_DELAYED_HEART_BLOCKS = (Has("Boss Blocks") | 
                            Has("Progressive Boss Blocks", count = 6) | 
                            Has("Delayed Heart Blocks"))

HAS_STANDARD_POP_BLOCKS = (Has("Pop Blocks") | 
                           Has("Progressive Pop Blocks", count = 1) | 
                           Has("Standard Pop Blocks"))
HAS_GALACTIC_POP_BLOCKS = (Has("Pop Blocks") | 
                           Has("Progressive Pop Blocks", count = 2) | 
                           Has("Galactic Pop Blocks"))

HAS_STANDARD_BUMPERS = (Has("Bumpers") | 
                        Has("Progressive Bumpers", count = 1) | 
                        Has("Standard Bumpers"))
HAS_DIRECTIONAL_BUMPERS = (Has("Bumpers") | 
                           Has("Progressive Bumpers", count = 2) | 
                           Has("Directional Bumpers"))
HAS_YELLOW_BUMPERS = (Has("Bumpers") | 
                      Has("Progressive Bumpers", count = 3) | 
                      Has("Yellow Bumpers"))
HAS_BLACK_HOLE_BUMPERS = (Has("Bumpers") | 
                          Has("Progressive Bumpers", count = 4) | 
                          Has("Black Hole Bumpers"))

HAS_BLUE_SWITCHES = (Has("Switches") | 
                     Has("Progressive Switches", count = 1) | 
                     Has("Blue Switches"))
HAS_ORANGE_SWITCHES = (Has("Switches") |
                       Has("Progressive Switches", count = 2) |
                       Has("Orange Switches"))

HAS_STANDARD_PUNCHAPPEAR_BLOCKS = (Has("Punchappear Blocks") | 
                                   Has("Progressive Punchappear Blocks", count = 1) | 
                                   Has("Standard Punchappear Blocks"))
HAS_YELLOW_PUNCHAPPEAR_BLOCKS = (Has("Punchappear Blocks") | 
                                 Has("Progressive Punchappear Blocks", count = 2) | 
                                 Has("Yellow Punchappear Blocks"))
HAS_BLUE_PUNCHAPPEAR_BLOCKS = (Has("Punchappear Blocks") | 
                               Has("Progressive Punchappear Blocks", count = 3) | 
                               Has("Blue Punchappear Blocks"))
HAS_ORANGE_PUNCHAPPEAR_BLOCKS = (Has("Punchappear Blocks") | 
                                 Has("Progressive Punchappear Blocks", count = 4) | 
                                 Has("Orange Punchappear Blocks"))

HAS_YELLOW_SKULL_BLOCKS = (Has("Skull Blocks") | 
                           Has("Progressive Skull Blocks", count = 1) | 
                           Has("Yellow Skull Blocks"))
HAS_BLUE_SKULL_BLOCKS = (Has("Skull Blocks") | 
                         Has("Progressive Skull Blocks", count = 2) | 
                         Has("Blue Skull Blocks"))
HAS_ORANGE_SKULL_BLOCKS = (Has("Skull Blocks") | 
                           Has("Progressive Skull Blocks", count = 3) | 
                           Has("Orange Skull Blocks"))

HAS_YELLOW_SKULL_RINGS = (Has("Skull Rings") | 
                          Has("Progressive Skull Rings", count = 1) | 
                          Has("Yellow Skull Rings"))
HAS_BLUE_SKULL_RINGS = (Has("Skull Rings") | 
                        Has("Progressive Skull Rings", count = 2) | 
                        Has("Blue Skull Rings"))

HAS_GUBES = (Has("Enemies") | 
             Has("Progressive Enemies", count = 1) | 
             Has("Gubes"))
HAS_YELLOW_GORBS = (Has("Enemies") | 
                    Has("Progressive Enemies", count = 2) | 
                    Has("Yellow Gorbs"))
HAS_BLUE_GORBS = (Has("Enemies") | 
                  Has("Progressive Enemies", count = 3) | 
                  Has("Blue Gorbs"))
HAS_PIXIES = (Has("Enemies") | 
              Has("Progressive Enemies", count = 4) | 
              Has("Pixies"))

HAS_STANDARD_VIVI_BLOCKS = (Has("Vivi Blocks") | 
                            Has("Progressive Vivi Blocks", count = 1) | 
                            Has("Standard Vivi Blocks"))
HAS_YELLOW_VIVI_BLOCKS = (Has("Vivi Blocks") | 
                          Has("Progressive Vivi Blocks", count = 2) | 
                          Has("Yellow Vivi Blocks"))
HAS_FIREWORK_VIVI_BLOCKS = (Has("Vivi Blocks") | 
                            Has("Progressive Vivi Blocks", count = 3) | 
                            Has("Firework Vivi Blocks"))

HAS_STANDARD_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                                Has("Progressive Block Launchers", count = 1) | 
                                Has("Standard Block Launchers"))
HAS_WING_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                            Has("Progressive Block Launchers", count = 2) | 
                            Has("Wing Block Launchers"))
HAS_PEARL_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                             Has("Progressive Block Launchers", count = 3) | 
                             Has("Pearl Block Launchers"))
HAS_ICE_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                           Has("Progressive Block Launchers", count = 4) | 
                           Has("Ice Block Launchers"))
HAS_YELLOW_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                              Has("Progressive Block Launchers", count = 5) | 
                              Has("Yellow Block Launchers"))
HAS_BLUE_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                            Has("Progressive Block Launchers", count = 6) | 
                            Has("Blue Block Launchers"))
HAS_INVERTED_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                                Has("Progressive Block Launchers", count = 7) | 
                                Has("Inverted Block Launchers"))
HAS_GALACTIC_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                                Has("Progressive Block Launchers", count = 8) | 
                                Has("Galactic Block Launchers"))
HAS_FIRE_BLOCK_LAUNCHERS = (Has("Block Launchers") | 
                            Has("Progressive Block Launchers", count = 9) | 
                            Has("Fire Block Launchers"))

HAS_STANDARD_LAUNCHERS = (Has("Launchers") | 
                          Has("Progressive Launchers", count = 1) | 
                          Has("Standard Launchers"))
HAS_BLUE_PEARL_LAUNCHERS = (Has("Launchers") | 
                            Has("Progressive Launchers", count = 2) | 
                            Has("Blue Pearl Launchers"))
HAS_RED_PEARL_LAUNCHERS = (Has("Launchers") | 
                           Has("Progressive Launchers", count = 3) | 
                           Has("Red Pearl Launchers"))
HAS_YELLOW_CRYSTAL_LAUNCHERS = (Has("Launchers") | 
                                Has("Progressive Launchers", count = 4) | 
                                Has("Yellow Crystal Launchers"))
HAS_BLUE_CRYSTAL_LAUNCHERS = (Has("Launchers") | 
                              Has("Progressive Launchers", count = 5) | 
                              Has("Blue Crystal Launchers"))
HAS_MOON_LAUNCHERS = (Has("Launchers") | 
                      Has("Progressive Launchers", count = 6) | 
                      Has("Moon Launchers"))

HAS_STANDARD_SPINNERS = (Has("Hazards") | 
                         Has("Progressive Hazards", count = 1) | 
                         Has("Standard Spinners"))
HAS_STAR_SPINNERS = (Has("Hazards") | 
                     Has("Progressive Hazards", count = 2) | 
                     Has("Star Spinners"))
HAS_RED_FIRE_RINGS = (Has("Hazards") | 
                      Has("Progressive Hazards", count = 3) | 
                      Has("Red Fire Rings"))
HAS_BLUE_FIRE_RINGS = (Has("Hazards") | 
                       Has("Progressive Hazards", count = 4) | 
                       Has("Blue Fire Rings"))

HAS_GREEN_BUBBLES = (Has("Bubbles") | 
                          Has("Progressive Bubbles", count = 1) | 
                          Has("Green Bubbles"))
HAS_KEY_BUBBLES = (Has("Bubbles") | 
                   Has("Progressive Bubbles", count = 2) | 
                   Has("Key Bubbles"))
HAS_NUMBER_BUBBLES = (Has("Bubbles") | 
                      Has("Progressive Bubbles", count = 3) | 
                      Has("Number Bubbles"))
HAS_CLEAR_BUBBLES = (Has("Bubbles") | 
                     Has("Progressive Bubbles", count = 4) | 
                     Has("Clear Bubbles"))
HAS_HONEY_BUBBLES = (Has("Bubbles") | 
                     Has("Progressive Bubbles", count = 5) | 
                     Has("Honey Bubbles"))

HAS_RED_BALLOONS = (Has("Balloons") | 
                    Has("Progressive Balloons", count = 1) | 
                    Has("Red Balloons"))
HAS_BLUE_BALLOONS = (Has("Balloons") | 
                     Has("Progressive Balloons", count = 2) | 
                     Has("Blue Balloons"))
HAS_LEAD_BALLOONS = (Has("Balloons") | 
                     Has("Progressive Balloons", count = 3) | 
                     Has("Lead Balloons"))
HAS_TOGGLE_BALLOONS = (Has("Balloons") | 
                       Has("Progressive Balloons", count = 4) | 
                       Has("Toggle Balloons"))

HAS_BOMB_FLOWERS = (Has("Bombs") | 
                    Has("Progressive Bombs", count = 1) | 
                    Has("Bomb Flowers"))
HAS_BOMB_BLOCKS = (Has("Bombs") | 
                   Has("Progressive Bombs", count = 2) | 
                   Has("Bomb Blocks"))
HAS_HIVE_BOMBS = (Has("Bombs") | 
                 Has("Progressive Bombs", count = 3) | 
                 Has("Hive Bombs"))

HAS_BLUE_HIVE_BLOCKS = (Has("Hive Blocks") | 
                        Has("Progressive Hive Blocks", count = 1) | 
                        Has("Blue Hive Blocks"))
HAS_RED_HIVE_BLOCKS = (Has("Hive Blocks") | 
                       Has("Progressive Hive Blocks", count = 2) | 
                       Has("Red Hive Blocks"))

HAS_STANDARD_KEY_BLOCKS = (Has("Keys") | 
                           Has("Progressive Keys", count = 1) | 
                           Has("Standard Key Blocks"))
HAS_KEY_QUARTETS = (Has("Keys") | 
                    Has("Progressive Keys", count = 2) | 
                    Has("Key Quartets"))
HAS_ICE_KEY_BLOCKS = (Has("Keys") | 
                      Has("Progressive Keys", count = 3) | 
                      Has("Ice Key Blocks"))
HAS_INVERTED_KEY_BLOCKS = (Has("Keys") | 
                           Has("Progressive Keys", count = 4) | 
                           Has("Inverted Key Blocks"))

HAS_UP_GRAVITY_FLIPPERS = (Has("Gravity Items") | 
                           Has("Progressive Gravity Items", count = 1) | 
                           Has("Up Gravity Flippers"))
HAS_DOWN_GRAVITY_FLIPPERS = (Has("Gravity Items") | 
                             Has("Progressive Gravity Items", count = 2) | 
                             Has("Down Gravity Flippers"))
HAS_UP_GRAVITY_FIELDS = (Has("Gravity Items") | 
                         Has("Progressive Gravity Items", count = 3) | 
                         Has("Up Gravity Fields"))
HAS_DOWN_GRAVITY_FIELDS = (Has("Gravity Items") | 
                           Has("Progressive Gravity Items", count = 4) | 
                           Has("Down Gravity Fields"))
HAS_UP_WATER = (Has("Gravity Items") | 
                Has("Progressive Gravity Items", count = 5) | 
                Has("Up Water"))
HAS_DOWN_WATER = (Has("Gravity Items") | 
                  Has("Progressive Gravity Items", count = 6) | 
                  Has("Down Water"))
HAS_GRAVITY_FISTS = (Has("Gravity Items") | 
                     Has("Progressive Gravity Items", count = 7) | 
                     Has("Gravity Fists"))
HAS_GRAVITY_ANCHORS = (Has("Gravity Items") | 
                       Has("Progressive Gravity Items", count = 8) | 
                       Has("Gravity Anchors"))

HAS_ARROW_LIFTS = (Has("Lifts") | 
                   Has("Progressive Lifts", count = 1) | 
                   Has("Arrow Lifts"))
HAS_YELLOW_LIFTS = (Has("Lifts") | 
                    Has("Progressive Lifts", count = 2) | 
                    Has("Yellow Lifts"))
HAS_HIVE_LIFTS = (Has("Lifts") | 
                  Has("Progressive Lifts", count = 3) | 
                  Has("Hive Lifts"))

HAS_STANDARD_SEMISOLIDS = (Has("Semisolids") | 
                           Has("Progressive Semisolids", count = 1) | 
                           Has("Standard Semisolids"))
HAS_INVERTED_SEMISOLIDS = (Has("Semisolids") | 
                           Has("Progressive Semisolids", count = 2) | 
                           Has("Inverted Semisolids"))
HAS_TOGGLE_SEMISOLIDS = (Has("Semisolids") | 
                         Has("Progressive Semisolids", count = 3) | 
                         Has("Toggle Semisolids"))

HAS_ON_OFF_BLOCKS = Has("On Off Blocks")
HAS_TIMER_BUTTONS = Has("Timer Buttons")
HAS_TOGGLE_FLOWERS = Has("Toggle Flowers")
HAS_TETHERS = Has("Tethers")
HAS_ICICLES = Has("Icicles")
HAS_GLASS_BLOCKS = Has("Glass Blocks")
HAS_THERMALS = Has("Thermals")
HAS_GOLF_BALL = Has("Golf Ball")
HAS_GOLF_CART = Has("Golf Cart")
HAS_FALLING_CRYSTALS = Has("Falling Crystals")
HAS_GRAB_BLOCKS = Has("Grab Blocks")
HAS_MIRRORS = Has("Mirrors")
HAS_BARRELS = Has("Barrels")
HAS_PILLARS = Has("Pillars")
HAS_YELLOW_SPIN_BLOCKS = Has("Yellow Spin Blocks")
HAS_TREES = Has("Trees")

# Intended, Simple, Advanced, Glitched
ITEM_REQUIREMENTS = {
    #Introduction
    "Introduction Room 1 Door": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS & 
                                  HAS_DOWN_WATER),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS)],
    "Introduction Coin 1": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                            (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                            (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                            (HAS_SMASH_BLOCKS)],
    "Introduction Room 2 Door": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS)],
    "Introduction Checkpoint 1": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS & 
                                   HAS_DOWN_WATER),
                                  (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_SMASH_BLOCKS)],
    "Introduction Room 3 Door": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS & 
                                  HAS_DOWN_WATER),
                                 (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                                 (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                                 (HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS)],
    "Introduction Coin 2": [(HAS_SMASH_BLOCKS),
                            None,
                            None,
                            None],
    "Introduction Level Clear": [(HAS_SMASH_BLOCKS & HAS_DOWN_WATER),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS),
                                 (HAS_SMASH_BLOCKS)],
    #The Caves
    "The Caves Coin 1": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS & 
                          HAS_STANDARD_KEY_BLOCKS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS)],
    "The Caves Room 1 Door": [(HAS_SMASH_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS & 
                               HAS_STANDARD_KEY_BLOCKS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS)],
    "The Caves Checkpoint 1": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS)],
    "The Caves Load Bearing Collectible": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS & 
                                            HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS &
                                            HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS &
                                            HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS,
                                            HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS)],
    "The Caves Room 2 Door": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS)],
    "The Caves Coin 2": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                         (HAS_STANDARD_BLOCK_LAUNCHERS),
                         (HAS_STANDARD_PHYSICS_BLOCKS | HAS_STANDARD_BLOCK_LAUNCHERS),
                         (HAS_STANDARD_PHYSICS_BLOCKS | HAS_STANDARD_BLOCK_LAUNCHERS)],
    "The Caves Checkpoint 2": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS & 
                                HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS)],
    "The Caves Room 3 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS & 
                               HAS_WING_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS &
                               HAS_STANDARD_SPINNERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS &
                               HAS_STANDARD_SPINNERS),
                              (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_WING_BLOCK_LAUNCHERS &
                               HAS_STANDARD_SPINNERS)],
    "The Caves Coin 3": [(HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS & 
                          HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS &
                          HAS_STANDARD_BLOCK_LAUNCHERS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                         (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS)],
    "The Caves Level Clear": [(HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS & 
                               HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS &
                               HAS_STANDARD_BLOCK_LAUNCHERS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS),
                              (HAS_SMASH_BLOCKS & HAS_STANDARD_KEY_BLOCKS)],
    #Get A Grip
    "Get A Grip Coin 1": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                          (HAS_ON_OFF_BLOCKS),
                          (HAS_ON_OFF_BLOCKS),
                          (HAS_ON_OFF_BLOCKS)],
    "Get A Grip Room 1 Door": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_PHYSICS_BLOCKS),
                               (HAS_ON_OFF_BLOCKS),
                               (HAS_ON_OFF_BLOCKS),
                               (HAS_ON_OFF_BLOCKS)],
    "Get A Grip Checkpoint 1": [(HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                 HAS_GUBES & HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_ON_OFF_BLOCKS)],
    "Get A Grip Room 2 Door": [(HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_GUBES & HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS & HAS_SMASH_BLOCKS),
                               (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS & HAS_SMASH_BLOCKS),
                               (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS)],
    "Get A Grip Checkpoint 2": [(HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                                (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS)],
    "Get A Grip Level Clear": [(HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                               (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                               (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS),
                               (HAS_STANDARD_LAUNCHERS & HAS_ON_OFF_BLOCKS)],
    #Verticality
    "Verticality Room 1 Door": [(HAS_STANDARD_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                 HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS),
                                (HAS_STANDARD_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_STANDARD_BLOCK_LAUNCHERS),
                                None],
    "Verticality Load Bearing Collectible": [(HAS_STANDARD_LAUNCHERS & HAS_STANDARD_SPINNERS & 
                                              HAS_STANDARD_BLOCK_LAUNCHERS),
                                             (HAS_STANDARD_LAUNCHERS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                             (HAS_STANDARD_LAUNCHERS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                             (HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Verticality Coin 1": [(HAS_STANDARD_LAUNCHERS & HAS_STANDARD_SPINNERS &
                            HAS_STANDARD_BUMPERS),
                           (HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_LAUNCHERS)],
    "Verticality Room 2 Side Door": [(HAS_STANDARD_LAUNCHERS & HAS_STANDARD_SPINNERS &
                                      HAS_STANDARD_BUMPERS),
                                      (HAS_STANDARD_LAUNCHERS),
                                      (HAS_STANDARD_LAUNCHERS),
                                      (HAS_STANDARD_LAUNCHERS)],
    "Verticality Checkpoint 1": [(HAS_STANDARD_BLOCK_LAUNCHERS),
                                 (HAS_STANDARD_BLOCK_LAUNCHERS),
                                 (HAS_STANDARD_BLOCK_LAUNCHERS),
                                 (HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Verticality Coin 2": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS)],
    "Verticality Room 2 Door": [(HAS_STANDARD_LAUNCHERS & HAS_STANDARD_SPINNERS &
                                 HAS_STANDARD_BUMPERS),
                                (HAS_STANDARD_LAUNCHERS),
                                (HAS_STANDARD_LAUNCHERS),
                                (HAS_STANDARD_LAUNCHERS)],
    "Verticality Room 3 Door": [(HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS &
                                 HAS_STANDARD_PHYSICS_BLOCKS & HAS_STANDARD_BUMPERS &
                                 HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS &
                                 HAS_STANDARD_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS),
                                (HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS &
                                 HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                 HAS_STANDARD_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS),
                                (HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS & (
                                 HAS_STANDARD_PHYSICS_BLOCKS | (HAS_STANDARD_BUMPERS & 
                                 HAS_STANDARD_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS))),
                                (HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS & (
                                 HAS_STANDARD_PHYSICS_BLOCKS | (HAS_STANDARD_BUMPERS & 
                                 HAS_STANDARD_LAUNCHERS)))],
    "Verticality Coin 3": [(HAS_STANDARD_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                            HAS_STANDARD_LAUNCHERS & HAS_STANDARD_BUMPERS & 
                            HAS_STANDARD_SPINNERS),
                           (HAS_STANDARD_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                            HAS_STANDARD_LAUNCHERS & HAS_STANDARD_BUMPERS & 
                            HAS_STANDARD_SPINNERS),
                           (HAS_STANDARD_VIVI_BLOCKS & (HAS_STANDARD_BLOCK_LAUNCHERS | (
                            HAS_STANDARD_LAUNCHERS & HAS_STANDARD_BUMPERS))),
                           (HAS_STANDARD_VIVI_BLOCKS)],
    "Verticality Level Clear": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS &
                                 HAS_STANDARD_BUMPERS & HAS_STANDARD_SPINNERS & 
                                 HAS_STANDARD_VIVI_BLOCKS),
                                (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS & (
                                 HAS_STANDARD_VIVI_BLOCKS | (HAS_STANDARD_LAUNCHERS &
                                 HAS_STANDARD_BUMPERS))),
                                (HAS_STANDARD_BLOCK_LAUNCHERS | (HAS_STANDARD_LAUNCHERS & 
                                HAS_STANDARD_BUMPERS)),
                                None],
    #Catch A Ride
    "Catch A Ride Room 1 Door": [(HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS)],
    "Catch A Ride Coin 1": [(HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS)],
    "Catch A Ride Room 2 Door": [(HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS)],
    "Catch A Ride Coin 2": [(HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS),
                            (HAS_STANDARD_SLIDING_BLOCKS)],
    "Catch A Ride Checkpoint 1": [(HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS & 
                                   HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                                   HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                                   HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                                  (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                                   HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS)],
    "Catch A Ride Coin 3": [(HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS & 
                             HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS &
                             HAS_STANDARD_BLOCK_LAUNCHERS),
                            (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                             HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS &
                             HAS_STANDARD_BLOCK_LAUNCHERS),
                            (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                             HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                            (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                             HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS)],
    "Catch A Ride Room 3 Door": [(HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                                  HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS &
                                  HAS_STANDARD_BLOCK_LAUNCHERS),
                                 (HAS_SMASH_BLOCKS & HAS_STANDARD_SLIDING_BLOCKS &
                                  HAS_ON_OFF_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                                 (HAS_SMASH_BLOCKS & (HAS_ON_OFF_BLOCKS |
                                  HAS_STANDARD_SLIDING_BLOCKS)),
                                 (HAS_SMASH_BLOCKS)],
    "Catch A Ride Level Clear": [(HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SLIDING_BLOCKS)],
    #Chaos Cavern
    "Chaos Cavern Room 1 Door": [(HAS_STANDARD_BUMPERS & HAS_STANDARD_SPINNERS &
                                  HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS & 
                                  HAS_ON_OFF_BLOCKS),
                                 (HAS_STANDARD_BUMPERS & HAS_STANDARD_SPINNERS &
                                  HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS & 
                                  HAS_ON_OFF_BLOCKS),
                                 (HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS & (
                                  HAS_STANDARD_BLOCK_LAUNCHERS | ( HAS_STANDARD_SPINNERS &
                                  HAS_STANDARD_LAUNCHERS))),
                                 (HAS_ON_OFF_BLOCKS & (HAS_STANDARD_LAUNCHERS | 
                                  HAS_STANDARD_BLOCK_LAUNCHERS | (HAS_STANDARD_BUMPERS & 
                                  HAS_STANDARD_SPINNERS)))],
    "Chaos Cavern Room 2 Door": [(HAS_STANDARD_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                  HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                  HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SLIDING_BLOCKS),
                                 (HAS_STANDARD_SPINNERS | (HAS_STANDARD_BLOCK_LAUNCHERS & 
                                  HAS_STANDARD_SLIDING_BLOCKS))],
    "Chaos Cavern Coin 1": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_VIVI_BLOCKS &
                             HAS_STANDARD_SPINNERS & HAS_SMASH_BLOCKS &
                             HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_KEY_BLOCKS),
                            (HAS_ON_OFF_BLOCKS & HAS_STANDARD_VIVI_BLOCKS &
                             HAS_STANDARD_SPINNERS),
                            (HAS_ON_OFF_BLOCKS & HAS_STANDARD_VIVI_BLOCKS),
                            None],
    "Chaos Cavern Level Clear": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_VIVI_BLOCKS &
                                  HAS_STANDARD_SPINNERS & HAS_SMASH_BLOCKS &
                                  HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_KEY_BLOCKS),
                                 (HAS_ON_OFF_BLOCKS),
                                 (HAS_ON_OFF_BLOCKS),
                                 None],
    #Holding On
    "Holding On Checkpoint 1": [(HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                 HAS_STANDARD_SPINNERS),
                                (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                 HAS_STANDARD_SPINNERS),
                                (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                 HAS_STANDARD_SPINNERS),
                                (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                 HAS_STANDARD_SPINNERS)],
    "Holding On Room 1 Door": [(HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_SPINNERS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_SPINNERS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_SPINNERS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_ON_OFF_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_SPINNERS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS)],
    "Holding On Checkpoint 2": [(HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                 HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                 HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                 HAS_STANDARD_BLOCK_LAUNCHERS),
                                (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Holding On Room 2 Door": [(HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS & 
                                HAS_SMASH_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS & 
                                HAS_SMASH_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS &
                                HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS & 
                                HAS_SMASH_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                HAS_SMASH_BLOCKS)],
    "Holding On Room 3 Door": [(HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_SPINNERS & HAS_GUBES &
                                HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_GUBES & HAS_STANDARD_BUMPERS & 
                                HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_SMASH_BLOCKS &
                                HAS_STANDARD_BUMPERS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_SMASH_BLOCKS)],
    "Holding On Coin 1": [(HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                          (HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                          (HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                          (HAS_STANDARD_PUNCHAPPEAR_BLOCKS)],
    "Holding On Level Clear": [(HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                               (HAS_STANDARD_PUNCHAPPEAR_BLOCKS)],
    #Fist Fight
    "Fist Fight Room 1 Door": [(HAS_STAR_SPINNERS & HAS_STANDARD_SPINNERS),
                               (HAS_STAR_SPINNERS),
                               (HAS_STAR_SPINNERS),
                               (HAS_STAR_SPINNERS)],
    "Fist Fight Room 2 Door": [(HAS_STAR_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS & 
                                HAS_STANDARD_LAUNCHERS & HAS_STANDARD_SLIDING_BLOCKS),
                               (HAS_STAR_SPINNERS & HAS_STANDARD_BLOCK_LAUNCHERS & 
                                HAS_STANDARD_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS),
                               (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_LAUNCHERS)],
    "Fist Fight Room 3 Door": [(HAS_STANDARD_VIVI_BLOCKS & HAS_STANDARD_SPINNERS),
                               (HAS_STANDARD_VIVI_BLOCKS & HAS_STANDARD_SPINNERS),
                               (HAS_STANDARD_VIVI_BLOCKS),
                               (HAS_STANDARD_VIVI_BLOCKS)],
    "Fist Fight Room 4 Door": [(HAS_WING_BLOCK_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS & 
                                HAS_ON_OFF_BLOCKS & HAS_STAR_SPINNERS),
                               (HAS_WING_BLOCK_LAUNCHERS & HAS_STANDARD_VIVI_BLOCKS),
                               (HAS_STANDARD_VIVI_BLOCKS),
                               (HAS_STANDARD_VIVI_BLOCKS | HAS_ON_OFF_BLOCKS)],
    "Fist Fight Room 5 Door": [(HAS_STAR_SPINNERS & HAS_STANDARD_STAR_BLOCKS & 
                                HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STAR_SPINNERS & HAS_STANDARD_STAR_BLOCKS &
                                HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STAR_SPINNERS & HAS_STANDARD_STAR_BLOCKS),
                               (HAS_STAR_SPINNERS & HAS_STANDARD_STAR_BLOCKS)],
    "Fist Fight Heart 1": [(HAS_STANDARD_STAR_BLOCKS),
                           (HAS_STANDARD_STAR_BLOCKS),
                           (HAS_STANDARD_STAR_BLOCKS),
                           (HAS_STANDARD_STAR_BLOCKS)],
    "Fist Fight Heart 2": [(HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS)],
    "Fist Fight Heart 3": [(HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS)],
    "Fist Fight Level Clear": [(HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_STAR_BLOCKS & HAS_WING_BLOCK_LAUNCHERS)],
    #Depths
    "Depths Room 1 Door": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_SMASH_BLOCKS & 
                            HAS_DOWN_WATER & HAS_STANDARD_SPINNERS & 
                            HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS),
                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_SMASH_BLOCKS & 
                            HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS),
                           (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_SMASH_BLOCKS & 
                            HAS_STANDARD_KEY_BLOCKS & HAS_ON_OFF_BLOCKS),
                           (HAS_ON_OFF_BLOCKS)],
    "Depths Room 2 Door": [(HAS_STANDARD_BUMPERS & HAS_STANDARD_LAUNCHERS &
                            HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_BUMPERS & HAS_STANDARD_LAUNCHERS &
                            HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                           (HAS_STANDARD_BUMPERS & HAS_STANDARD_LAUNCHERS &
                            HAS_ON_OFF_BLOCKS),
                           (HAS_STANDARD_BUMPERS & HAS_STANDARD_LAUNCHERS &
                            HAS_ON_OFF_BLOCKS)],
    "Depths Level Clear": [(HAS_STANDARD_SLIDING_BLOCKS & HAS_ON_OFF_BLOCKS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_SLIDING_BLOCKS & HAS_ON_OFF_BLOCKS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_SLIDING_BLOCKS & HAS_ON_OFF_BLOCKS & HAS_STANDARD_LAUNCHERS),
                           (HAS_STANDARD_SLIDING_BLOCKS & HAS_ON_OFF_BLOCKS & HAS_STANDARD_LAUNCHERS)],
    #Cliff Warning
    "Cliff Warning Room 1 Door": [(HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Cliff Warning Checkpoint 1": [(HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_STANDARD_BUMPERS),
                                   (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_STANDARD_BUMPERS),
                                   (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_STANDARD_BUMPERS),
                                   (HAS_TIMER_BUTTONS & (HAS_STANDARD_BLOCK_LAUNCHERS |
                                    HAS_STANDARD_BUMPERS))],
    "Cliff Warning Coin 1": [(HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                              HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                              HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                             (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                              HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                              HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                             (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                              HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                              HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                             (HAS_TIMER_BUTTONS & HAS_ON_OFF_BLOCKS &
                              HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS & (
                              HAS_STANDARD_BLOCK_LAUNCHERS | HAS_STANDARD_BUMPERS))],
    "Cliff Warning Level Clear": [(HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                                   HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                                  (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                                   HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                                  (HAS_TIMER_BUTTONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_BUMPERS & HAS_ON_OFF_BLOCKS &
                                   HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS),
                                  (HAS_TIMER_BUTTONS & HAS_ON_OFF_BLOCKS &
                                   HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_LAUNCHERS & (
                                   HAS_STANDARD_BLOCK_LAUNCHERS | HAS_STANDARD_BUMPERS))],
    #The Library
    "The Library Tutorial Panel 1": [(HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS)],
    "The Library Tutorial Panel 2": [(HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS)],
    "The Library Tutorial Panel 3": [(HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS),
                                     (HAS_TIMER_BUTTONS)],
    "The Library Room 1 Side Door 1": [(HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS)],
    "The Library Room 1 Side Door 2": [(HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS)],
    "The Library Room 1 Side Door 3": [(HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS)],
    "The Library Coin 1": [(HAS_STANDARD_PHYSICS_BLOCKS),
                           (HAS_STANDARD_PHYSICS_BLOCKS),
                           (HAS_STANDARD_PHYSICS_BLOCKS),
                           (HAS_STANDARD_PHYSICS_BLOCKS)],
    "The Library Coin 2": [(HAS_TIMER_BUTTONS),
                           (HAS_TIMER_BUTTONS),
                           (HAS_TIMER_BUTTONS),
                           (HAS_TIMER_BUTTONS)],
    "The Library Level Clear": [(HAS_TIMER_BUTTONS),
                                (HAS_TIMER_BUTTONS),
                                (HAS_TIMER_BUTTONS),
                                (HAS_TIMER_BUTTONS)],
    #Midnight Grove
    "Midnight Grove Coin 1": [(HAS_BLUE_PEARL_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS)],
    "Midnight Grove Room 1 Door": [(HAS_BLUE_PEARL_LAUNCHERS),
                                   (HAS_BLUE_PEARL_LAUNCHERS),
                                   (HAS_BLUE_PEARL_LAUNCHERS),
                                   (HAS_BLUE_PEARL_LAUNCHERS)],
    "Midnight Grove Coin 2": [(HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                              (HAS_BLUE_PEARL_LAUNCHERS | HAS_PEARL_BLOCK_LAUNCHERS)],
    "Midnight Grove Room 2 Door": [(HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                   (HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                   (HAS_BLUE_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                   (HAS_PEARL_BLOCK_LAUNCHERS)],
    "Midnight Grove Checkpoint 1": [(HAS_RED_PEARL_LAUNCHERS),
                                    (HAS_RED_PEARL_LAUNCHERS),
                                    (HAS_RED_PEARL_LAUNCHERS),
                                    (HAS_RED_PEARL_LAUNCHERS)],
    "Midnight Grove Coin 3": [(HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS),
                              (HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS),
                              (HAS_RED_PEARL_LAUNCHERS & (HAS_BLUE_PEARL_LAUNCHERS |
                               HAS_RED_FIRE_RINGS)),
                              (HAS_RED_PEARL_LAUNCHERS & (HAS_BLUE_PEARL_LAUNCHERS |
                               HAS_RED_FIRE_RINGS))],
    "Midnight Grove Room 3 Door": [(HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                                    HAS_RED_FIRE_RINGS),
                                   (HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                                    HAS_RED_FIRE_RINGS),
                                   (HAS_RED_PEARL_LAUNCHERS & HAS_RED_FIRE_RINGS),
                                   (HAS_RED_PEARL_LAUNCHERS & HAS_RED_FIRE_RINGS)],
    "Midnight Grove Checkpoint 2": [(HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                     HAS_ARROW_LIFTS),
                                    (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                     HAS_ARROW_LIFTS),
                                    (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS),
                                    (HAS_RED_FIRE_RINGS & (HAS_BLUE_PEARL_LAUNCHERS |
                                     HAS_ARROW_LIFTS))],
    "Midnight Grove Load Bearing Collectible": [(HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                                 HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                                 HAS_LEAD_BALLOONS),
                                                (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                                 HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                                 HAS_LEAD_BALLOONS),
                                                (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                                 HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                                 HAS_LEAD_BALLOONS),
                                                (HAS_RED_FIRE_RINGS & HAS_ARROW_LIFTS &
                                                 HAS_BOMB_FLOWERS)],
    "Midnight Grove Level Clear": [(HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                    HAS_ARROW_LIFTS),
                                   (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                    HAS_ARROW_LIFTS),
                                   (HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS &
                                    HAS_ARROW_LIFTS),
                                   (HAS_RED_FIRE_RINGS & HAS_ARROW_LIFTS)],
    #Briarbrush Woods
    "Briarbrush Woods Room 1 Door": [(HAS_TOGGLE_FLOWERS),
                                     (HAS_TOGGLE_FLOWERS),
                                     (HAS_TOGGLE_FLOWERS),
                                     (HAS_TOGGLE_FLOWERS)],
    "Briarbrush Woods Coin 1": [(HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                (HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                (HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                (HAS_TOGGLE_FLOWERS)],
    "Briarbrush Woods Room 2 Door": [(HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS &
                                      HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS),
                                     (HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS &
                                      HAS_RED_FIRE_RINGS & HAS_BLUE_PEARL_LAUNCHERS),
                                     (HAS_TOGGLE_FLOWERS & HAS_RED_FIRE_RINGS &
                                      HAS_BLUE_PEARL_LAUNCHERS),
                                     (HAS_TOGGLE_FLOWERS & HAS_RED_FIRE_RINGS & 
                                      HAS_BLUE_PEARL_LAUNCHERS)],
    "Briarbrush Woods Room 3 Door": [(HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS),
                                     (HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS),
                                     (HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS),
                                     (HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS)],
    "Briarbrush Woods Level Clear": [(HAS_TOGGLE_FLOWERS & HAS_GREEN_BUBBLES),
                                     (HAS_TOGGLE_FLOWERS),
                                     (HAS_TOGGLE_FLOWERS),
                                     (HAS_TOGGLE_FLOWERS)],
    #Various Explosives
    "Various Explosives Coin 1": [(HAS_RED_BALLOONS & HAS_LEAD_BALLOONS &
                                   HAS_BOMB_FLOWERS),
                                  (HAS_RED_BALLOONS & HAS_LEAD_BALLOONS &
                                   HAS_BOMB_FLOWERS),
                                  (HAS_RED_BALLOONS & HAS_BOMB_FLOWERS),
                                  (HAS_BOMB_FLOWERS)],
    "Various Explosives Room 1 Door": [(HAS_RED_BALLOONS & HAS_LEAD_BALLOONS &
                                        HAS_BOMB_FLOWERS),
                                       (HAS_RED_BALLOONS & HAS_LEAD_BALLOONS &
                                        HAS_BOMB_FLOWERS),
                                       (HAS_RED_BALLOONS & HAS_BOMB_FLOWERS),
                                       (HAS_BOMB_FLOWERS)],
    "Various Explosives Coin 2": [(HAS_BOMB_FLOWERS),
                                  (HAS_BOMB_FLOWERS),
                                  (HAS_BOMB_FLOWERS),
                                  (HAS_BOMB_FLOWERS)],
    "Various Explosives Room 2 Door": [(HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                                        HAS_LEAD_BALLOONS & HAS_RED_BALLOONS),
                                       (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                                        HAS_RED_BALLOONS),
                                       (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS),
                                       (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS)],
    "Various Explosives Coin 3": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                   HAS_TOGGLE_BALLOONS & HAS_LEAD_BALLOONS),
                                  (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                   HAS_TOGGLE_BALLOONS),
                                  (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                   HAS_TOGGLE_BALLOONS),
                                  (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                   HAS_TOGGLE_BALLOONS)],
    "Various Explosives Level Clear": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                        HAS_TOGGLE_BALLOONS & HAS_LEAD_BALLOONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                        HAS_TOGGLE_BALLOONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                        HAS_TOGGLE_BALLOONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BOMB_FLOWERS &
                                        HAS_TOGGLE_BALLOONS)],
    #Together By Tether
    "Together By Tether Room 1 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_BLUE_PEARL_LAUNCHERS & HAS_BOMB_FLOWERS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_BOMB_FLOWERS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_BOMB_FLOWERS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_BOMB_FLOWERS)],
    "Together By Tether Coin 1": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_BLUE_PEARL_LAUNCHERS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Together By Tether Coin 2": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_BLUE_PEARL_LAUNCHERS & HAS_GREEN_BUBBLES & 
                                   HAS_LEAD_BALLOONS & HAS_RED_BALLOONS &
                                   HAS_RED_FIRE_RINGS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_GREEN_BUBBLES),
                                  (HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Together By Tether Room 2 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_BLUE_PEARL_LAUNCHERS & HAS_GREEN_BUBBLES &
                                        HAS_RED_FIRE_RINGS & HAS_LEAD_BALLOONS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_RED_FIRE_RINGS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_RED_FIRE_RINGS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Together By Tether Coin 3": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                   HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS)],
    "Together By Tether Room 3 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_TOGGLE_FLOWERS & HAS_PEARL_BLOCK_LAUNCHERS)],
    "Together By Tether Level Clear": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                        HAS_LEAD_BALLOONS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS)],
    #Pop Unlock
    "Pop Unlock Room 1 Door": [(HAS_GREEN_BUBBLES & HAS_KEY_BUBBLES),
                               (HAS_GREEN_BUBBLES & HAS_KEY_BUBBLES),
                               (HAS_GREEN_BUBBLES & HAS_KEY_BUBBLES),
                               (HAS_GREEN_BUBBLES & HAS_KEY_BUBBLES)],
    "Pop Unlock Coin 1": [(HAS_KEY_BUBBLES & HAS_DIRECTIONAL_BUMPERS &
                           HAS_RED_BALLOONS & HAS_RED_FIRE_RINGS & 
                           HAS_GREEN_BUBBLES & HAS_LEAD_BALLOONS),
                          (HAS_KEY_BUBBLES & HAS_DIRECTIONAL_BUMPERS & (
                           HAS_RED_FIRE_RINGS | HAS_RED_BALLOONS)),
                          (HAS_KEY_BUBBLES & (HAS_RED_BALLOONS | (
                           HAS_DIRECTIONAL_BUMPERS & HAS_RED_FIRE_RINGS))),
                          (HAS_KEY_BUBBLES & (HAS_RED_BALLOONS |
                           HAS_DIRECTIONAL_BUMPERS))],
    "Pop Unlock Room 2 Door": [(HAS_GREEN_BUBBLES & HAS_KEY_BUBBLES &
                                HAS_DIRECTIONAL_BUMPERS & HAS_RED_BALLOONS &
                                HAS_RED_FIRE_RINGS & HAS_LEAD_BALLOONS),
                               (HAS_KEY_BUBBLES & HAS_DIRECTIONAL_BUMPERS & 
                                HAS_RED_FIRE_RINGS & HAS_GREEN_BUBBLES),
                               (HAS_KEY_BUBBLES & (HAS_RED_BALLOONS | (
                                HAS_RED_FIRE_RINGS & (HAS_LEAD_BALLOONS | 
                                HAS_GREEN_BUBBLES)))),
                               (HAS_KEY_BUBBLES & (HAS_RED_BALLOONS | (
                                (HAS_RED_FIRE_RINGS | HAS_DIRECTIONAL_BUMPERS) & (
                                HAS_LEAD_BALLOONS | HAS_GREEN_BUBBLES))))],
    "Pop Unlock Coin 2": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                           HAS_KEY_BUBBLES & HAS_RED_BALLOONS &
                           HAS_PEARL_BLOCK_LAUNCHERS & HAS_TOGGLE_FLOWERS),
                          (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                           HAS_KEY_BUBBLES & HAS_PEARL_BLOCK_LAUNCHERS),
                          (HAS_STANDARD_PHYSICS_BLOCKS & HAS_KEY_BUBBLES & (
                           HAS_TETHERS | HAS_PEARL_BLOCK_LAUNCHERS)),
                          (HAS_STANDARD_PHYSICS_BLOCKS & HAS_KEY_BUBBLES & (
                           HAS_TETHERS | HAS_PEARL_BLOCK_LAUNCHERS))],
    "Pop Unlock Level Clear": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                HAS_KEY_BUBBLES & HAS_RED_BALLOONS &
                                HAS_PEARL_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_PHYSICS_BLOCKS & HAS_TETHERS &
                                HAS_KEY_BUBBLES & HAS_PEARL_BLOCK_LAUNCHERS),
                               (HAS_STANDARD_PHYSICS_BLOCKS & HAS_KEY_BUBBLES),
                               (HAS_STANDARD_PHYSICS_BLOCKS & HAS_KEY_BUBBLES)],
    #The Gatekeeper
    "The Gatekeeper Room 1 Door": [(HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS)],
    "The Gatekeeper Room 2 Door": [(HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS &
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS &
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS &
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS &
                                    HAS_BURNABLE_BLOCKS)],
    "The Gatekeeper Coin 1": [(HAS_ARROW_LIFTS),
                              (HAS_ARROW_LIFTS),
                              (HAS_ARROW_LIFTS),
                              (HAS_ARROW_LIFTS)],
    "The Gatekeeper Coin 2": [(HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS & 
                               HAS_RED_BALLOONS),
                              (HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS & 
                               HAS_RED_BALLOONS),
                              (HAS_GREEN_BUBBLES & (HAS_RED_PEARL_LAUNCHERS |
                               HAS_RED_BALLOONS)),
                              (HAS_GREEN_BUBBLES & (HAS_RED_PEARL_LAUNCHERS |
                               HAS_RED_BALLOONS))],
    "The Gatekeeper Room 3 Door": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES & 
                                    HAS_STANDARD_STAR_BLOCKS & HAS_RED_PEARL_LAUNCHERS & 
                                    HAS_RED_BALLOONS & HAS_ARROW_LIFTS & 
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES & 
                                    HAS_STANDARD_STAR_BLOCKS & HAS_RED_PEARL_LAUNCHERS & 
                                    HAS_RED_BALLOONS & HAS_ARROW_LIFTS & 
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS & HAS_ARROW_LIFTS &
                                    HAS_BURNABLE_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS & HAS_ARROW_LIFTS &
                                    HAS_BURNABLE_BLOCKS)],
    "The Gatekeeper Coin 3": [(HAS_RED_PEARL_LAUNCHERS & HAS_TOGGLE_FLOWERS &
                               HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS &
                               HAS_LEAD_BALLOONS & HAS_RED_BALLOONS),
                              (HAS_RED_PEARL_LAUNCHERS & HAS_TOGGLE_FLOWERS &
                               HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS &
                               HAS_RED_BALLOONS),
                              (HAS_RED_PEARL_LAUNCHERS & HAS_TOGGLE_FLOWERS &
                               HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS),
                              (HAS_TOGGLE_FLOWERS & HAS_GREEN_BUBBLES &
                               HAS_RED_FIRE_RINGS)],
    "The Gatekeeper Room 4 Door": [(HAS_RED_PEARL_LAUNCHERS & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS & HAS_LEAD_BALLOONS &
                                    HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS &
                                    HAS_RED_BALLOONS & HAS_TOGGLE_FLOWERS),
                                   (HAS_RED_PEARL_LAUNCHERS & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS & HAS_GREEN_BUBBLES &
                                    HAS_RED_FIRE_RINGS & HAS_RED_BALLOONS &
                                    HAS_TOGGLE_FLOWERS),
                                   (HAS_RED_PEARL_LAUNCHERS & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS & HAS_GREEN_BUBBLES &
                                    HAS_RED_FIRE_RINGS & HAS_TOGGLE_FLOWERS),
                                   (HAS_NUMBER_BUBBLES & HAS_STANDARD_STAR_BLOCKS &
                                    HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS & 
                                    HAS_TOGGLE_FLOWERS)],
    "The Gatekeeper Heart 1": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS)],
    "The Gatekeeper Heart 2": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS)],
    "The Gatekeeper Heart 3": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS)],
    "The Gatekeeper Heart 4": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS),
                               (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                HAS_STANDARD_STAR_BLOCKS)],
    "The Gatekeeper Level Clear": [(HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS),
                                   (HAS_GREEN_BUBBLES & HAS_NUMBER_BUBBLES &
                                    HAS_STANDARD_STAR_BLOCKS)],
    #The Elevator
    "The Elevator Room 1 Door": [(HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS)],
    "The Elevator Room 2 Door": [(HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS),
                                 (HAS_ARROW_LIFTS)],
    "The Elevator Coin 1": [(HAS_ARROW_LIFTS),
                            (HAS_ARROW_LIFTS),
                            None,
                            None],
    "The Elevator Level Clear": [(HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                  HAS_RED_FIRE_RINGS & HAS_RED_BALLOONS),
                                 (HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                  HAS_RED_FIRE_RINGS),
                                 (HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                  HAS_RED_FIRE_RINGS),
                                 (HAS_ARROW_LIFTS & HAS_BOMB_FLOWERS &
                                  HAS_RED_FIRE_RINGS)],
    #Frostbite
    "Frostbite Room 1 Door": [(HAS_ICE_KEY_BLOCKS & HAS_ICE_BLOCKS &
                               HAS_ICICLES),
                              (HAS_ICE_KEY_BLOCKS & HAS_ICE_BLOCKS),
                              (HAS_ICE_KEY_BLOCKS & HAS_ICE_BLOCKS),
                              (HAS_ICE_KEY_BLOCKS & HAS_ICE_BLOCKS)],
    "Frostbite Room 2 Door": [(HAS_ICE_KEY_BLOCKS & HAS_ICICLES &
                               HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                               HAS_ICE_BLOCKS),
                              (HAS_ICE_KEY_BLOCKS & HAS_ICICLES &
                               HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS),
                              (HAS_ICE_KEY_BLOCKS & HAS_ICICLES &
                               HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS),
                              (HAS_ICE_KEY_BLOCKS & HAS_BOMB_FLOWERS &
                               HAS_TOGGLE_BALLOONS & (HAS_ICE_BLOCKS |
                               HAS_ICICLES))],
    "Frostbite Coin 1": [(HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                          HAS_LEAD_BALLOONS),
                         (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS),
                         (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS),
                         (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS)],
    "Frostbite Room 3 Door": [(HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                               HAS_ICE_KEY_BLOCKS & HAS_ICICLES &
                               HAS_LEAD_BALLOONS),
                              (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                               HAS_ICE_KEY_BLOCKS & HAS_ICICLES),
                              (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                               HAS_ICE_KEY_BLOCKS & HAS_ICICLES),
                              (HAS_BOMB_FLOWERS & HAS_TOGGLE_BALLOONS &
                               HAS_ICE_KEY_BLOCKS & HAS_ICICLES)],
    "Frostbite Checkpoint 1": [(HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS &
                                HAS_ICICLES),
                               (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS),
                               (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS),
                               (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS)],
    "Frostbite Level Clear": [(HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS &
                               HAS_ICICLES & HAS_ICE_KEY_BLOCKS &
                               HAS_RED_PEARL_LAUNCHERS),
                              (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS &
                               HAS_ICE_KEY_BLOCKS & HAS_RED_PEARL_LAUNCHERS),
                              (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS & 
                               HAS_ICE_KEY_BLOCKS),
                              (HAS_ICE_BLOCK_LAUNCHERS & HAS_ICE_BLOCKS)],
    #Forgotten Archives
    "Forgotten Archives Room 1 Door": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_KEY_QUARTETS &
                                        HAS_TIMER_BUTTONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_KEY_QUARTETS &
                                        HAS_TIMER_BUTTONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_KEY_QUARTETS &
                                        HAS_TIMER_BUTTONS),
                                       (HAS_PEARL_BLOCK_LAUNCHERS & HAS_KEY_QUARTETS &
                                        HAS_TIMER_BUTTONS)],
    "Forgotten Archives Checkpoint 1": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS)],
    "Forgotten Archives Room 2 Door": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS)],
    "Forgotten Archives Coin 1": [(HAS_TIMER_BUTTONS & HAS_GREEN_BUBBLES),
                                  (HAS_TIMER_BUTTONS),
                                  (HAS_TIMER_BUTTONS),
                                  (HAS_TIMER_BUTTONS)],
    "Forgotten Archives Room 3 Door": [(HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS)],
    "Forgotten Archives Load Bearing Collectible": [(HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                                     HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS &
                                                     HAS_LEAD_BALLOONS & HAS_RED_FIRE_RINGS &
                                                     HAS_RED_BALLOONS),
                                                    (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                                     HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS &
                                                     HAS_RED_FIRE_RINGS & HAS_RED_BALLOONS),
                                                    (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                                     HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS &
                                                     HAS_RED_FIRE_RINGS & HAS_RED_BALLOONS),
                                                    (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                                     HAS_GREEN_BUBBLES & HAS_RED_PEARL_LAUNCHERS &
                                                     HAS_RED_FIRE_RINGS & HAS_RED_BALLOONS)],
    "Forgotten Archives Room 4 Door": [(HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                        HAS_GREEN_BUBBLES & HAS_RED_FIRE_RINGS & 
                                        HAS_DIRECTIONAL_BUMPERS),
                                       (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                        HAS_RED_FIRE_RINGS & HAS_DIRECTIONAL_BUMPERS),
                                       (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                        HAS_RED_FIRE_RINGS & HAS_DIRECTIONAL_BUMPERS),
                                       (HAS_TIMER_BUTTONS & HAS_KEY_BUBBLES &
                                        HAS_RED_FIRE_RINGS & HAS_DIRECTIONAL_BUMPERS)],
    "Forgotten Archives Checkpoint 2": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS)],
    "Forgotten Archives Checkpoint 3": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                        (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS)],
    "Forgotten Archives Coin 2": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                   HAS_RED_BALLOONS),
                                  (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                   HAS_RED_BALLOONS),
                                  (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS),
                                  (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS)],
    "Forgotten Archives Level Clear": [(HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS & HAS_RED_FIRE_RINGS &
                                        HAS_LEAD_BALLOONS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS & HAS_RED_FIRE_RINGS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS & HAS_RED_FIRE_RINGS),
                                       (HAS_GREEN_BUBBLES & HAS_TIMER_BUTTONS &
                                        HAS_KEY_QUARTETS & HAS_RED_FIRE_RINGS)],
    #The Scenic Route
    "The Scenic Route Room 1 Door": [(HAS_RED_BALLOONS & HAS_SNAKE_BLOCKS &
                                      HAS_RED_FIRE_RINGS & HAS_GREEN_BUBBLES &
                                      HAS_LEAD_BALLOONS & HAS_BOMB_FLOWERS),
                                     (HAS_RED_BALLOONS & HAS_SNAKE_BLOCKS &
                                      HAS_RED_FIRE_RINGS & HAS_GREEN_BUBBLES &
                                      HAS_LEAD_BALLOONS & HAS_BOMB_FLOWERS),
                                     (HAS_RED_BALLOONS & HAS_SNAKE_BLOCKS &
                                      HAS_RED_FIRE_RINGS),
                                     (HAS_RED_BALLOONS & HAS_SNAKE_BLOCKS &
                                      HAS_RED_FIRE_RINGS)],
    "The Scenic Route Checkpoint 1": [(HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                       HAS_PEARL_BLOCK_LAUNCHERS & HAS_RED_BALLOONS),
                                      (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                       HAS_PEARL_BLOCK_LAUNCHERS),
                                      (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                       HAS_PEARL_BLOCK_LAUNCHERS),
                                      (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS)],
    "The Scenic Route Room 2 Door": [(HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                      HAS_PEARL_BLOCK_LAUNCHERS & HAS_RED_BALLOONS &
                                      HAS_ARROW_LIFTS & HAS_GREEN_BUBBLES),
                                     (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                      HAS_PEARL_BLOCK_LAUNCHERS & HAS_ARROW_LIFTS & 
                                      HAS_GREEN_BUBBLES),
                                     (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                      HAS_PEARL_BLOCK_LAUNCHERS & HAS_ARROW_LIFTS &
                                      HAS_GREEN_BUBBLES),
                                     (HAS_BLUE_FIRE_RINGS & HAS_SNAKE_BLOCKS &
                                      HAS_ARROW_LIFTS & HAS_GREEN_BUBBLES)],
    "The Scenic Route Room 3 Door": [(HAS_BLUE_FIRE_RINGS & HAS_RED_PEARL_LAUNCHERS &
                                      HAS_BOMB_FLOWERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_RED_PEARL_LAUNCHERS &
                                      HAS_BOMB_FLOWERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_RED_PEARL_LAUNCHERS &
                                      HAS_BOMB_FLOWERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_RED_PEARL_LAUNCHERS &
                                      HAS_BOMB_FLOWERS)],
    "The Scenic Route Room 4 Door": [(HAS_BLUE_FIRE_RINGS & HAS_STANDARD_PHYSICS_BLOCKS &
                                      HAS_TETHERS & HAS_LEAD_BALLOONS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_STANDARD_PHYSICS_BLOCKS &
                                      HAS_TETHERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_STANDARD_PHYSICS_BLOCKS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_STANDARD_PHYSICS_BLOCKS)],
    "The Scenic Route Room 5 Door": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                      HAS_YELLOW_BLOCK_LAUNCHERS),
                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                      HAS_YELLOW_BLOCK_LAUNCHERS),
                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                      HAS_YELLOW_BLOCK_LAUNCHERS),
                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "The Scenic Route Room 6 Door": [(HAS_BLUE_FIRE_RINGS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_SWITCHES & 
                                      HAS_STANDARD_POP_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_SWITCHES &
                                      HAS_STANDARD_POP_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS),
                                     (HAS_BLUE_FIRE_RINGS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_SWITCHES &
                                      HAS_STANDARD_POP_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS),
                                     (HAS_BLUE_FIRE_RINGS & (HAS_STANDARD_POP_BLOCKS | (
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_SWITCHES)) &
                                      HAS_BLUE_CRYSTAL_LAUNCHERS)],
    "The Scenic Route Coin 1": [(HAS_YELLOW_SKULL_RINGS),
                                None,
                                None,
                                None],
    "The Scenic Route Level Clear": [HAS_YELLOW_SKULL_RINGS,
                                     None,
                                     None,
                                     None],
    #The Timeless Temple
    "The Timeless Temple Room 1 Door": [(HAS_YELLOW_PHYSICS_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                        (HAS_YELLOW_PHYSICS_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                        (HAS_YELLOW_PHYSICS_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "The Timeless Temple Room 2 Door": [(HAS_YELLOW_SKULL_RINGS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS & 
                                         HAS_YELLOW_SKULL_BLOCKS),
                                        (HAS_YELLOW_SKULL_RINGS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "The Timeless Temple Coin 1": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                    HAS_YELLOW_SKULL_RINGS),
                                   (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                   (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                   (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "The Timeless Temple Load Bearing Collectible": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                                      HAS_YELLOW_SKULL_RINGS & HAS_YELLOW_VIVI_BLOCKS),
                                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                                      HAS_YELLOW_VIVI_BLOCKS),
                                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                                      HAS_YELLOW_VIVI_BLOCKS),
                                                     (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_VIVI_BLOCKS)],
    "The Timeless Temple Level Clear": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS & 
                                         HAS_YELLOW_SKULL_RINGS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                        (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    #Haunted Halls
    "Haunted Halls Room 1 Door": [(HAS_YELLOW_GORBS & HAS_YELLOW_PHYSICS_BLOCKS &
                                   HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_RINGS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_GORBS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "Haunted Halls Coin 1": [(HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                              HAS_YELLOW_GORBS & HAS_YELLOW_SKULL_BLOCKS),
                             (HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                              HAS_YELLOW_GORBS & HAS_YELLOW_SKULL_BLOCKS),
                             (HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                             (HAS_YELLOW_SLIDING_BLOCKS)],
    "Haunted Halls Room 2 Door": [(HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS & 
                                   HAS_YELLOW_SKULL_BLOCKS & HAS_YELLOW_GORBS),
                                  (HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS & 
                                   HAS_YELLOW_SKULL_BLOCKS & HAS_YELLOW_GORBS),
                                  (HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS & 
                                   HAS_YELLOW_SKULL_BLOCKS),
                                  (HAS_YELLOW_SLIDING_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "Haunted Halls Room 3 Door": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BLOCK_LAUNCHERS &
                                   HAS_YELLOW_GORBS & HAS_YELLOW_SKULL_BLOCKS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BLOCK_LAUNCHERS &
                                   HAS_YELLOW_GORBS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BLOCK_LAUNCHERS),
                                  (HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "Haunted Halls Level Clear": [(HAS_YELLOW_BUMPERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                   HAS_YELLOW_GORBS & HAS_YELLOW_SKULL_BLOCKS),
                                  (HAS_YELLOW_BUMPERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                   HAS_YELLOW_GORBS),
                                  (HAS_YELLOW_BUMPERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                  None],
    #Borrowed Time
    "Borrowed Time Room 1 Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Borrowed Time Coin 1": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                              HAS_BLUE_SKULL_BLOCKS),
                             (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                             (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                             (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Borrowed Time Room 2 Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Borrowed Time Room 3 Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                   HAS_BLUE_SKULL_RINGS & HAS_BLUE_SKULL_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                  (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Borrowed Time Level Clear": [(HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                   HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                  (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                   HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                  (HAS_CLEAR_BUBBLES),
                                  (HAS_CLEAR_BUBBLES)],
    #Nyctophobia
    "Nyctophobia Coin 1": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                           (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                           (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                           (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Nyctophobia Room 1 Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Nyctophobia Coin 2": [(HAS_CLEAR_BUBBLES),
                           (HAS_CLEAR_BUBBLES),
                           (HAS_CLEAR_BUBBLES),
                           (HAS_CLEAR_BUBBLES)],
    "Nyctophobia Room 2 Door": [(HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                 HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                 HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                 HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                 HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Nyctophobia Coin 3": [(HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                           (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                           (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                           (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS)],
    "Nyctophobia Room 3 Door": [(HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS &
                                 HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS &
                                 HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                                (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS)],
    "Nyctophobia Checkpoint 1": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                  HAS_CLEAR_BUBBLES & HAS_BLUE_SKULL_RINGS),
                                 (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                  HAS_CLEAR_BUBBLES),
                                 (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                  HAS_CLEAR_BUBBLES),
                                 None],
    "Nyctophobia Coin 4": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                            HAS_CLEAR_BUBBLES & HAS_BLUE_SKULL_RINGS &
                            HAS_STANDARD_POP_BLOCKS),
                           (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                            HAS_CLEAR_BUBBLES),
                           (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                            HAS_CLEAR_BUBBLES),
                           (None)],
    "Nyctophobia Room 4 Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                  HAS_CLEAR_BUBBLES & HAS_BLUE_SKULL_RINGS &
                                  HAS_STANDARD_POP_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                 HAS_CLEAR_BUBBLES & HAS_STANDARD_POP_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                 HAS_CLEAR_BUBBLES & HAS_STANDARD_POP_BLOCKS),
                                (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                 HAS_STANDARD_POP_BLOCKS)],
    "Nyctophobia Coin 5": [(HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES),
                           (HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES),
                           (HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES),
                           (HAS_BLUE_GORBS)],
    "Nyctophobia Level Clear": [(HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES &
                                 HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES &
                                 HAS_BLUE_BLOCK_LAUNCHERS),
                                (HAS_BLUE_GORBS & HAS_CLEAR_BUBBLES),
                                (HAS_BLUE_GORBS & (HAS_CLEAR_BUBBLES |
                                 HAS_BLUE_BLOCK_LAUNCHERS))],
    #Shifting Walls
    "Shifting Walls Room 1 Door": [(HAS_STANDARD_POP_BLOCKS),
                                   (HAS_STANDARD_POP_BLOCKS),
                                   (HAS_STANDARD_POP_BLOCKS),
                                   None],
    "Shifting Walls Room 2 Door": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                    HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                    HAS_BLUE_SLIDING_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                    HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                    HAS_BLUE_SLIDING_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                    HAS_BLUE_SLIDING_BLOCKS),
                                   None],
    "Shifting Walls Checkpoint 1": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                    (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                    (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                    (HAS_GLASS_BLOCKS)],
    "Shifting Walls Coin 1": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                              (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                              (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                              (HAS_GLASS_BLOCKS)],
    "Shifting Walls Room 3 Door": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                   (HAS_GLASS_BLOCKS)],
    "Shifting Walls Coin 2": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                               HAS_STANDARD_POP_BLOCKS & HAS_BLUE_SKULL_BLOCKS),
                              (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS & 
                               HAS_STANDARD_POP_BLOCKS),
                              (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                               HAS_STANDARD_POP_BLOCKS),
                              (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "Shifting Walls Checkpoint 2": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                     HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                    (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                     HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                    (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                    (HAS_GLASS_BLOCKS)],
    "Shifting Walls Level Clear": [(HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                    HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                    HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS),
                                   (HAS_GLASS_BLOCKS & HAS_STANDARD_POP_BLOCKS)],
    #Skullduggery
    "Skullduggery Room 1 Door": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_LIFTS &
                                  HAS_YELLOW_VIVI_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_LIFTS &
                                  HAS_YELLOW_VIVI_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_LIFTS &
                                  HAS_YELLOW_VIVI_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_VIVI_BLOCKS)],
    "Skullduggery Coin 1": [(HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_SKULL_BLOCKS &
                             HAS_RED_FIRE_RINGS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_RED_FIRE_RINGS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS)],
    "Skullduggery Coin 2": [(HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_SKULL_BLOCKS &
                             HAS_RED_FIRE_RINGS & HAS_YELLOW_BLOCK_LAUNCHERS &
                             HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_RED_FIRE_RINGS &
                             HAS_YELLOW_BLOCK_LAUNCHERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_BLOCK_LAUNCHERS & 
                             HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                            (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "Skullduggery Room 2 Door": [(HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_SKULL_BLOCKS &
                                  HAS_RED_FIRE_RINGS & HAS_YELLOW_BLOCK_LAUNCHERS &
                                  HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                 (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_RED_FIRE_RINGS &
                                  HAS_YELLOW_BLOCK_LAUNCHERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                 (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_BLOCK_LAUNCHERS & 
                                  HAS_YELLOW_PUNCHAPPEAR_BLOCKS),
                                 (HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "Skullduggery Coin 3": [(HAS_YELLOW_BUMPERS & HAS_YELLOW_GORBS),
                            (HAS_YELLOW_BUMPERS),
                            (HAS_YELLOW_BUMPERS),
                            (HAS_YELLOW_BUMPERS)],
    "Skullduggery Room 3 Door": [(HAS_YELLOW_BUMPERS & HAS_YELLOW_GORBS &
                                  HAS_YELLOW_SKULL_RINGS & HAS_YELLOW_SLIDING_BLOCKS),
                                 (HAS_YELLOW_BUMPERS & HAS_YELLOW_GORBS &
                                  HAS_YELLOW_SLIDING_BLOCKS),
                                 (HAS_YELLOW_BUMPERS & HAS_YELLOW_GORBS &
                                  HAS_YELLOW_SLIDING_BLOCKS),
                                 (HAS_YELLOW_BUMPERS & HAS_YELLOW_GORBS &
                                  HAS_YELLOW_SLIDING_BLOCKS)],
    "Skullduggery Room 4 Door": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SWITCHES &
                                  HAS_ORANGE_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SKULL_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SWITCHES &
                                  HAS_ORANGE_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SKULL_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SWITCHES &
                                  HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SWITCHES &
                                  HAS_ORANGE_PUNCHAPPEAR_BLOCKS)],
    "Skullduggery Coin 4": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                             HAS_RED_FIRE_RINGS & HAS_YELLOW_SKULL_RINGS & 
                             HAS_YELLOW_CRYSTAL_LAUNCHERS & HAS_YELLOW_VIVI_BLOCKS),
                            (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                             HAS_RED_FIRE_RINGS & HAS_YELLOW_CRYSTAL_LAUNCHERS &
                             HAS_YELLOW_VIVI_BLOCKS),
                            (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                             HAS_RED_FIRE_RINGS & HAS_YELLOW_CRYSTAL_LAUNCHERS),
                            (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_RED_FIRE_RINGS,
                             HAS_YELLOW_CRYSTAL_LAUNCHERS)],
    "Skullduggery Level Clear": [(HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                  HAS_RED_FIRE_RINGS & HAS_YELLOW_SKULL_RINGS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                  HAS_RED_FIRE_RINGS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                  HAS_RED_FIRE_RINGS),
                                 (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_RED_FIRE_RINGS)],
    #The Throne Room
    "The Throne Room Room 1 Door": [(HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Coin 1": [(HAS_BOMB_BLOCKS),
                               (HAS_BOMB_BLOCKS),
                               (HAS_BOMB_BLOCKS),
                               (None)],
    "The Throne Room Room 2 Door": [(HAS_BOMB_BLOCKS),
                                    (HAS_BOMB_BLOCKS),
                                    (HAS_BOMB_BLOCKS),
                                    (None)],
    "The Throne Room Room 3 Door 1": [(HAS_SLIDING_HEART_BLOCKS & HAS_CLEAR_BUBBLES),
                                      (HAS_SLIDING_HEART_BLOCKS & HAS_CLEAR_BUBBLES),
                                      (HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Room 3 Door 2": [(HAS_SLIDING_HEART_BLOCKS & HAS_CLEAR_BUBBLES),
                                      (HAS_SLIDING_HEART_BLOCKS & HAS_CLEAR_BUBBLES),
                                      (HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Room 4A Door": [(HAS_YELLOW_GORBS & HAS_YELLOW_SKULL_RINGS &
                                      HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_ORANGE_SWITCHES &
                                      HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_YELLOW_GORBS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                      HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_YELLOW_GORBS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                      HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_YELLOW_GORBS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                      HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS)],
    "The Throne Room Room 4B Door": [(HAS_BLUE_GORBS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_BLUE_GORBS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_BLUE_GORBS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                     (HAS_BLUE_GORBS & HAS_GLASS_BLOCKS &
                                      HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    "The Throne Room Coin 2": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                HAS_BLUE_SKULL_RINGS & HAS_SLIDING_HEART_BLOCKS),
                               (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                HAS_SLIDING_HEART_BLOCKS),
                               (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                HAS_SLIDING_HEART_BLOCKS),
                               (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                HAS_YELLOW_PUNCHAPPEAR_BLOCKS)],
    "The Throne Room Room 5 Door 1": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                       HAS_BLUE_SKULL_RINGS & HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                       HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Room 5 Door 2": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                       HAS_BLUE_SKULL_RINGS & HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_SKULL_RINGS &
                                       HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                       HAS_SLIDING_HEART_BLOCKS),
                                      (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                       HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Room 6A Door": [(HAS_ORANGE_SWITCHES & HAS_ORANGE_SKULL_BLOCKS &
                                      HAS_ORANGE_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_CRYSTAL_LAUNCHERS &
                                      HAS_YELLOW_SLIDING_BLOCKS),
                                     (HAS_ORANGE_SWITCHES & HAS_ORANGE_SKULL_BLOCKS &
                                      HAS_ORANGE_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_CRYSTAL_LAUNCHERS &
                                      HAS_YELLOW_SLIDING_BLOCKS),
                                     (HAS_ORANGE_SWITCHES & HAS_ORANGE_SKULL_BLOCKS &
                                      HAS_ORANGE_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_CRYSTAL_LAUNCHERS),
                                     (HAS_YELLOW_CRYSTAL_LAUNCHERS | HAS_YELLOW_SLIDING_BLOCKS)],
    "The Throne Room Room 6B Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_SKULL_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS &
                                      HAS_BLUE_SLIDING_BLOCKS),
                                     (HAS_BLUE_SWITCHES & HAS_BLUE_SKULL_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS &
                                      HAS_BLUE_SLIDING_BLOCKS),
                                     (HAS_BLUE_SWITCHES & HAS_BLUE_SKULL_BLOCKS &
                                      HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_CRYSTAL_LAUNCHERS),
                                     (HAS_BLUE_CRYSTAL_LAUNCHERS | HAS_BLUE_SLIDING_BLOCKS)],
    "The Throne Room Room 7 Door": [(HAS_SLIDING_HEART_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS & HAS_YELLOW_SKULL_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Heart 1": [(HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS),
                                (HAS_STANDARD_HEART_BLOCKS)],
    "The Throne Room Heart 2": [(HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_YELLOW_STAR_BLOCKS & HAS_SLIDING_HEART_BLOCKS &
                                 HAS_YELLOW_SKULL_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_YELLOW_STAR_BLOCKS & HAS_SLIDING_HEART_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_YELLOW_STAR_BLOCKS & HAS_SLIDING_HEART_BLOCKS),
                                (HAS_STANDARD_HEART_BLOCKS & HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Heart 3": [(HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_BLUE_STAR_BLOCKS & HAS_DELAYED_HEART_BLOCKS &
                                 HAS_BLUE_SKULL_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_BLUE_STAR_BLOCKS & HAS_DELAYED_HEART_BLOCKS),
                                (HAS_STANDARD_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                 HAS_BLUE_STAR_BLOCKS & HAS_DELAYED_HEART_BLOCKS),
                                (HAS_STANDARD_HEART_BLOCKS & HAS_DELAYED_HEART_BLOCKS)],
    "The Throne Room Boss Arena Door": [(HAS_STANDARD_STAR_BLOCKS & HAS_YELLOW_STAR_BLOCKS &
                                         HAS_BLUE_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                         HAS_SLIDING_HEART_BLOCKS & HAS_DELAYED_HEART_BLOCKS &
                                         HAS_YELLOW_SKULL_BLOCKS & HAS_BLUE_SKULL_BLOCKS),
                                        (HAS_STANDARD_STAR_BLOCKS & HAS_YELLOW_STAR_BLOCKS &
                                         HAS_BLUE_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                         HAS_SLIDING_HEART_BLOCKS & HAS_DELAYED_HEART_BLOCKS),
                                        (HAS_STANDARD_STAR_BLOCKS & HAS_YELLOW_STAR_BLOCKS &
                                         HAS_BLUE_STAR_BLOCKS & HAS_STANDARD_HEART_BLOCKS &
                                         HAS_SLIDING_HEART_BLOCKS & HAS_DELAYED_HEART_BLOCKS),
                                        (HAS_STANDARD_HEART_BLOCKS & HAS_SLIDING_HEART_BLOCKS &
                                         HAS_DELAYED_HEART_BLOCKS)],
    "The Throne Room Coin 3": [(HAS_SLIDING_HEART_BLOCKS),
                               (HAS_SLIDING_HEART_BLOCKS),
                               (HAS_SLIDING_HEART_BLOCKS),
                               (HAS_SLIDING_HEART_BLOCKS)],
    "The Throne Room Level Clear": [(HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS),
                                    (HAS_SLIDING_HEART_BLOCKS)],
    #Pop To The Top
    "Pop To The Top Coin 1": [(HAS_CLEAR_BUBBLES),
                              (HAS_CLEAR_BUBBLES),
                              (HAS_CLEAR_BUBBLES),
                              (HAS_CLEAR_BUBBLES)],
    "Pop To The Top Room 1 Door": [(HAS_CLEAR_BUBBLES),
                                   (HAS_CLEAR_BUBBLES),
                                   (HAS_CLEAR_BUBBLES),
                                   (HAS_CLEAR_BUBBLES)],
    "Pop To The Top Coin 2": [(HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                              (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                              (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                              (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES)],
    "Pop To The Top Room 2 Door": [(HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                   (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                   (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                   (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES)],
    "Pop To The Top Level Clear": [(HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                    HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_BLUE_SKULL_BLOCKS),
                                   (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                    HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                   (HAS_CLEAR_BUBBLES & HAS_BLUE_SWITCHES &
                                    HAS_BLUE_PUNCHAPPEAR_BLOCKS),
                                   (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS)],
    #Periodic Prison
    "Periodic Prison Room 1 Door": [(HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS)],
    "Periodic Prison Room 2 Door": [(HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                                    (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                                    (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS),
                                    (HAS_CLEAR_BUBBLES & HAS_GLASS_BLOCKS)],
    "Periodic Prison Room 3 Door": [(HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS)],
    "Periodic Prison Coin 1": [(HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES)],
    "Periodic Prison Coin 2": [(HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                               (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES)],
    "Periodic Prison Level Clear": [(HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                     HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                     HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                     HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES),
                                    (HAS_GLASS_BLOCKS & HAS_BLUE_SWITCHES &
                                     HAS_BLUE_PUNCHAPPEAR_BLOCKS & HAS_CLEAR_BUBBLES)],
    #Infinity Garden
    "Infinity Garden Coin 1": [(HAS_STANDARD_SEMISOLIDS),
                               (HAS_STANDARD_SEMISOLIDS),
                               (HAS_STANDARD_SEMISOLIDS),
                               (HAS_STANDARD_SEMISOLIDS)],
    "Infinity Garden Room 1 Door": [(HAS_STANDARD_SEMISOLIDS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_STANDARD_SEMISOLIDS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_STANDARD_SEMISOLIDS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_STANDARD_SEMISOLIDS)],
    "Infinity Garden Coin 2": [(HAS_STANDARD_PHYSICS_BLOCKS),
                               (HAS_STANDARD_PHYSICS_BLOCKS),
                               (HAS_STANDARD_PHYSICS_BLOCKS),
                               (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Infinity Garden Room 2 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_INVERTED_SEMISOLIDS),
                                    (None),
                                    (None),
                                    (None)],
    "Infinity Garden Coin 3": [(None),
                               (None),
                               (None),
                               (None)],
    "Infinity Garden Load Bearing Collectible": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_UP_GRAVITY_FLIPPERS &
                                                  HAS_DOWN_GRAVITY_FLIPPERS),
                                                 (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_UP_GRAVITY_FLIPPERS &
                                                  HAS_DOWN_GRAVITY_FLIPPERS),
                                                 (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_UP_GRAVITY_FLIPPERS &
                                                  HAS_DOWN_GRAVITY_FLIPPERS),
                                                 (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_UP_GRAVITY_FLIPPERS)],
    "Infinity Garden Level Clear": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS | HAS_TOGGLE_SEMISOLIDS)],
    #Autumnal Aether
    "Autumnal Aether Coin 1": [(HAS_RED_BALLOONS & HAS_BLUE_BALLOONS),
                               (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS),
                               (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS),
                               (HAS_RED_BALLOONS)],
    "Autumnal Aether Coin 2": [(HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                HAS_INVERTED_BLOCK_LAUNCHERS),
                               (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                HAS_INVERTED_BLOCK_LAUNCHERS),
                               (HAS_RED_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS),
                               (HAS_RED_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS)],
    "Autumnal Aether Checkpoint 1": [(HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                      HAS_INVERTED_BLOCK_LAUNCHERS),
                                     (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                      HAS_INVERTED_BLOCK_LAUNCHERS),
                                     (HAS_RED_BALLOONS),
                                     (HAS_RED_BALLOONS)],
    "Autumnal Aether Coin 3": [(HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                HAS_INVERTED_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES),
                               (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                HAS_INVERTED_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES),
                               (HAS_RED_BALLOONS & HAS_GREEN_BUBBLES),
                               (HAS_RED_BALLOONS & HAS_GREEN_BUBBLES)],
    "Autumnal Aether Room 1 Door": [(HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                     HAS_INVERTED_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES),
                                    (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS &
                                     HAS_INVERTED_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES),
                                    (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS),
                                    (HAS_RED_BALLOONS & HAS_BLUE_BALLOONS)],
    "Autumnal Aether Tutorial Panel": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                       (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                       (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                       (HAS_INVERTED_BLOCK_LAUNCHERS)],
    "Autumnal Aether Checkpoint 2": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS &
                                      HAS_BLUE_BALLOONS),
                                     (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS &
                                      HAS_BLUE_BALLOONS),
                                     (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                     (HAS_INVERTED_BLOCK_LAUNCHERS)],
    "Autumnal Aether Room 2 Door": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_GREEN_BUBBLES),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_GREEN_BUBBLES),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES)],
    "Autumnal Aether Coin 4": [(HAS_BLUE_BALLOONS & HAS_RED_BALLOONS),
                               (HAS_BLUE_BALLOONS & HAS_RED_BALLOONS),
                               (HAS_BLUE_BALLOONS),
                               (HAS_BLUE_BALLOONS)],
    "Autumnal Aether Coin 5": [(HAS_BLUE_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS),
                               (HAS_BLUE_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS),
                               (HAS_BLUE_BALLOONS),
                               (HAS_BLUE_BALLOONS)],
    "Autumnal Aether Level Clear": [(HAS_BLUE_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_GREEN_BUBBLES),
                                    (HAS_BLUE_BALLOONS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_GREEN_BUBBLES),
                                    (HAS_BLUE_BALLOONS),
                                    (HAS_BLUE_BALLOONS)],
    #Among The Stars
    "Among The Stars Coin 1": [(HAS_MOON_LAUNCHERS),
                               (HAS_MOON_LAUNCHERS),
                               (HAS_MOON_LAUNCHERS),
                               (HAS_MOON_LAUNCHERS)],
    "Among The Stars Room 1 Door": [(HAS_MOON_LAUNCHERS),
                                    (HAS_MOON_LAUNCHERS),
                                    (HAS_MOON_LAUNCHERS),
                                    (HAS_MOON_LAUNCHERS)],
    "Among The Stars Coin 2": [(HAS_MOON_LAUNCHERS & HAS_RED_FIRE_RINGS &
                                HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_BALLOONS &
                                HAS_LEAD_BALLOONS & HAS_RED_BALLOONS),
                               (HAS_MOON_LAUNCHERS & HAS_RED_FIRE_RINGS &
                                HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_BALLOONS &
                                HAS_LEAD_BALLOONS & HAS_RED_BALLOONS),
                               (HAS_MOON_LAUNCHERS),
                               (HAS_MOON_LAUNCHERS)],
    "Among The Stars Room 2 Door": [(HAS_MOON_LAUNCHERS & HAS_RED_FIRE_RINGS &
                                     HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_BALLOONS &
                                     HAS_LEAD_BALLOONS & HAS_RED_BALLOONS),
                                    (HAS_MOON_LAUNCHERS & HAS_RED_PEARL_LAUNCHERS &
                                     HAS_BLUE_BALLOONS & HAS_LEAD_BALLOONS &
                                     HAS_RED_BALLOONS),
                                    (HAS_MOON_LAUNCHERS & (HAS_RED_FIRE_RINGS |
                                     HAS_RED_BALLOONS | HAS_BLUE_BALLOONS)),
                                    (HAS_MOON_LAUNCHERS & (HAS_RED_FIRE_RINGS |
                                     HAS_RED_BALLOONS | HAS_BLUE_BALLOONS))],
    "Among The Stars Checkpoint 1": [(HAS_MOON_LAUNCHERS & HAS_INVERTED_SEMISOLIDS &
                                      HAS_RED_FIRE_RINGS),
                                     (HAS_MOON_LAUNCHERS),
                                     (HAS_MOON_LAUNCHERS),
                                     (HAS_MOON_LAUNCHERS)],
    "Among The Stars Room 3 Door": [(HAS_MOON_LAUNCHERS & HAS_INVERTED_SEMISOLIDS &
                                     HAS_RED_FIRE_RINGS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                     HAS_INVERTED_BLOCK_LAUNCHERS),
                                    (HAS_MOON_LAUNCHERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                     HAS_INVERTED_BLOCK_LAUNCHERS),
                                    (HAS_MOON_LAUNCHERS & (HAS_STANDARD_BLOCK_LAUNCHERS |
                                     HAS_INVERTED_BLOCK_LAUNCHERS)),
                                    (HAS_MOON_LAUNCHERS)],
    "Among The Stars Level Clear": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                     HAS_MOON_LAUNCHERS),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_MOON_LAUNCHERS),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & (HAS_STANDARD_BLOCK_LAUNCHERS |
                                     HAS_MOON_LAUNCHERS)),
                                    (HAS_INVERTED_BLOCK_LAUNCHERS & (HAS_STANDARD_BLOCK_LAUNCHERS |
                                     HAS_MOON_LAUNCHERS))],
    #Den Of Pixies
    "Den Of Pixies Room 1 Door": [(HAS_PIXIES & HAS_THERMALS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_THERMALS),
                                  (HAS_THERMALS),
                                  (HAS_THERMALS)],
    "Den Of Pixies Coin 1": [(HAS_PIXIES & HAS_INVERTED_BLOCK_LAUNCHERS &
                              HAS_STANDARD_PHYSICS_BLOCKS & HAS_THERMALS),
                             (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_PHYSICS_BLOCKS &
                              HAS_THERMALS),
                             (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_PHYSICS_BLOCKS),
                             (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Den Of Pixies Room 2 Door": [(HAS_PIXIES & HAS_INVERTED_BLOCK_LAUNCHERS &
                                   HAS_STANDARD_PHYSICS_BLOCKS & HAS_THERMALS),
                                  (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_PHYSICS_BLOCKS),
                                  (HAS_STANDARD_PHYSICS_BLOCKS)],
    "Den Of Pixies Coin 2": [(HAS_PIXIES & HAS_STANDARD_BLOCK_LAUNCHERS),
                             (HAS_PIXIES & HAS_STANDARD_BLOCK_LAUNCHERS),
                             (None),
                             (None)],
    "Den Of Pixies Room 3 Door": [(HAS_PIXIES & HAS_INVERTED_BLOCK_LAUNCHERS &
                                   HAS_THERMALS & HAS_TOGGLE_SEMISOLIDS),
                                  (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_THERMALS &
                                   HAS_TOGGLE_SEMISOLIDS),
                                  (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_THERMALS),
                                  (HAS_THERMALS)],
    "Den Of Pixies Coin 3": [(HAS_PIXIES & HAS_STANDARD_BLOCK_LAUNCHERS &
                              HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                             (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                             (HAS_STANDARD_BLOCK_LAUNCHERS),
                             (None)],
    "Den Of Pixies Level Clear": [(HAS_PIXIES & HAS_STANDARD_BLOCK_LAUNCHERS &
                                   HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                  (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                  (HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (None)],
    #Heels Over Head
    "Heels Over Head Room 1 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_DOWN_WATER &
                                     HAS_DOWN_GRAVITY_FLIPPERS),
                                    (None),
                                    (None),
                                    (None)],
    "Heels Over Head Checkpoint 1": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_UP_GRAVITY_FLIPPERS &
                                      HAS_INVERTED_SEMISOLIDS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                      HAS_DOWN_GRAVITY_FLIPPERS & HAS_TOGGLE_SEMISOLIDS),
                                     (HAS_UP_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                      HAS_DOWN_GRAVITY_FLIPPERS),
                                     (HAS_STANDARD_PHYSICS_BLOCKS | (HAS_UP_GRAVITY_FLIPPERS &
                                      HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS)),
                                     (HAS_STANDARD_PHYSICS_BLOCKS | (HAS_UP_GRAVITY_FLIPPERS &
                                      HAS_DOWN_GRAVITY_FLIPPERS))],
    "Heels Over Head Room 2 Door": [(HAS_STANDARD_PHYSICS_BLOCKS & HAS_UP_GRAVITY_FLIPPERS &
                                     HAS_INVERTED_SEMISOLIDS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_DOWN_GRAVITY_FLIPPERS & HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_UP_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_DOWN_GRAVITY_FLIPPERS),
                                    (HAS_STANDARD_PHYSICS_BLOCKS | (HAS_UP_GRAVITY_FLIPPERS &
                                     HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS)),
                                    (HAS_STANDARD_PHYSICS_BLOCKS | (HAS_UP_GRAVITY_FLIPPERS &
                                     HAS_DOWN_GRAVITY_FLIPPERS))],
    "Heels Over Head Coin 1": [(HAS_INVERTED_SEMISOLIDS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                HAS_DOWN_GRAVITY_FLIPPERS),
                               (HAS_INVERTED_SEMISOLIDS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                HAS_DOWN_GRAVITY_FLIPPERS),
                               (HAS_INVERTED_SEMISOLIDS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                HAS_DOWN_GRAVITY_FLIPPERS),
                               (HAS_INVERTED_SEMISOLIDS)],
    "Heels Over Head Room 3 Door": [(HAS_INVERTED_SEMISOLIDS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_TOGGLE_SEMISOLIDS & HAS_UP_GRAVITY_FLIPPERS),
                                    (HAS_INVERTED_SEMISOLIDS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS &
                                     HAS_TOGGLE_SEMISOLIDS),
                                    (HAS_INVERTED_SEMISOLIDS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_BLOCK_LAUNCHERS),
                                    (HAS_INVERTED_SEMISOLIDS & HAS_STANDARD_SEMISOLIDS &
                                     HAS_DOWN_GRAVITY_FLIPPERS)],
    "Heels Over Head Level Clear": [(HAS_UP_WATER & HAS_DOWN_WATER &
                                     HAS_STANDARD_BLOCK_LAUNCHERS & HAS_INVERTED_BLOCK_LAUNCHERS),
                                    (HAS_UP_WATER & HAS_STANDARD_BLOCK_LAUNCHERS),
                                    (HAS_STANDARD_BLOCK_LAUNCHERS),
                                    (HAS_STANDARD_BLOCK_LAUNCHERS)],
    #The Hive
    "The Hive Room 1 Door": [(HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_DOWN_GRAVITY_FLIPPERS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_DOWN_GRAVITY_FLIPPERS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_DOWN_GRAVITY_FLIPPERS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS)],
    "The Hive Checkpoint 1": [(HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                               HAS_TOGGLE_FLOWERS & HAS_TOGGLE_SEMISOLIDS),
                              (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                               HAS_TOGGLE_FLOWERS),
                              (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                               HAS_TOGGLE_FLOWERS),
                              (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                               HAS_TOGGLE_FLOWERS)],
    "The Hive Coin 1": [(HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                         HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS &
                         HAS_TOGGLE_SEMISOLIDS),
                        (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                         HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS),
                        (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                         HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS),
                        (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                         HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS)],
    "The Hive Room 2 Door": [(HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS &
                              HAS_TOGGLE_SEMISOLIDS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_TOGGLE_FLOWERS & HAS_RED_HIVE_BLOCKS)],
    "The Hive Coin 2": [(HAS_HIVE_LIFTS & HAS_STANDARD_SEMISOLIDS &
                         HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                        (HAS_HIVE_LIFTS & HAS_HIVE_BOMBS &
                         HAS_RED_HIVE_BLOCKS),
                        (HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                        (HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS)],
    "The Hive Room 3 Door": [(HAS_HIVE_LIFTS & HAS_STANDARD_SEMISOLIDS &
                              HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_LIFTS & HAS_STANDARD_SEMISOLIDS &
                              HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS),
                             (HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS)],
    "The Hive Room 4 Door": [(HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS & HAS_RED_HIVE_BLOCKS &
                              HAS_STANDARD_SEMISOLIDS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS & HAS_RED_HIVE_BLOCKS),
                             (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                              HAS_HIVE_LIFTS & HAS_RED_HIVE_BLOCKS)],
    "The Hive Coin 3": [(HAS_GREEN_BUBBLES & HAS_HONEY_BUBBLES),
                        (HAS_GREEN_BUBBLES & HAS_HONEY_BUBBLES),
                        (HAS_GREEN_BUBBLES & HAS_HONEY_BUBBLES),
                        (HAS_GREEN_BUBBLES & HAS_HONEY_BUBBLES)],
    "The Hive Room 5 Door": [(HAS_GREEN_BUBBLES & HAS_HONEY_BUBBLES &
                              HAS_RED_BALLOONS & HAS_RED_FIRE_RINGS &
                              HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS &
                              HAS_STANDARD_SEMISOLIDS & HAS_INVERTED_SEMISOLIDS),
                             (HAS_GREEN_BUBBLES & (HAS_HONEY_BUBBLES |
                              HAS_RED_BALLOONS) & HAS_RED_FIRE_RINGS &
                              HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS &
                              HAS_STANDARD_SEMISOLIDS),
                             (HAS_GREEN_BUBBLES & ((HAS_HONEY_BUBBLES &
                              HAS_RED_FIRE_RINGS) | HAS_RED_BALLOONS) &
                              HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                             (HAS_GREEN_BUBBLES & (HAS_HONEY_BUBBLES |
                              HAS_RED_BALLOONS) & HAS_HIVE_BOMBS &
                              HAS_RED_HIVE_BLOCKS)],
    "The Hive Checkpoint 2": [(HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS),
                              (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS),
                              (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS),
                              (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS)],
    "The Hive Room 6 Door": [(HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS &
                              HAS_KEY_BUBBLES),
                             (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS &
                              HAS_KEY_BUBBLES),
                             (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS &
                              HAS_KEY_BUBBLES),
                             (HAS_GRAVITY_FISTS & HAS_RED_FIRE_RINGS &
                              HAS_KEY_BUBBLES)],
    "The Hive Level Clear": [(HAS_UP_WATER & HAS_HIVE_BOMBS &
                              HAS_RED_HIVE_BLOCKS),
                             (HAS_UP_WATER & HAS_HIVE_BOMBS &
                              HAS_RED_HIVE_BLOCKS),
                             (HAS_UP_WATER & HAS_HIVE_BOMBS &
                              HAS_RED_HIVE_BLOCKS),
                             (HAS_UP_WATER & HAS_HIVE_BOMBS &
                              HAS_RED_HIVE_BLOCKS)],
    #The Five Mile Spire
    "The Five Mile Spire Room 1 Door": [(HAS_SMASH_BLOCKS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_DOWN_GRAVITY_FLIPPERS),
                                        (HAS_SMASH_BLOCKS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_DOWN_GRAVITY_FLIPPERS),
                                        (HAS_SMASH_BLOCKS & HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_SMASH_BLOCKS & HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Coin 1": [(HAS_GRAVITY_ANCHORS & HAS_CONCRETE_BLOCKS),
                                   (HAS_GRAVITY_ANCHORS & HAS_CONCRETE_BLOCKS),
                                   (HAS_GRAVITY_ANCHORS & HAS_CONCRETE_BLOCKS),
                                   (HAS_GRAVITY_ANCHORS & HAS_CONCRETE_BLOCKS)],
    "The Five Mile Spire Room 2 Door": [(HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Coin 2": [(HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Coin 3": [(HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS &
                                    HAS_UP_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS),
                                   (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                    HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Room 3 Door": [(HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS &
                                         HAS_UP_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS & HAS_DOWN_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_SMASH_BLOCKS &
                                         HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Room 4 Door": [(HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS & HAS_GREEN_BUBBLES &
                                         HAS_UP_GRAVITY_FIELDS & HAS_UP_WATER &
                                         HAS_DOWN_WATER & HAS_RED_FIRE_RINGS &
                                         HAS_DOWN_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS & HAS_RED_FIRE_RINGS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS & HAS_RED_FIRE_RINGS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS & HAS_RED_FIRE_RINGS)],
    "The Five Mile Spire Room 5 Door": [(HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS)],
    "The Five Mile Spire Room 6 Door": [(HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS & HAS_GREEN_BUBBLES &
                                         HAS_DOWN_WATER & HAS_UP_WATER &
                                         HAS_DOWN_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS),
                                        (HAS_GRAVITY_ANCHORS & HAS_INVERTED_KEY_BLOCKS &
                                         HAS_SMASH_BLOCKS)],
    "The Five Mile Spire Room 7 Side Door": [(None),
                                             (None),
                                             (None),
                                             (None)],
    "The Five Mile Spire Coin 4": [(HAS_GRAVITY_ANCHORS & HAS_CONCRETE_BLOCKS &
                                    HAS_UP_GRAVITY_FLIPPERS & HAS_DOWN_GRAVITY_FLIPPERS),
                                   (HAS_GRAVITY_ANCHORS & HAS_UP_GRAVITY_FLIPPERS &
                                    HAS_DOWN_GRAVITY_FLIPPERS),
                                   (HAS_GRAVITY_ANCHORS & HAS_UP_GRAVITY_FLIPPERS),
                                   (HAS_GRAVITY_ANCHORS & HAS_UP_GRAVITY_FLIPPERS)],
    "The Five Mile Spire Room 7 Door": [(HAS_DOWN_GRAVITY_FLIPPERS & HAS_DOWN_WATER &
                                         HAS_UP_GRAVITY_FIELDS & HAS_UP_WATER &
                                         HAS_RED_FIRE_RINGS & HAS_LEAD_BALLOONS),
                                        (HAS_DOWN_GRAVITY_FLIPPERS & HAS_DOWN_WATER &
                                         HAS_UP_GRAVITY_FIELDS & HAS_UP_WATER),
                                        (HAS_DOWN_WATER & HAS_UP_GRAVITY_FIELDS &
                                         HAS_UP_WATER),
                                        (HAS_DOWN_WATER & HAS_UP_GRAVITY_FIELDS &
                                         HAS_UP_WATER)],
    "The Five Mile Spire Coin 5": [(HAS_GRAVITY_ANCHORS & HAS_DOWN_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS & HAS_DOWN_GRAVITY_FIELDS),
                                   (HAS_GRAVITY_ANCHORS),
                                   (HAS_GRAVITY_ANCHORS)],
    "The Five Mile Spire Level Clear": [(HAS_GRAVITY_ANCHORS & HAS_DOWN_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS & HAS_DOWN_GRAVITY_FIELDS),
                                        (HAS_GRAVITY_ANCHORS),
                                        (HAS_GRAVITY_ANCHORS)],
    #Gube Gardens
    "Gube Gardens Coin 1": [(HAS_GUBES & HAS_TETHERS),
                            (HAS_GUBES & HAS_TETHERS),
                            (HAS_GUBES & HAS_TETHERS),
                            (HAS_GUBES & HAS_TETHERS)],
    "Gube Gardens Room 1 Door": [(HAS_GUBES & HAS_TETHERS),
                                 (HAS_GUBES),
                                 (HAS_GUBES),
                                 (HAS_GUBES)],
    "Gube Gardens Coin 2": [(HAS_GUBES & HAS_TETHERS),
                            (HAS_TETHERS),
                            (None),
                            (None)],
    "Gube Gardens Room 2 Door": [(HAS_GUBES & HAS_TETHERS &
                                  HAS_STANDARD_SEMISOLIDS & HAS_INVERTED_SEMISOLIDS &
                                  HAS_TOGGLE_SEMISOLIDS & HAS_SMASH_BLOCKS),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS & (
                                  HAS_STANDARD_SEMISOLIDS | HAS_TOGGLE_SEMISOLIDS)),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS & (
                                  HAS_STANDARD_SEMISOLIDS | HAS_TOGGLE_SEMISOLIDS |
                                  HAS_TETHERS)),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS)],
    "Gube Gardens Room 3 Door": [(HAS_GUBES & HAS_TETHERS &
                                  HAS_SMASH_BLOCKS & HAS_RED_FIRE_RINGS &
                                  HAS_INVERTED_BLOCK_LAUNCHERS & HAS_PIXIES),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS &
                                  HAS_TETHERS),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS & (
                                  HAS_TETHERS | HAS_INVERTED_BLOCK_LAUNCHERS)),
                                 (HAS_GUBES & HAS_SMASH_BLOCKS)],
    "Gube Gardens Room 4 Door": [(HAS_GUBES & HAS_TETHERS &
                                  HAS_UP_GRAVITY_FLIPPERS & HAS_STANDARD_SEMISOLIDS &
                                  HAS_MOON_LAUNCHERS & HAS_TOGGLE_SEMISOLIDS &
                                  HAS_THERMALS & HAS_DOWN_GRAVITY_FLIPPERS &
                                  HAS_DOWN_WATER),
                                 (HAS_GUBES & HAS_TETHERS & (
                                  HAS_UP_GRAVITY_FLIPPERS | HAS_TOGGLE_SEMISOLIDS)),
                                 (HAS_GUBES & HAS_TETHERS),
                                 (HAS_GUBES & HAS_TETHERS)],
    "Gube Gardens Coin 3": [(HAS_GUBES & HAS_TETHERS),
                            (HAS_GUBES),
                            (None),
                            (None)],
    "Gube Gardens Level Clear": [(HAS_GUBES & HAS_TETHERS &
                                  HAS_STANDARD_SEMISOLIDS),
                                 (HAS_GUBES & HAS_TETHERS),
                                 (HAS_GUBES & HAS_TETHERS),
                                 (HAS_GUBES)],
    #The Golf Fungus
    "The Golf Fungus Room 1 Door": [(None),
                                    (None),
                                    (None),
                                    (None)],
    "The Golf Fungus Hole 1": [(HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 2 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 2": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_STANDARD_BLOCK_LAUNCHERS),
                               (HAS_GOLF_BALL & HAS_GOLF_CART &
                                HAS_STANDARD_BLOCK_LAUNCHERS)],
    "The Golf Fungus Room 3 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_STANDARD_BLOCK_LAUNCHERS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_STANDARD_BLOCK_LAUNCHERS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 3": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_INVERTED_SEMISOLIDS & HAS_UP_GRAVITY_FLIPPERS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 4 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_INVERTED_SEMISOLIDS & HAS_UP_GRAVITY_FLIPPERS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 4": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS)],
    "The Golf Fungus Room 5 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_HIVE_BOMBS & HAS_RED_HIVE_BLOCKS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 5": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_RED_BALLOONS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 6 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_RED_BALLOONS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 6": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_TOGGLE_BALLOONS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 7 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_TOGGLE_BALLOONS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 7": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_RED_BALLOONS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 8 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                     HAS_RED_BALLOONS),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL),
                                    (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Hole 8": [(HAS_GOLF_BALL & HAS_GRAVITY_FISTS &
                                HAS_RED_BALLOONS),
                               (HAS_GOLF_BALL),
                               (HAS_GOLF_BALL),
                               (HAS_GOLF_BALL)],
    "The Golf Fungus Room 9 Door": [(HAS_GOLF_BALL & HAS_GRAVITY_FISTS &
                                     HAS_RED_BALLOONS),
                                    (HAS_GOLF_BALL),
                                    (HAS_GOLF_BALL),
                                    (HAS_GOLF_BALL)],
    "The Golf Fungus Hole 9": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_RED_FIRE_RINGS & HAS_MOON_LAUNCHERS &
                                HAS_BLUE_BALLOONS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL &
                                HAS_RED_FIRE_RINGS),
                               (HAS_GOLF_CART & HAS_GOLF_BALL),
                               (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Room 10 Door": [(HAS_GOLF_CART & HAS_GOLF_BALL &
                                      HAS_RED_FIRE_RINGS & HAS_MOON_LAUNCHERS &
                                      HAS_BLUE_BALLOONS),
                                     (HAS_GOLF_CART & HAS_GOLF_BALL &
                                      HAS_RED_FIRE_RINGS),
                                     (HAS_GOLF_CART & HAS_GOLF_BALL),
                                     (HAS_GOLF_CART & HAS_GOLF_BALL)],
    "The Golf Fungus Coin 1": [(None),
                               (None),
                               (None),
                               (None)],
    "The Golf Fungus Level Clear": [(None),
                                    (None),
                                    (None),
                                    (None)],
    #Over The Woods
    "Over The Woods Room 1 Door": [(HAS_BLUE_BALLOONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_INVERTED_BLOCK_LAUNCHERS & HAS_STANDARD_SEMISOLIDS),
                                   (HAS_BLUE_BALLOONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_INVERTED_BLOCK_LAUNCHERS),
                                   (HAS_BLUE_BALLOONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_INVERTED_BLOCK_LAUNCHERS),
                                   (HAS_BLUE_BALLOONS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                    HAS_INVERTED_BLOCK_LAUNCHERS)],
    "Over The Woods Room 2 Door": [(HAS_UP_GRAVITY_FLIPPERS & HAS_DOWN_GRAVITY_FLIPPERS),
                                   (HAS_UP_GRAVITY_FLIPPERS & HAS_DOWN_GRAVITY_FLIPPERS),
                                   (HAS_UP_GRAVITY_FLIPPERS & HAS_DOWN_GRAVITY_FLIPPERS),
                                   (HAS_UP_GRAVITY_FLIPPERS & HAS_DOWN_GRAVITY_FLIPPERS)],
    "Over The Woods Coin 1": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                              (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                              (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                              (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS)],
    "Over The Woods Level Clear": [(HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                                   (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                                   (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS),
                                   (HAS_INVERTED_BLOCK_LAUNCHERS & HAS_BLUE_BALLOONS)],
    #Welcome To The Void
    "Welcome To The Void Coin 1": [(HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Room 1 Door": [(HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Tutorial Panel": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_FIREWORK_VIVI_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS | HAS_FIREWORK_VIVI_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS | HAS_FIREWORK_VIVI_BLOCKS),
                                           (HAS_STANDARD_BLOCK_LAUNCHERS | HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Room 2 Door": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS),
                                        (HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Coin 2": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Checkpoint 1": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                         (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                         (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                         (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Coin 3": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Room 3 Door": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "Welcome To The Void Checkpoint 2": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                         (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                         (HAS_FIREWORK_VIVI_BLOCKS),
                                         (HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Coin 4": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                   (HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Room 4 Door": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Coin 5": [(HAS_FIREWORK_VIVI_BLOCKS),
                                   (HAS_FIREWORK_VIVI_BLOCKS),
                                   (HAS_FIREWORK_VIVI_BLOCKS),
                                   (HAS_FIREWORK_VIVI_BLOCKS)],
    "Welcome To The Void Level Clear": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                        (HAS_FIREWORK_VIVI_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    #The Sky Is Falling
    "The Sky Is Falling Coin 1": [(HAS_FALLING_CRYSTALS),
                                  (HAS_FALLING_CRYSTALS),
                                  (None),
                                  (None)],
    "The Sky Is Falling Room 1 Door": [(HAS_FALLING_CRYSTALS),
                                       (HAS_FALLING_CRYSTALS),
                                       (None),
                                       (None)],
    "The Sky Is Falling Coin 2": [(HAS_GRAB_BLOCKS),
                                  (HAS_GRAB_BLOCKS),
                                  (HAS_GRAB_BLOCKS),
                                  (HAS_GRAB_BLOCKS)],
    "The Sky Is Falling Room 2 Door": [(HAS_GRAB_BLOCKS),
                                       (HAS_GRAB_BLOCKS),
                                       (HAS_GRAB_BLOCKS),
                                       (HAS_GRAB_BLOCKS)],
    "The Sky Is Falling Coin 3": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                  (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                  (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                  (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS)],
    "The Sky Is Falling Room 3 Door": [(HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                       (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                       (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                       (HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS)],
    "The Sky Is Falling Room 4 Door": [(HAS_FALLING_CRYSTALS & HAS_GRAB_BLOCKS &
                                        HAS_FIREWORK_VIVI_BLOCKS),
                                       (HAS_FALLING_CRYSTALS & HAS_GRAB_BLOCKS &
                                        HAS_FIREWORK_VIVI_BLOCKS),
                                       (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS),
                                       (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS)],
    "The Sky Is Falling Coin 4": [(HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "The Sky Is Falling Coin 5": [(HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS),
                                  (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                   HAS_STANDARD_BLOCK_LAUNCHERS)],
    "The Sky Is Falling Level Clear": [(HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                        HAS_STANDARD_BLOCK_LAUNCHERS),
                                       (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                        HAS_STANDARD_BLOCK_LAUNCHERS),
                                       (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                        HAS_STANDARD_BLOCK_LAUNCHERS),
                                       (HAS_GRAB_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                        HAS_STANDARD_BLOCK_LAUNCHERS)],
    #The Looking Glass
    "The Looking Glass Room 1 Secret Exit": [(None),
                                             (None),
                                             (None),
                                             (None)],
    "Universal Bearing Collectable Checkpoint 1": [(HAS_PIXIES & HAS_DOWN_GRAVITY_FLIPPERS &
                                                    HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                    HAS_FIREWORK_VIVI_BLOCKS & HAS_HONEY_BUBBLES &
                                                    HAS_GRAB_BLOCKS & HAS_BLUE_BALLOONS &
                                                    HAS_UP_GRAVITY_FLIPPERS),
                                                   (HAS_DOWN_GRAVITY_FLIPPERS & HAS_HIVE_BOMBS &
                                                    HAS_BLUE_HIVE_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                    HAS_HONEY_BUBBLES & HAS_GRAB_BLOCKS),
                                                   (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                    HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                                   (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                    HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS)],
    "Universal Bearing Collectible The Hive Door": [(HAS_PIXIES & HAS_DOWN_GRAVITY_FLIPPERS &
                                                     HAS_INVERTED_SEMISOLIDS & HAS_HIVE_BOMBS &
                                                     HAS_BLUE_HIVE_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                     HAS_HONEY_BUBBLES & HAS_GRAB_BLOCKS &
                                                     HAS_BLUE_BALLOONS & HAS_UP_GRAVITY_FLIPPERS &
                                                     HAS_TOGGLE_SEMISOLIDS & HAS_MOON_LAUNCHERS &
                                                     HAS_STANDARD_SEMISOLIDS),
                                                    (HAS_DOWN_GRAVITY_FLIPPERS & HAS_INVERTED_SEMISOLIDS &
                                                     HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                     HAS_FIREWORK_VIVI_BLOCKS & HAS_HONEY_BUBBLES &
                                                     HAS_GRAB_BLOCKS),
                                                    (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                     HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS),
                                                    (HAS_HIVE_BOMBS & HAS_BLUE_HIVE_BLOCKS &
                                                     HAS_FIREWORK_VIVI_BLOCKS & HAS_GRAB_BLOCKS)],
    "Universal Bearing Collectable Checkpoint 2": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                    HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                    HAS_YELLOW_SKULL_BLOCKS & HAS_YELLOW_BUMPERS &
                                                    HAS_BLUE_SKULL_RINGS & HAS_CLEAR_BUBBLES),
                                                   (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                    HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                    HAS_YELLOW_BUMPERS),
                                                   (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                    HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                    HAS_YELLOW_BUMPERS),
                                                   (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BUMPERS)],
    "Universal Bearing Collectible Nyctophobia Door": [(HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                        HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                        HAS_YELLOW_SKULL_BLOCKS & HAS_YELLOW_BUMPERS &
                                                        HAS_BLUE_SKULL_RINGS & HAS_CLEAR_BUBBLES &
                                                        HAS_GLASS_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                        HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS &
                                                        HAS_ORANGE_SKULL_BLOCKS),
                                                       (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                        HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                        HAS_YELLOW_BUMPERS & HAS_CLEAR_BUBBLES &
                                                        HAS_GLASS_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                        HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                                       (HAS_BLUE_SWITCHES & HAS_BLUE_PUNCHAPPEAR_BLOCKS &
                                                        HAS_BLUE_SKULL_BLOCKS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                                        HAS_YELLOW_BUMPERS & HAS_CLEAR_BUBBLES &
                                                        HAS_GLASS_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                        HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS),
                                                       (HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BUMPERS &
                                                        HAS_GLASS_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                        HAS_ORANGE_SWITCHES & HAS_ORANGE_PUNCHAPPEAR_BLOCKS)],
    "Universal Bearing Collectable Checkpoint 3": [(HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                    HAS_KEY_QUARTETS & HAS_TIMER_BUTTONS &
                                                    HAS_DIRECTIONAL_BUMPERS & HAS_MIRRORS &
                                                    HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS),
                                                   (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                    HAS_KEY_QUARTETS & HAS_TIMER_BUTTONS &
                                                    HAS_DIRECTIONAL_BUMPERS & HAS_MIRRORS &
                                                    HAS_TOGGLE_FLOWERS),
                                                   (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                    HAS_KEY_QUARTETS & HAS_DIRECTIONAL_BUMPERS &
                                                    HAS_MIRRORS & HAS_TOGGLE_FLOWERS),
                                                   (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                    HAS_KEY_QUARTETS & HAS_DIRECTIONAL_BUMPERS &
                                                    HAS_MIRRORS & HAS_TOGGLE_FLOWERS)],
    "Universal Bearing Collectible Various Explosives Door": [(HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                               HAS_KEY_QUARTETS & HAS_TIMER_BUTTONS &
                                                               HAS_DIRECTIONAL_BUMPERS & HAS_MIRRORS &
                                                               HAS_GREEN_BUBBLES & HAS_TOGGLE_FLOWERS &
                                                               HAS_ARROW_LIFTS & HAS_RED_BALLOONS),
                                                              (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                               HAS_KEY_QUARTETS & HAS_TIMER_BUTTONS &
                                                               HAS_DIRECTIONAL_BUMPERS & HAS_MIRRORS &
                                                               HAS_TOGGLE_FLOWERS & HAS_ARROW_LIFTS &
                                                               HAS_RED_BALLOONS),
                                                              (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                               HAS_KEY_QUARTETS & HAS_DIRECTIONAL_BUMPERS &
                                                               HAS_MIRRORS & HAS_TOGGLE_FLOWERS &
                                                               HAS_ARROW_LIFTS & HAS_RED_BALLOONS),
                                                              (HAS_BLUE_FIRE_RINGS & HAS_PEARL_BLOCK_LAUNCHERS &
                                                               HAS_KEY_QUARTETS & HAS_DIRECTIONAL_BUMPERS &
                                                               HAS_MIRRORS & HAS_TOGGLE_FLOWERS &
                                                               HAS_ARROW_LIFTS & HAS_RED_BALLOONS)],
    "Universal Bearing Collectable Checkpoint 4": [(HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                    HAS_STANDARD_SLIDING_BLOCKS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                                                   (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                    HAS_STANDARD_SLIDING_BLOCKS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                                                   (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                    HAS_STANDARD_PUNCHAPPEAR_BLOCKS),
                                                   (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                    HAS_STANDARD_PUNCHAPPEAR_BLOCKS)],
    "The Looking Glass Universal Bearing Collectible": [(HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                         HAS_STANDARD_SLIDING_BLOCKS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS &
                                                         HAS_STANDARD_BLOCK_LAUNCHERS),
                                                        (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                         HAS_STANDARD_SLIDING_BLOCKS & HAS_STANDARD_PUNCHAPPEAR_BLOCKS &
                                                         HAS_STANDARD_BLOCK_LAUNCHERS),
                                                        (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                         HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS),
                                                        (HAS_STANDARD_VIVI_BLOCKS & HAS_FIREWORK_VIVI_BLOCKS &
                                                         HAS_STANDARD_PUNCHAPPEAR_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS)],
    "The Looking Glass Room 1 Door": [(HAS_ELECTRIC_BLOCKS),
                                      (HAS_ELECTRIC_BLOCKS),
                                      (HAS_ELECTRIC_BLOCKS),
                                      (HAS_ELECTRIC_BLOCKS)],
    "The Looking Glass Coin 1": [(HAS_BLACK_HOLE_BUMPERS & HAS_ELECTRIC_BLOCKS),
                                 (HAS_BLACK_HOLE_BUMPERS & HAS_ELECTRIC_BLOCKS),
                                 (HAS_BLACK_HOLE_BUMPERS & HAS_ELECTRIC_BLOCKS),
                                 (HAS_BLACK_HOLE_BUMPERS & HAS_ELECTRIC_BLOCKS)],
    "The Looking Glass Room 2 Door": [(HAS_BLACK_HOLE_BUMPERS & HAS_ELECTRIC_BLOCKS),
                                      (HAS_BLACK_HOLE_BUMPERS),
                                      (HAS_BLACK_HOLE_BUMPERS),
                                      (HAS_BLACK_HOLE_BUMPERS)],
    "The Looking Glass Coin 2": [(HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS)],
    "The Looking Glass Coin 3": [(HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                  HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                  HAS_FIREWORK_VIVI_BLOCKS & HAS_LEAD_BALLOONS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                  HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                  HAS_FIREWORK_VIVI_BLOCKS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                  HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                  HAS_FIREWORK_VIVI_BLOCKS),
                                 (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                  HAS_STANDARD_BUMPERS & HAS_FIREWORK_VIVI_BLOCKS)],
    "The Looking Glass Room 3 Door": [(HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                       HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                       HAS_FIREWORK_VIVI_BLOCKS),
                                      (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                       HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                       HAS_FIREWORK_VIVI_BLOCKS),
                                      (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                       HAS_STANDARD_BUMPERS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                       HAS_FIREWORK_VIVI_BLOCKS),
                                      (HAS_MIRRORS & HAS_BLACK_HOLE_BUMPERS &
                                       HAS_STANDARD_BUMPERS & HAS_FIREWORK_VIVI_BLOCKS)],
    "The Looking Glass Coin 4": [(HAS_CRYSTAL_SLIDING_BLOCKS),
                                 (HAS_CRYSTAL_SLIDING_BLOCKS),
                                 (HAS_CRYSTAL_SLIDING_BLOCKS),
                                 (HAS_CRYSTAL_SLIDING_BLOCKS)],
    "The Looking Glass Room 4 Door": [(HAS_CRYSTAL_SLIDING_BLOCKS & HAS_MIRRORS),
                                      (HAS_CRYSTAL_SLIDING_BLOCKS & HAS_MIRRORS),
                                      (HAS_CRYSTAL_SLIDING_BLOCKS & HAS_MIRRORS),
                                      (HAS_CRYSTAL_SLIDING_BLOCKS & HAS_MIRRORS)],
    "The Looking Glass Checkpoint 1": [(HAS_MIRRORS & HAS_RED_BALLOONS &
                                        HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                        HAS_RED_PEARL_LAUNCHERS),
                                       (HAS_MIRRORS & HAS_RED_BALLOONS &
                                        HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                        HAS_RED_PEARL_LAUNCHERS),
                                       (HAS_MIRRORS & HAS_RED_BALLOONS &
                                        HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                        HAS_RED_PEARL_LAUNCHERS),
                                       (HAS_MIRRORS & HAS_RED_BALLOONS &
                                        HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                        HAS_RED_PEARL_LAUNCHERS)],
    "The Looking Glass Level Clear": [(HAS_MIRRORS & HAS_RED_BALLOONS &
                                       HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                       HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                                       HAS_PEARL_BLOCK_LAUNCHERS & HAS_YELLOW_VIVI_BLOCKS &
                                       HAS_STANDARD_POP_BLOCKS & HAS_MOON_LAUNCHERS &
                                       HAS_BLUE_CRYSTAL_LAUNCHERS & HAS_STANDARD_SLIDING_BLOCKS &
                                       HAS_CLEAR_BUBBLES),
                                      (HAS_MIRRORS & HAS_RED_BALLOONS &
                                       HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                       HAS_RED_PEARL_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                                       HAS_PEARL_BLOCK_LAUNCHERS & HAS_YELLOW_VIVI_BLOCKS &
                                       HAS_STANDARD_POP_BLOCKS & HAS_MOON_LAUNCHERS &
                                       HAS_BLUE_CRYSTAL_LAUNCHERS & HAS_STANDARD_SLIDING_BLOCKS &
                                       HAS_CLEAR_BUBBLES),
                                      (HAS_MIRRORS & HAS_RED_BALLOONS &
                                       HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                       HAS_RED_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS &
                                       HAS_YELLOW_VIVI_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                       HAS_MOON_LAUNCHERS & HAS_BLUE_CRYSTAL_LAUNCHERS &
                                       HAS_STANDARD_SLIDING_BLOCKS & HAS_CLEAR_BUBBLES),
                                      (HAS_MIRRORS & HAS_RED_BALLOONS &
                                       HAS_BLUE_BALLOONS & HAS_GREEN_BUBBLES &
                                       HAS_RED_PEARL_LAUNCHERS & HAS_PEARL_BLOCK_LAUNCHERS &
                                       HAS_YELLOW_VIVI_BLOCKS & HAS_STANDARD_POP_BLOCKS &
                                       HAS_MOON_LAUNCHERS & HAS_BLUE_CRYSTAL_LAUNCHERS &
                                       HAS_STANDARD_SLIDING_BLOCKS & HAS_CLEAR_BUBBLES)],
    #Galactic Central Point
    "Galactic Central Point Room 1 Door": [(HAS_GALACTIC_BLOCK_LAUNCHERS),
                                           (HAS_GALACTIC_BLOCK_LAUNCHERS),
                                           (HAS_GALACTIC_BLOCK_LAUNCHERS),
                                           (HAS_GALACTIC_BLOCK_LAUNCHERS)],
    "Galactic Central Point Room 2 Door": [(HAS_GALACTIC_SLIDING_BLOCKS),
                                           (HAS_GALACTIC_SLIDING_BLOCKS),
                                           (HAS_GALACTIC_SLIDING_BLOCKS),
                                           (HAS_GALACTIC_SLIDING_BLOCKS)],
    "Galactic Central Point Room 3 Door": [(HAS_GALACTIC_POP_BLOCKS),
                                           (HAS_GALACTIC_POP_BLOCKS),
                                           (HAS_GALACTIC_POP_BLOCKS),
                                           (None)],
    "Galactic Central Point Heart 32": [(HAS_HIVE_BOMBS),
                                        (HAS_HIVE_BOMBS),
                                        (HAS_HIVE_BOMBS),
                                        (HAS_HIVE_BOMBS)],
    "Galactic Central Point Checkpoint 1": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                             HAS_GREEN_BUBBLES),
                                            (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                             HAS_GREEN_BUBBLES),
                                            (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES),
                                            (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES)],
    "Galactic Central Point Heart 49": [(HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                         HAS_GREEN_BUBBLES & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                         HAS_YELLOW_SKULL_BLOCKS & HAS_CLEAR_BUBBLES &
                                         HAS_BARRELS),
                                        (HAS_ON_OFF_BLOCKS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                         HAS_GREEN_BUBBLES & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                         HAS_YELLOW_SKULL_BLOCKS & HAS_CLEAR_BUBBLES &
                                         HAS_BARRELS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES &
                                         HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                         HAS_CLEAR_BUBBLES & HAS_BARRELS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES &
                                         HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                         HAS_CLEAR_BUBBLES & HAS_BARRELS)],
    "Galactic Central Point Heart 37": [(HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS &
                                         HAS_TOGGLE_SEMISOLIDS & HAS_RED_PEARL_LAUNCHERS &
                                         HAS_GREEN_BUBBLES & HAS_RED_BALLOONS &
                                         HAS_ON_OFF_BLOCKS & HAS_SLIDING_HEART_BLOCKS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS &
                                         HAS_TOGGLE_SEMISOLIDS & HAS_RED_BALLOONS &
                                         HAS_SLIDING_HEART_BLOCKS),
                                        (HAS_STANDARD_BLOCK_LAUNCHERS & HAS_STANDARD_SPINNERS & (
                                         HAS_TOGGLE_SEMISOLIDS | HAS_RED_PEARL_LAUNCHERS) &
                                         HAS_RED_BALLOONS & HAS_SLIDING_HEART_BLOCKS),
                                        (HAS_STANDARD_SPINNERS & (HAS_TOGGLE_SEMISOLIDS |
                                         HAS_RED_PEARL_LAUNCHERS) & HAS_RED_BALLOONS &
                                         HAS_SLIDING_HEART_BLOCKS)],
    "Galactic Central Point Level Clear": [(HAS_HIVE_BOMBS & HAS_ON_OFF_BLOCKS &
                                            HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES &
                                            HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                            HAS_CLEAR_BUBBLES & HAS_BARRELS &
                                            HAS_STANDARD_SPINNERS & HAS_TOGGLE_SEMISOLIDS &
                                            HAS_RED_PEARL_LAUNCHERS & HAS_RED_BALLOONS &
                                            HAS_SLIDING_HEART_BLOCKS),
                                           (HAS_HIVE_BOMBS & HAS_ON_OFF_BLOCKS &
                                            HAS_STANDARD_BLOCK_LAUNCHERS & HAS_GREEN_BUBBLES &
                                            HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_SKULL_BLOCKS &
                                            HAS_CLEAR_BUBBLES & HAS_BARRELS &
                                            HAS_STANDARD_SPINNERS & HAS_TOGGLE_SEMISOLIDS &
                                            HAS_RED_BALLOONS & HAS_SLIDING_HEART_BLOCKS),
                                           (HAS_HIVE_BOMBS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                            HAS_GREEN_BUBBLES & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                            HAS_YELLOW_SKULL_BLOCKS & HAS_CLEAR_BUBBLES &
                                            HAS_BARRELS & HAS_STANDARD_SPINNERS & (
                                            HAS_TOGGLE_SEMISOLIDS | HAS_RED_PEARL_LAUNCHERS) &
                                            HAS_RED_BALLOONS & HAS_SLIDING_HEART_BLOCKS),
                                           (HAS_HIVE_BOMBS & HAS_STANDARD_BLOCK_LAUNCHERS &
                                            HAS_GREEN_BUBBLES & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                                            HAS_YELLOW_SKULL_BLOCKS & HAS_CLEAR_BUBBLES &
                                            HAS_BARRELS & HAS_STANDARD_SPINNERS & (
                                            HAS_TOGGLE_SEMISOLIDS | HAS_RED_PEARL_LAUNCHERS) &
                                            HAS_RED_BALLOONS & HAS_SLIDING_HEART_BLOCKS)],
    #Home
    "Home Room 1 Door": [(None),
                         (None),
                         (None),
                         (None)],
    "Home Checkpoint 1": [(HAS_PILLARS),
                          (HAS_PILLARS),
                          (HAS_PILLARS),
                          (HAS_PILLARS)],
    "Home Checkpoint 2": [(HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS),
                          (HAS_PILLARS)],
    "Home Checkpoint 3": [(HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS),
                          (HAS_PILLARS & HAS_LINE_BLOCKS)],
    "Home Checkpoint 4": [(HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                           HAS_STANDARD_BLOCK_LAUNCHERS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                           HAS_STANDARD_BLOCK_LAUNCHERS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS),
                          (HAS_PILLARS & HAS_LINE_BLOCKS)],
    "Home Checkpoint 5": [(HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                           HAS_STANDARD_BLOCK_LAUNCHERS & HAS_YELLOW_SPIN_BLOCKS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                           HAS_STANDARD_BLOCK_LAUNCHERS),
                          (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                           HAS_LINE_BLOCKS),
                          (HAS_PILLARS & HAS_LINE_BLOCKS)],
    "Home Room 2 Door": [(HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                          HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                          HAS_STANDARD_BLOCK_LAUNCHERS & HAS_YELLOW_SPIN_BLOCKS &
                          HAS_TREES),
                         (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                          HAS_LINE_BLOCKS & HAS_ELECTRIC_BLOCKS &
                          HAS_STANDARD_BLOCK_LAUNCHERS & HAS_TREES),
                         (HAS_PILLARS & HAS_FIRE_BLOCK_LAUNCHERS &
                          HAS_LINE_BLOCKS & HAS_TREES),
                         (HAS_PILLARS & HAS_LINE_BLOCKS)],
    "Home Checkpoint 6": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS)],
    "Home Checkpoint 7": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_LEAD_BALLOONS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS)],
    "Home Checkpoint 8": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_LEAD_BALLOONS &
                           HAS_TOGGLE_FLOWERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS)],
    "Home Room 3 Door": [(HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_LEAD_BALLOONS &
                           HAS_TOGGLE_FLOWERS & HAS_YELLOW_PUNCHAPPEAR_BLOCKS &
                          HAS_YELLOW_BLOCK_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS &
                           HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BLOCK_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS &
                           HAS_YELLOW_PUNCHAPPEAR_BLOCKS & HAS_YELLOW_BLOCK_LAUNCHERS),
                          (HAS_PEARL_BLOCK_LAUNCHERS & HAS_BLUE_PEARL_LAUNCHERS &
                           HAS_FIREWORK_VIVI_BLOCKS & HAS_TOGGLE_FLOWERS)],
    "Home Room 4 Door": [(None),
                         (None),
                         (None),
                         (None)],
    "Home Room 5 Door": [(HAS_TETHERS & HAS_GUBES),
                         (HAS_GUBES),
                         (HAS_GUBES),
                         (HAS_GUBES)],
    "Home Level Clear": [(None),
                         (None),
                         (None),
                         (None)],
    "Coyote Time Tutorial Complete": [(None),
                                      (None),
                                      (None),
                                      (None)],
    "Box Boosting Tutorial Complete": [(HAS_STANDARD_PHYSICS_BLOCKS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS),
                                       (HAS_STANDARD_PHYSICS_BLOCKS),
                                       (None)],
    "Fast Falling Tutorial Complete": [(HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS),
                                       (HAS_TIMER_BUTTONS)],
    "Steep Slope Kicks Tutorial Complete": [(None),
                                            (None),
                                            (None),
                                            (None)],
    "Bubble Jumps Tutorial Complete": [(HAS_GREEN_BUBBLES),
                                       (HAS_GREEN_BUBBLES),
                                       (HAS_GREEN_BUBBLES),
                                       (HAS_GREEN_BUBBLES)],
    "Fireworks Tutorial Complete": [(HAS_FIREWORK_VIVI_BLOCKS),
                                    (HAS_FIREWORK_VIVI_BLOCKS),
                                    (HAS_FIREWORK_VIVI_BLOCKS),
                                    (HAS_FIREWORK_VIVI_BLOCKS)],
}

# Vanilla/Randomized
STANDARD_ENTRANCE_REQUIREMENTS = {
    ("1-1", "1-2"): Has("1-1 Standard Exit Path"),
    ("1-2", "1-3"): Has("1-2 Standard Exit Path"),
    ("1-3", "1-4"): Has("1-3 Standard Exit Path"),
    ("1-4", "1-5"): Has("1-4 Standard Exit Path"),
    ("1-5", "1-6"): Has("1-5 Standard Exit Path"),
    ("1-6", "1-7"): Has("1-6 Standard Exit Path"),
    ("1-7", "1-8"): Has("1-7 Standard Exit Path"),
    ("2-1", "2-2"): Has("2-1 Standard Exit Path"),
    ("2-2", "2-3"): Has("2-2 Standard Exit Path"),
    ("2-3", "2-4"): Has("2-3 Standard Exit Path"),
    ("2-4", "2-5"): Has("2-4 Standard Exit Path"),
    ("2-5", "2-6"): Has("2-5 Standard Exit Path"),
    ("3-1", "3-2"): Has("3-1 Standard Exit Path"),
    ("3-2", "3-3"): Has("3-2 Standard Exit Path"),
    ("3-3", "3-4"): Has("3-3 Standard Exit Path"),
    ("3-4", "3-5"): Has("3-4 Standard Exit Path"),
    ("3-5", "3-6"): Has("3-5 Standard Exit Path"),
    ("3-6", "3-7"): Has("3-6 Standard Exit Path"),
    ("4-1", "4-2"): Has("4-1 Standard Exit Path"),
    ("4-2", "4-3"): Has("4-2 Standard Exit Path"),
    ("4-3", "4-4"): Has("4-3 Standard Exit Path"),
    ("4-4", "4-5"): Has("4-4 Standard Exit Path"),
    ("4-5", "4-6"): Has("4-5 Standard Exit Path"),
    ("4-6", "4-7"): Has("4-6 Standard Exit Path"),
    ("4-7", "4-8"): Has("4-7 Standard Exit Path"),
    ("4-8", "4-9"): Has("4-8 Standard Exit Path"),
    ("5-1", "5-2"): Has("5-1 Standard Exit Path"),
    ("5-2", "5-3"): Has("5-2 Standard Exit Path"),
    ("5-3", "5-4"): Has("5-3 Standard Exit Path"),

    ("1-2", "1-A"): Has("1-2 Secret Exit Path"),
    ("1-4", "1-C"): Has("1-4 Secret Exit Path"),
    ("2-1", "2-A"): Has("2-1 Secret Exit Path"),
    ("2-C", "2-D"): Has("2-C Secret Exit Path"),
    ("3-1", "3-A"): Has("3-1 Secret Exit Path"),
    ("4-1", "4-A"): Has("4-1 Secret Exit Path"),

    ("1-A", "1-B"): Has("1-A Standard Exit Path"),
    ("1-B", "1-5"): Has("1-B Standard Exit Path"),
    ("1-C", "1-7"): Has("1-C Standard Exit Path"),
    ("2-A", "2-B"): Has("2-A Standard Exit Path"),
    ("2-B", "2-C"): Has("2-B Standard Exit Path"),
    ("2-C", "2-5"): Has("2-C Standard Exit Path"),
    ("3-A", "3-B"): Has("3-A Standard Exit Path"),
    ("3-B", "3-4"): Has("3-B Standard Exit Path"),
    ("4-A", "4-5"): Has("4-A Standard Exit Path"),

    ("1-8", "2-1"): Has("1-8 Boss Exit Path"),
    ("2-6", "3-1"): Has("2-6 Boss Exit Path"),
    ("3-7", "4-1"): Has("3-7 Boss Exit Path"),
    ("4-9", "5-1"): Has("4-9 Boss Exit Path"),

    ("2-D", "3-7"): Has("2-D Standard Exit Path"),

    ("1-1", "1-0"): Has("1-1 Home Exit Path")
}

PROGRESSIVE_CLOSED_STANDARD_PATHS = {
    ("1-1", "1-2"): 1,
    ("1-2", "1-3"): 2,
    ("1-3", "1-4"): 3,
    ("1-4", "1-5"): 4,
    ("1-5", "1-6"): 5,
    ("1-6", "1-7"): 6,
    ("1-7", "1-8"): 7,
    ("2-1", "2-2"): 9,
    ("2-2", "2-3"): 10,
    ("2-3", "2-4"): 11,
    ("2-4", "2-5"): 12,
    ("2-5", "2-6"): 13,
    ("3-1", "3-2"): 15,
    ("3-2", "3-3"): 16,
    ("3-3", "3-4"): 17,
    ("3-4", "3-5"): 18,
    ("3-5", "3-6"): 19,
    ("3-6", "3-7"): 20,
    ("4-1", "4-2"): 22,
    ("4-2", "4-3"): 23,
    ("4-3", "4-4"): 24,
    ("4-4", "4-5"): 25,
    ("4-5", "4-6"): 26,
    ("4-6", "4-7"): 27,
    ("4-7", "4-8"): 28,
    ("4-8", "4-9"): 29,
    ("5-1", "5-2"): 31,
    ("5-2", "5-3"): 32,
    ("5-3", "5-4"): 33,

    ("1-8", "2-1"): 8,
    ("2-6", "3-1"): 14,
    ("3-7", "4-1"): 21,
    ("4-9", "5-1"): 30,
}

PROGRESSIVE_CLOSED_SECRET_PATHS = {
    ("1-2", "1-A"): 2,
    ("1-4", "1-C"): 5,
    ("2-1", "2-A"): 7,
    ("2-C", "2-D"): 11,
    ("3-1", "3-A"): 13,
    ("4-1", "4-A"): 16,

    ("1-A", "1-B"): 3,
    ("1-B", "1-5"): 4,
    ("1-C", "1-7"): 6,
    ("2-A", "2-B"): 8,
    ("2-B", "2-C"): 9,
    ("2-C", "2-5"): 10,
    ("3-A", "3-B"): 14,
    ("3-B", "3-4"): 15,
    ("4-A", "4-5"): 17,

    ("2-D", "3-7"): 12,
}

PROGRESSIVE_PARTIAL_STANDARD_PATHS = {
    ("1-8", "2-1"): 1,
    ("2-6", "3-1"): 2,
    ("3-7", "4-1"): 3,
    ("4-9", "5-1"): 4,
}

PROGRESSIVE_PARTIAL_SECRET_PATHS = {
    ("1-2", "1-A"): 2,
    ("1-4", "1-C"): 5,
    ("2-1", "2-A"): 7,
    ("2-C", "2-D"): 11,
    ("3-1", "3-A"): 13,
    ("4-1", "4-A"): 16,

    ("1-A", "1-B"): 3,
    ("1-B", "1-5"): 4,
    ("1-C", "1-7"): 6,
    ("2-A", "2-B"): 8,
    ("2-B", "2-C"): 9,
    ("2-C", "2-5"): 10,
    ("3-A", "3-B"): 14,
    ("3-B", "3-4"): 15,
    ("4-A", "4-5"): 17,

    ("2-D", "3-7"): 12,
}

PROGRESSIVE_OPEN_STANDARD_PATHS = {
    ("1-8", "2-1"): 1,
    ("2-6", "3-1"): 2,
    ("3-7", "4-1"): 3,
    ("4-9", "5-1"): 4,
}

PROGRESSIVE_OPEN_SECRET_PATHS = {
    ("2-D", "3-7"): 1,
}

def set_all_rules(world: FantasticFistWorld):
    for item_requirement in ITEM_REQUIREMENTS:

        rule: Rule = ITEM_REQUIREMENTS[item_requirement][world.options.difficulty]

        if rule is None:
            continue

        if world.location_names.__contains__(item_requirement):

            location_id: int = world.location_name_to_id[item_requirement]
            if (not world.options.checkpointsanity) & (location_id >= 900) & (location_id < 942):
                #If checkpointsanity is off, don't add rules for checkpoints.
                continue

            location: Location = world.get_location(item_requirement)

            world.set_rule(location, rule)
        else:
            entrance: Entrance = world.get_entrance(item_requirement)
            world.set_rule(entrance, rule)

    victory_location: str = ""
    if world.options.goal == 0:
        victory_location = "Galactic Central Point Level Clear"
    elif world.options.goal == 1:
        victory_location = "The Looking Glass Universal Bearing Collectible"
    elif world.options.goal == 2:
        victory_location = "Home Level Clear"

    victory_rule: Rule = ITEM_REQUIREMENTS[victory_location][world.options.difficulty]

    if victory_rule is not None:
        world.set_rule(world.get_location("Victory"), victory_rule)

    world.set_completion_rule(Has("Victory"))

    if world.options.paths == 0 or world.options.paths == 1:
        for entrance_requirement in STANDARD_ENTRANCE_REQUIREMENTS:
            start: str = entrance_requirement[0]
            end: str = entrance_requirement[1]

            world.set_rule(world.get_entrance(start + " to " + end), STANDARD_ENTRANCE_REQUIREMENTS[entrance_requirement])
            world.set_rule(world.get_entrance(end + " to " + start), STANDARD_ENTRANCE_REQUIREMENTS[entrance_requirement])

    elif world.options.paths == 2:
        if world.options.open_world == 0:
            set_progressive_path_rules(world, PROGRESSIVE_CLOSED_STANDARD_PATHS, False, 0)

            home_rule: Rule

            if world.options.goal == 2:
                set_progressive_path_rules(world, PROGRESSIVE_CLOSED_SECRET_PATHS, True, -1)
                home_rule = STANDARD_ENTRANCE_REQUIREMENTS[("1-1", "1-0")]
            else:
                set_progressive_path_rules(world, PROGRESSIVE_CLOSED_SECRET_PATHS, True, 0)
                home_rule = Has("Progressive Secret Path", count = 1)

            world.set_rule(world.get_entrance("1-1 to 1-0"), home_rule)
            world.set_rule(world.get_entrance("1-0 to 1-1"), home_rule)

        elif world.options.open_world == 1:
            set_progressive_path_rules(world, PROGRESSIVE_PARTIAL_STANDARD_PATHS, False, 0)

            home_rule: Rule

            if world.options.goal == 2:
                set_progressive_path_rules(world, PROGRESSIVE_PARTIAL_SECRET_PATHS, True, -1)
                home_rule = STANDARD_ENTRANCE_REQUIREMENTS[("1-1", "1-0")]
            else:
                set_progressive_path_rules(world, PROGRESSIVE_PARTIAL_SECRET_PATHS, True, 0)
                home_rule = Has("Progressive Secret Path", count=1)

            world.set_rule(world.get_entrance("1-1 to 1-0"), home_rule)
            world.set_rule(world.get_entrance("1-0 to 1-1"), home_rule)

        elif world.options.open_world == 2:
            set_progressive_path_rules(world, PROGRESSIVE_OPEN_STANDARD_PATHS, False, 0)
            set_progressive_path_rules(world, PROGRESSIVE_OPEN_SECRET_PATHS, True, 0)

            home_rule: Rule

            if world.options.goal == 2:
                home_rule = STANDARD_ENTRANCE_REQUIREMENTS[("1-1", "1-0")]
                world.set_rule(world.get_entrance("1-1 to 1-0"), home_rule)
                world.set_rule(world.get_entrance("1-0 to 1-1"), home_rule)

        elif world.options.open_world == 3:
            if world.options.goal == 2:
                home_rule = STANDARD_ENTRANCE_REQUIREMENTS[("1-1", "1-0")]
                world.set_rule(world.get_entrance("1-1 to 1-0"), home_rule)
                world.set_rule(world.get_entrance("1-0 to 1-1"), home_rule)

    current_secret_index: int = 0
    for level in regions.ID_TO_LEVEL:
        current_room = regions.get_edge_from_start_node_name(world.randomized_entrances, regions.ID_TO_LEVEL[level].level_id)[0].end_node
        next_rooms: list[regions.Node] = []
        while current_room is not None:
            if current_room.node_name == "The Caves Room 2":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("The Caves Load Bearing Collectible"), ITEM_REQUIREMENTS["The Caves Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(0)
                current_secret_index += 1
            elif current_room.node_name == "Verticality Room 2":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("Verticality Load Bearing Collectible"), ITEM_REQUIREMENTS["Verticality Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(1)
                current_secret_index += 1
            elif current_room.node_name == "Midnight Grove Room 4":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("Midnight Grove Load Bearing Collectible"), ITEM_REQUIREMENTS["Midnight Grove Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(2)
                current_secret_index += 1
            elif current_room.node_name == "Forgotten Archives Room 4":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("Forgotten Archives Load Bearing Collectible"), ITEM_REQUIREMENTS["Forgotten Archives Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(3)
                current_secret_index += 1
            elif current_room.node_name == "The Timeless Temple Room 3":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("The Timeless Temple Load Bearing Collectible"), ITEM_REQUIREMENTS["The Timeless Temple Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(4)
                current_secret_index += 1
            elif current_room.node_name == "Infinity Garden Room 3":
                if world.secret_coin_requirements[current_secret_index] != 0:
                    world.set_rule(world.get_location("Infinity Garden Load Bearing Collectible"), ITEM_REQUIREMENTS["Infinity Garden Load Bearing Collectible"][world.options.difficulty] & Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
                world.secret_exit_room_order.append(5)
                current_secret_index += 1

            for edge in regions.get_edge_from_start_node_name(world.randomized_doors, current_room.node_name):
                if not next_rooms.__contains__(edge.end_node):
                    next_rooms.append(edge.end_node)

            if len(next_rooms) == 0:
                current_room = None
            else:
                current_room = next_rooms[0]
                next_rooms.remove(current_room)

    if world.secret_coin_requirements[current_secret_index] != 0:
        world.set_rule(world.get_entrance("The Looking Glass Room 1 Secret Exit"), Has("Coin", count = world.secret_coin_requirements[current_secret_index]))
    world.secret_exit_room_order.append(6)

    if world.boss_coin_requirements[0] != 0:
        world.set_rule(world.get_entrance("1-8 Entrance"), Has("Coin", count = world.boss_coin_requirements[0]))
    if world.boss_coin_requirements[1] != 0:
        world.set_rule(world.get_entrance("2-6 Entrance"), Has("Coin", count = world.boss_coin_requirements[1]))
    if world.boss_coin_requirements[2] != 0:
        world.set_rule(world.get_entrance("3-7 Entrance"), Has("Coin", count = world.boss_coin_requirements[2]))
    if world.boss_coin_requirements[3] != 0:
        world.set_rule(world.get_entrance("4-9 Entrance"), Has("Coin", count = world.boss_coin_requirements[3]))
    if world.boss_coin_requirements[4] != 0:
        world.set_rule(world.get_entrance("5-4 Entrance"), Has("Coin", count = world.boss_coin_requirements[4]))


def set_progressive_path_rules(world: FantasticFistWorld, path_list: dict[tuple[str, str], int], is_secret: bool, modifier: int):
    for path in path_list:
        start: str = path[0]
        end: str = path[1]

        path_type: str = ""
        if is_secret:
            path_type = "Progressive Secret Path"
        else:
            path_type = "Progressive Standard Path"

        path_amt: int = path_list[path] + modifier

        rule: Rule = Has(path_type, count = path_amt)

        world.set_rule(world.get_entrance(start + " to " + end), rule)
        world.set_rule(world.get_entrance(end + " to " + start), rule)