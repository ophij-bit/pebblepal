#******************************************************************************
# Author:           Ophi Joughin
# Assignment:       Assignment 04
# Date:             A01: 10/05/2025 
#                   A02: 10/08/25 
#                   A03: 11/05/2025 
#                   A04: 11/17/2025
# Description:      This program offers a variety of tools to guess the 
#                   identity of a given rock sample, and display information
#                   about the guessed rock. The user is presented with a main
#                   menu to select whether to analyze a new sample, calculate
#                   a sample’s density, display a log of the samples analyzed
#                   so far, or quit the program. 
#                   If the user selects the analyze option they are presented
#                   with a further series of menus and questions that 
#                   lead the program to a conclusion about the sample's 
#                   identity. (Currently the program can guess minerals 
#                   and igneous rocks.) 
#                   If the user selects the density option the program will 
#                   prompt them for the sample’s mass and volume, and 
#                   display the calculated density and predicted behavior
#                   of the sample in water.
#                   If the user selects the display option, the program will
#                   display a placeholder log for now. Selecting the quit
#                   option will display the number of samples analyzed during
#                   the current session before exiting the program.
#                   All user input will be validated for data type and range,
#                   and reprompted if invalid. The main menu will be presented
#                   to the user after each operation, until the user selects
#                   the quit option. 
#                   An imported module of rock facts has been implemented
#                   to save space within the main program.
# Additional Files: rockfacts.py, menus.py
# Revisions:        Please see file: revisions.txt
#******************************************************************************
import textwrap
import rockfacts as rf
import menus as m

# Formatting Elements
DIVIDER = m.DIVIDER
LINE_LEN = m.DIV_LEN - 2
LABEL_MAX = 8
ROCK_EMOJI = "\U0001FAA8"

def main():
  # Variable Declaration
  mi = 0 # menu index, used for menus.py
  option = 0
  sample_type = 0
  label = ""
  guess = ""
  fact = "" 
  unit = ""
  mass = 0.0
  volume = 0.0
  density = 0.0
  a_labels = []
  guesses = []
  facts = []
  d_labels =[]
  masses = []
  volumes = []
  a_count = 0 # sample analysis counter
  d_count = 0 # density calculation counter

  print_intro()
  mi = m.MI_MAIN
  m.print_menu(m.titles[mi], m.opts[mi])
  option = m.get_option(m.opts[mi])

  while option != m.QUIT:

    if option == m.ANALYZE:
      mi = m.MI_TYPE
      m.print_menu(m.titles[mi], m.opts[mi])
      sample_type = m.get_option(m.opts[mi])
      label = get_label()
      a_labels.append(label)
      guess, fact = guess_sample(sample_type)
      guesses.append(guess)
      facts.append(fact)
      print_guess(a_labels[a_count], guesses[a_count], facts[a_count])
      a_count += 1

    elif option == m.DISPLAY_ANALYSIS:
      print_a_log(a_labels, guesses, a_count)

    elif option == m.DENSITY:
      label = get_label()
      d_labels.append(label)
      unit = rf.UNIT_MASS
      mass = get_value("Mass", unit)
      masses.append(mass)
      unit = rf.UNIT_VOLUME
      volume = get_value("Volume", unit)
      volumes.append(volume)
      density = calc_density(masses[d_count], volumes[d_count])
      buoyancy = calc_buoyancy(density)
      print_density(d_labels[d_count], density, buoyancy)
      d_count += 1

    elif option == m.DISPLAY_DENSITIES:
      print_d_log(d_labels, masses, volumes, d_count)

    mi = m.MI_MAIN
    m.print_menu(m.titles[mi], m.opts[mi])
    option = m.get_option(m.opts[mi])

  print_end(a_count, d_count)


def print_intro():
  """
  Display the program title and a brief introduction message.
  Uses textwrap to format text to the appropriate line width.

  :return: None
  """
  print(f"\nWelcome To Pebble Pal!{ROCK_EMOJI}")
  print(DIVIDER)
  intro = ("This program is designed to help you identify mystery "
          + "rocks and minerals! You can analyze a hand sample by answering "
          + "questions about its attributes, or you can calculate its "
          + "density.")
  print(f"{textwrap.fill(intro, width=LINE_LEN)}")


