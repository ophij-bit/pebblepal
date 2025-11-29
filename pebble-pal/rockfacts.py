# Description:  This module pertains to geological information.
#               This modules import reference in Pebble Pal is 'rf'.
# Contents:     > Reference links for geological information
#               > Unit strings for mass, volume, and density values.
#               > Mineral Hardness goalpost values
#               > Facts/blurbs about common rocks and minerals
#               > Density value for water
#               > Lists of common rock/mineral names
#               > Lists of common rock/mineral density range lows and highs
#               > Function to compare a given density value to ranges of 
#                 common rocks and minerals, and store the indices of the 
#                 matches in a new list
#               > Function to print common rocks/minerals with matching 
#                 density ranges given a list of indices
#*****************************************************************************

# Igneous rocks ref: https://scontent.fhio3-1.fna.fbcdn.net/v/t39.30808-6/473439567_595861290008130_8703317653298180077_n.jpg?stp=dst-jpg_p526x296_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=enqMqJy5mD0Q7kNvwHLL31g&_nc_oc=AdlC7at_xVWRFALSqGGocDHpHOhmfInecR_T-CeqZX8xgJmhLw2AiJOBSRBa85SdZAA&_nc_zt=23&_nc_ht=scontent.fhio3-1.fna&_nc_gid=NnjV2h9V2pVZqcYMK1iT4w&oh=00_AfjY4wAtEL4sVU8CxvvzWDYuHiEXRmG07HiD5ni4HdCzww&oe=691AB073
# Common densities ref: https://www.thoughtco.com/densities-of-common-rocks-and-minerals-1439119

# Unit Strings
UNIT_MASS = "g"
UNIT_VOLUME = "cm\u00b3"
UNIT_DENSITY = "g/cm\u00b3"

# Mineral Hardness Goalposts
SOFT = 2.5
MEDIUM = 5.5
HARD = 10

# Rock Facts
UNKNOWN_FACT = "More data is needed."
GRANITE_FACT = ("Granite is an intrusive rock common to the PNW, often "
                "featuring large visible grains.")
DIORITE_FACT = ("Diorite may be mistaken for Granite, but features a higher "
                "ratio of mafic components.")
GABBRO_FACT = "Gabbro is Basalt's intrusive counterpart."
RHYOLITE_FACT = "Something about Rhyolite."
ANDESITE_FACT = ("Andesite is an extrusive rock, "
                "named after the Andes mountain range.")
BASALT_FACT = "Basalt is an extrusive igneous rock common to the PNW."
PUMICE_FACT = ("Pumice is a vesicular rock (full of air pockets!) that forms "
              " during explosive eruptions, and is felsic in composition. "
              "Pumice floats in water!")
SCORIA_FACT = ("Scoria is a vesicular rock (full of air pockets!) that forms "
              "during explosive eruptions, and is mafic in composition. "
              "Unlike Pumice, Scoria will sink in water.")
OBSIDIAN_FACT = ("Obsidian is a volcanic glass. Though very dark, "
                 "it is actually felsic.")
PORPHYRITIC_FACT = (f"\nPorphyritic rocks exhibit crystals embedded in fine "
                    "grained rock. This is due to initial slow cooling followed "
                    "by explosive eruption.")
VESICULAR_FACT = ("If your sample is not clearly light (Pumice) or clearly "
                  "dark (Scoria) then it could be vesicular Andesite, or "
                  "another vesicular igneous rock.")
GRAPHITE_FACT = ("Graphite is a very soft mineral, composed solely of carbon. "
                 "Diamonds are also composed only of carbon but are the "
                 "hardest minerals! The difference lies in the type of "
                 "bonding present between carbon atoms. Graphite is also "
                 "used for pencil lead!")
FLUORITE_FACT = ("Fluorite comes in many colors and its crystal habit "
                 "resembles an 8-sided die!")


#Density lists & values
WATER_DENSITY = 1.0

