# Description:  This module pertains to menu generation, options sets,
#               and option retrieval and validation. 
#               This modules import reference in Pebble Pal is 'm'.
# Contents:     > Formatting elements
#               > List of menu titles
#               > Lists for each option set content and related constants
#               > List of option sets and respective 'mi' or menu index
#               > Function to print formatted menu with title and options
#               > Funciton to retrive and validate an option selection
#*****************************************************************************

# Formatting Elements
DIV_CHAR = "-"
DIV_LEN = 48
DIVIDER = DIV_CHAR * DIV_LEN

# Menu Titles
titles = ["Main Menu", 
          "Select Sample Type", 
          "Select Luster",
          "Select Color Range",
          "Selcet Streak Color",
          "Select Texture",
          "Select Mafic Color Index",]

# Main Menu Options
main_opts = ["1. Analyze Sample",
            "2. Display Sample Log",
            "3. Density Calculator",
            "4. Display Density Log",
            "5. Quit"]
ANALYZE = 1
DISPLAY_ANALYSIS = 2
DENSITY = 3
DISPLAY_DENSITIES = 4
QUIT = 5

# Sample Type Options
type_opts = ["1. Mineral", 
              "2. Igneous Rock",
              "3. Sedimentary Rock", 
              "4. Metamorphic Rock",
              "5. Unknown"]
MINERAL = 1
IGNEOUS = 2
SEDIMENTARY = 3
METAMORPHIC = 4
UNKNOWN = 5

# Mineral Luster Options
luster_opts = ["1. Metallic",
                "2. Non-Metallic"]
METALLIC = 1
NON_METALLIC = 2

# Mineral Color Options
color_opts = ["1. Light (Clear, White, Light Gray, etc.)", 
              "2. Dark (Dark Gray, Black, etc.)", 
              "3. Distinct Color(Green, Yellow, Pink, etc.)"]
LIGHT = 1
DARK = 2
COLORED = 3

# Mineral Streak Options
streak_opts = ["1. Rust-Red", 
                "2. Green-Black",
                "3. Dark (Gray, Black, etc.)",
                "4. Light (White, Pale, Colorless)"]
RED_STREAK = 1
GREEN_STREAK = 2
DARK_STREAK = 3
LIGHT_STREAK = 4

# Igneous Texture Options
texture_opts = ["1. Coarse Grain (Phaneritic)",
                "2. Fine Grain (Aphanitic)",
                "3. Both (Porphyritic)", 
                "4. Pocketed (Vesicular)", 
                "5. Glassy"]
COARSE = 1
FINE = 2
BOTH = 3
VESICULAR = 4
GLASSY = 5

# Igneous Mafic Color Index
mci_opts = ["1. Felsic (Mostly Light)",
            "2. Intermediate (Light and Dark)",
            "3. Mafic (Mostly Dark)"]
FELSIC = 1
INTERMEDIATE = 2
MAFIC = 3

# Option Sets
opts = [main_opts, 
        type_opts,
        luster_opts,
        color_opts,
        streak_opts,
        texture_opts,
        mci_opts
        ]
MI_MAIN = 0
MI_TYPE = 1
MI_LUSTER = 2
MI_COLOR = 3
MI_STREAK = 4
MI_TEXTURE = 5
MI_MCI = 6


def print_menu(title, opts):
  """
  Displays a formatted menu with a title and a list of options.
  Prints the menu header, each option on its own line, and a closing divider.

  :param title: title text for the menu, string
  :param opts: list of option strings to display, list[str]
  :return: none
  """

  i = 0
  print(f"\n{title}")
  print(DIVIDER)

  while i < len(opts):
    print(opts[i])
    i += 1
  print(DIVIDER)


def get_option(opts):
  """
  Prompts the user to select a menu option and validates the input.
  Ensures the selection is an integer within the valid option range.
  
  :param opts: list of option strings; used to determine valid range, list[str]
  :return option: validated menu selection, int
  """

  option = 0
  valid = False
  while valid == False:
      try:
          option = int(input("Enter Selection:\n> "))
          while option <= 0 or option > len(opts):
              print("Invalid Entry. Try Again.")
              option = int(input("Enter Selection:\n> "))
          valid = True
      except:
          print("Invalid Entry. Try Again.")
  return option