def print_end(a_count, d_count):
  """
  Display a closing message along with the number of analyses and
  density calculations completed during the session.

  :param a_count: total number of samples analyzed, int
  :param d_count: total number of density calculations performed, int
  :return: None
  """
  print(f"\nThank You For Using Pebble Pal!{ROCK_EMOJI}")
  print(f"{DIVIDER}")
  if a_count == 1:
      print(f"> You Analyzed {a_count} Sample")
  else:    
      print(f"> You Analyzed {a_count} Samples")
  if d_count == 1:
      print(f"> You Calculated {d_count} Density")
  else:    
      print(f"> You Calculated {d_count} Densities") 


def print_guess(label, guess, fact):
  """
  Display the identification result for a sample, including the label,
  predicted identity, and an accompanying fact.

  :param label: sample label, string
  :param guess: predicted identity of the sample, string
  :param fact: informational fact about the guessed identity, string
  :return: None
  """
  print("\nSample Identification Guess")
  print(DIVIDER)
  print(f"Sample\t{label}")
  print(f"Guess\t{guess}")
  print(DIVIDER)
  print(f"> Additional Info:")
  print(f"\n{textwrap.fill(fact, width=LINE_LEN)}")


def print_density(label, density, buoy):
  """
  Display density information for a sample, including the calculated
  density, predicted buoyancy behavior, and a list of rocks/minerals
  with similar densities.

  :param label: sample label, string
  :param density: calculated density value (g/cm^3), float
  :param buoy: buoyancy description based on density, string
  :return: None
  """
  print("\nSample Density")
  print(DIVIDER)
  print(f"Sample\t{label}")
  print(f"Density\t{density:.2f}{rf.UNIT_DENSITY}")
  print(DIVIDER)
  print(f"> This sample likely {buoy} in water.")
  rf.print_dens_list(rf.check_density(density))


def print_a_log(a_labels, guesses, a_count):
  """
  Display a formatted log of all analyzed samples, including each label
  and its corresponding identification guess.

  :param a_labels: list of sample labels, list of strings
  :param guesses: list of identity guesses, list of strings
  :param a_count: number of analyzed samples, int
  :return: None
  """
  i = 0
  print(f"\nSample Analysis Log")
  print(DIVIDER)
  while i < a_count:
      print(f"{a_labels[i]}\t{guesses[i]}")
      i += 1
  print(DIVIDER)
  print(f"> Samples Analyzed: {a_count}")


def print_d_log(d_labels, masses, volumes, d_count):
  """
  Display a formatted log of all density calculations, including each
  label, calculated density, and totals for buoyancy categories.

  :param d_labels: list of sample labels, list of strings
  :param masses: list of sample masses, list of floats
  :param volumes: list of sample volumes, list of floats
  :param d_count: number of density entries, int
  :return: None
  """

  float_count = 0
  sink_count = 0
  suspend_count = 0
  i = 0
  density = 0.0
  print(f"\nDensity Log")
  print(DIVIDER)
  while i < d_count:
      density = calc_density(masses[i], volumes[i])
      buoyancy = calc_buoyancy(density)
      if buoyancy == "floats":
        float_count += 1
      elif buoyancy == "sinks":
        sink_count += 1
      elif buoyancy == "remains suspended":
        suspend_count += 1
      print(f"{d_labels[i]}\t{density:.2f}{rf.UNIT_DENSITY}")
      i += 1
  print(DIVIDER)
  print(f"> Densities Calculated: {d_count}")
  if float_count == 1:
    print(f"> 1 sample floats")
  else:
    print(f"> {float_count} samples float")
  if sink_count == 1:
    print(f"> 1 sample sinks")
  else:
    print(f"> {sink_count} samples sink")
  if suspend_count == 1:
    print(f"> 1 sample suspends")
  else:
    print(f"> {suspend_count} samples suspend")


def get_label():
  """
  Prompt the user for a sample label, validate that it is non-empty,
  and shorten it if necessary using shorten_string().

  :return: validated and possibly shortened label string
  """
  label = ""
  label = shorten_string(input(f"\nEnter Sample Label:\n> "))
  while not label:
    print("Please Enter A Label")
    label = shorten_string(input(f"\nEnter Sample Label:\n> "))
  return label