D_NAMES = [
  "Ice",
  "Pumice",
  "Coal",
  "Halite",
  "Gypsum",
  "Limestone",
  "Sandstone",
  "Shale",
  "Quartz",
  "Granite",
  "Rhyolite",
  "Andesite",
  "Diorite",
  "Basalt",
  "Gabbro",
  "Peridotite",
  "Kaolinite",
  "Calcite",
  "Dolomite",
  "Hornblende",
  "Biotite Mica",
  "Mica Schist",
  "Slate",
  "Quartzite",
  "Gneiss",
  "Talc",
  "Fluorite",
  "Pyrite",
  "Magnetite",
  "Hematite",
  "Copper",
  "Silver",
  "Gold",
  "Iridium"
]

D_LOWS = [
  0.917,  # Ice
  0.40,   # Pumice
  1.10,   # Coal
  2.10,   # Halite
  2.30,   # Gypsum
  2.30,   # Limestone
  2.20,   # Sandstone
  2.40,   # Shale
  2.60,   # Quartz
  2.60,   # Granite
  2.40,   # Rhyolite
  2.50,   # Andesite
  2.80,   # Diorite
  2.80,   # Basalt
  2.70,   # Gabbro
  3.10,   # Peridotite
  2.60,   # Kaolinite
  2.71,   # Calcite
  2.80,   # Dolomite
  3.00,   # Hornblende
  2.80,   # Biotite Mica
  2.70,   # Mica Schist
  2.70,   # Slate
  2.60,   # Quartzite
  2.70,   # Gneiss
  2.70,   # Talc
  3.00,   # Fluorite
  4.90,   # Pyrite
  5.17,   # Magnetite
  4.90,   # Hematite
  8.90,   # Copper
  10.30,  # Silver
  19.30,  # Gold
  22.40   # Iridium
]

D_HIGHS = [
  0.917,  # Ice
  0.70,   # Pumice
  1.40,   # Coal
  2.20,   # Halite
  2.40,   # Gypsum
  2.70,   # Limestone
  2.80,   # Sandstone
  2.70,   # Shale
  2.65,   # Quartz
  2.75,   # Granite
  2.60,   # Rhyolite
  2.80,   # Andesite
  3.00,   # Diorite
  3.10,   # Basalt
  3.30,   # Gabbro
  3.40,   # Peridotite
  2.65,   # Kaolinite
  2.75,   # Calcite
  2.90,   # Dolomite
  3.40,   # Hornblende
  3.10,   # Biotite Mica
  2.90,   # Mica Schist
  2.90,   # Slate
  2.70,   # Quartzite
  2.90,   # Gneiss
  2.90,   # Talc
  3.30,   # Fluorite
  5.20,   # Pyrite
  5.18,   # Magnetite
  5.30,   # Hematite
  8.90,   # Copper
  10.50,  # Silver
  19.30,  # Gold
  22.40   # Iridium
]


def check_density(d):
  """
  Compares a given density value to known density ranges of common rocks
  and minerals. Returns a list of indices for all ranges that include
  the provided value.
  :param d: density value to compare, float
  :return dens_list: list of indices of matching density ranges, list[int]
  """

  i = 0
  dens_list = []
  while i < len(D_NAMES):
    if d >= D_LOWS[i] and d <= D_HIGHS[i]:
      dens_list.append(i)
    i += 1
  return dens_list


def print_dens_list(dens_list):
  """
  Prints a formatted list of rock and mineral types whose density ranges
  match the provided index list. For each index, displays the name and
  its associated density range.
  :param dens_list: list of indices referencing density-range lists, list[int]
  :return: none
  """

  i = 0
  if dens_list:
    print(f"> Common rocks and minerals in this range include:\n")
    while i < len(dens_list):
      print(f">> {D_NAMES[dens_list[i]]} ",end="")
      if D_LOWS[dens_list[i]] != D_HIGHS[dens_list[i]]:
        print(f"({D_LOWS[dens_list[i]]}-{D_HIGHS[dens_list[i]]}",end="")
      else:
        print(f"({D_LOWS[dens_list[i]]}",end="")
      print(f"{UNIT_DENSITY})")
      i += 1