def shorten_string(input_string):
  """
  Shorten a string to the maximum label length, appending ellipses if
  necessary. If shorter than the limit, pad with a tab for alignment.

  :param input_string: the string to format, string
  :return: formatted label string, string
  """
  short_string = ""
  if len(input_string) > LABEL_MAX:
      short_string = (f"{input_string[:LABEL_MAX]}...")
  elif len(input_string) < LABEL_MAX: 
      short_string = (f"{input_string}\t")
  else: 
    short_string = (f"{input_string}")  
  return short_string


def get_value(string, unit):
  """
  Prompt the user for a numeric value (mass or volume), validate that
  it is a positive float, and return the result.

  :param string: descriptor for the value (e.g., 'Mass' or 'Volume'), string
  :param unit: unit to display in the prompt, string
  :return: validated numeric value, float
  """
  value = 0.0
  valid = False
  while valid == False:
      try:
          value = float(input(f"Enter Sample {string} ({unit}):\n> "))
          while value <= 0.0:
              print(f"{string} Must Be Greater Than Zero")
              value = float(input(f"Enter Sample {string} ({unit}):\n> "))
          valid = True
      except:
          print("Invalid Entry. Try Again.")
  return value


def get_attribute(mi):
  """
  Display a menu of attribute options using menus.py and prompt the
  user to select one. Returns the validated option.

  :param mi: menu index indicating which attribute menu to show, int
  :return: selected attribute option, int
  """
  attr = 0
  m.print_menu(m.titles[mi], m.opts[mi])
  attr = m.get_option(m.opts[mi])
  return attr


def get_hardness():
  """
  Prompt the user for a mineral hardness value on the Mohs scale,
  validate that it is between 1 and 10, and return it.

  :return: hardness value, float
  """
  hard = 0
  valid = False
  while valid == False:
      try:
          hard = float(input("\nEnter Mineral Hardness: (1-10)\n> "))
          while hard < 1 or hard > rf.HARD:
              print("Hardness Must Be Between 1 and 10")
              hard = float(input("Enter Mineral Hardness: (1-10)\n> "))
          valid = True
      except:
          print("Invalid Entry. Try Again.")
  return hard


def calc_density(mass, volume):
  """
  Compute the density of a sample given mass and volume.

  :param mass: sample mass in grams, float
  :param volume: sample volume in cubic centimeters, float
  :return: density in g/cm^3, float
  """
  density = 0.0
  density = mass / volume
  return density


def calc_buoyancy(density):
  """
  Determine whether a sample will float, sink, or remain suspended
  in water based on its density.

  :param density: density value in g/cm^3, float
  :return: buoyancy description, string
  """

  if density > rf.WATER_DENSITY:
    buoyancy = "sinks"
  elif density == rf.WATER_DENSITY:
    buoyancy = "remains suspended"
  elif density > 0.0:
    buoyancy = "floats"
  else:
    buoyancy = "does something"
  return buoyancy


def guess_sample(sample_type):
  """
  Direct the sample through the appropriate identification workflow
  based on its type (mineral, igneous, etc.). Collect necessary
  attributes and call the matching guess function.

  :param sample_type: selected sample type constant, int
  :return: (guess, fact) tuple containing predicted identity and fact
  """

  fact = rf.UNKNOWN_FACT
  if sample_type == m.MINERAL:
    mi = m.MI_LUSTER
    luster = get_attribute(mi)
    mi = m.MI_COLOR
    color = get_attribute(mi)
    mi = m.MI_STREAK
    streak = get_attribute(mi)
    hardness = get_hardness()
    guess, fact = guess_mineral(luster, color, streak, hardness)
  elif sample_type == m.IGNEOUS:
    mi = m.MI_TEXTURE
    texture = get_attribute(mi)
    mi = m.MI_MCI
    mci = get_attribute(mi) # mci: Mafic Color Index
    guess, fact = guess_igneous(texture, mci)
  elif sample_type == m.SEDIMENTARY:
    guess = "Unknown Sedimentary Rock"
    fact = rf.UNKNOWN_FACT
  elif sample_type == m.METAMORPHIC:
    guess = "Unknown Metamorphic Rock"
    fact = rf.UNKNOWN_FACT
  elif sample_type == m.UNKNOWN:
    guess = "Unknown"
    fact = rf.UNKNOWN_FACT
  return guess, fact


def guess_mineral(luster, color, streak, hardness):
  """
  Predict the identity of a mineral using luster, color, streak,
  and hardness through a series of conditional checks.

  :param luster: selected luster option, int
  :param color: selected color option, int
  :param streak: selected streak option, int
  :param hardness: mineral hardness value, float
  :return: (guess, fact) tuple, strings
  """

  guess = ""
  fact = ""
  if streak == m.RED_STREAK:
    guess = "Hematite"
    fact = rf.UNKNOWN_FACT
  elif streak == m.GREEN_STREAK and luster == m.METALLIC:
    guess = "Pyrite"
    fact = rf.UNKNOWN_FACT
  elif luster == m.METALLIC:
    if hardness <= rf.SOFT:
      if color == m.DARK:
        guess = "Graphite"
        fact = rf.GRAPHITE_FACT
    elif hardness < rf.MEDIUM:
      guess = "Unknown Mineral"
      fact = rf.UNKNOWN_FACT
    elif hardness <= rf.HARD:
      guess = "Unknown Mineral"
      fact = rf.UNKNOWN_FACT
  elif luster == m.NON_METALLIC:
    if hardness <= rf.SOFT:
      if color == m.LIGHT:
        guess = "Talc"
        fact = rf.UNKNOWN_FACT
      elif color == m.COLORED:
        guess = "Sulfur"
        fact = rf.UNKNOWN_FACT
    elif hardness < rf.MEDIUM:
      if color == m.COLORED:
        guess = "Fluorite"
        fact = rf.FLUORITE_FACT
    elif hardness <= rf.HARD:
      guess = "Unknown Mineral"
      fact = rf.UNKNOWN_FACT
  else: 
    guess = "Unknown Mineral"
    fact = rf.UNKNOWN_FACT
  return guess, fact


def guess_igneous(texture, mci):
  """
  Predict the identity of an igneous rock using texture and mafic
  color index (MCI), applying property trees to determine the best match.

  :param texture: igneous texture option, int
  :param mci: mafic color index option, int
  :return: (guess, fact) tuple, strings
  """

  if texture == m.COARSE:
    if mci == m.FELSIC:
      guess = "Granite"
      fact = rf.GRANITE_FACT
    elif mci == m.INTERMEDIATE:
      guess = "Diorite"
      fact = rf.DIORITE_FACT
    elif mci == m.MAFIC:
      guess = "Gabbro"
      fact = rf.GABBRO_FACT 
  elif texture == m.FINE:
    if mci == m.FELSIC:
      guess = "Rhyolite"
      fact = rf.RHYOLITE_FACT
    elif mci == m.INTERMEDIATE:
      guess = "Andesite"
      fact = rf.ANDESITE_FACT
    elif mci == m.MAFIC:
      guess = "Basalt"
      fact = rf.BASALT_FACT
  elif texture == m.BOTH:
    if mci == m.FELSIC:
      guess = "Rhyolite"
      fact = rf.RHYOLITE_FACT
    elif mci == m.INTERMEDIATE:
      guess = "Andesite"
      fact = rf.ANDESITE_FACT
    elif mci == m.MAFIC:
      guess = "Basalt"
      fact = rf.BASALT_FACT
    guess = "Porphyritic " + guess
    fact = fact + rf.PORPHYRITIC_FACT 
  elif texture == m.VESICULAR:
    if mci == m.FELSIC:
      guess = "Pumice"
      fact = rf.PUMICE_FACT
    elif mci == m.INTERMEDIATE:
      guess = "Unknown Vesicular"
      fact = rf.VESICULAR_FACT
    elif mci == m.MAFIC:
      guess = "Scoria"
      fact = rf.SCORIA_FACT
  elif texture == m.GLASSY:
    guess = "Obsidian"
    fact = rf.OBSIDIAN_FACT
  return guess, fact


#******************************************************************************
main()