# Define a dictionary containing information about elements in the periodic table
elements = {
    "H": {"name": "Hydrogen", "symbol": "H", "number": 1, "mass": 1.00794, "category": "Nonmetal"},
    "He": {"name": "Helium", "symbol": "He", "number": 2, "mass": 4.002602, "category": "Noble Gas"},
    "Li": {"name": "Lithium", "symbol": "Li", "number": 3, "mass": 6.94, "category": "Alkali Metal"},
    "Be": {"name": "Beryllium", "symbol": "Be", "number": 4, "mass": 9.0121831, "category": "Alkaline Earth Metal"},
    "B": {"name": "Boron", "symbol": "B", "number": 5, "mass": 10.81, "category": "Metalloid"},
    "C": {"name": "Carbon", "symbol": "C", "number": 6, "mass": 12.01, "category": "Nonmetal"},
    "N": {"name": "Nitrogen", "symbol": "N", "number": 7, "mass": 14.01, "category": "Nonmetal"},
    "O": {"name": "Oxygen", "symbol": "O", "number": 8, "mass": 15.999, "category": "Nonmetal"},
    "F": {"name": "Fluorine", "symbol": "F", "number": 9, "mass": 18.998403, "category": "Halogen"},
    "Ne": {"name": "Neon", "symbol": "Ne", "number": 10, "mass": 20.1797, "category": "Noble Gas"},
    "Na": {"name": "Sodium", "symbol": "Na", "number": 11, "mass": 22.98976928, "category": "Alkali Metal"},
    "Mg": {"name": "Magnesium", "symbol": "Mg", "number": 12, "mass": 24.305, "category": "Alkaline Earth Metal"},
    "Al": {"name": "Aluminum", "symbol": "Al", "number": 13, "mass": 26.9815384, "category": "Post-Transition Metal"},
    "Si": {"name": "Silicon", "symbol": "Si", "number": 14, "mass": 28.085, "category": "Metalloid"},
    "P": {"name": "Phosphorus", "symbol": "P", "number": 15, "mass": 30.973761998, "category": "Nonmetal"},
    "S": {"name": "Sulfur", "symbol": "S", "number": 16, "mass": 32.06, "category": "Nonmetal"},
    "Cl": {"name": "Chlorine", "symbol": "Cl", "number": 17, "mass": 35.45, "category": "Halogen"},
    "K": {"name": "Potassium", "symbol": "K", "number": 19, "mass": 39.0983, "category": "Alkali Metal"},
    "Ca": {"name": "Calcium", "symbol": "Ca", "number": 20, "mass": 40.08, "category": "Alkaline Earth Metal"},
    "Sc": {"name": "Scandium", "symbol": "Sc", "number": 21, "mass": 44.955908, "category": "Transition Metal"},
    "Ti": {"name": "Titanium", "symbol": "Ti", "number": 22, "mass": 47.867, "category": "Transition Metal"},
    "V": {"name": "Vanadium", "symbol": "V", "number": 23, "mass": 50.9415, "category": "Transition Metal"},
    "Cr": {"name": "Chromium", "symbol": "Cr", "number": 24, "mass": 51.9961, "category": "Transition Metal"},
    "Mn": {"name": "Manganese", "symbol": "Mn", "number": 25, "mass": 54.938044, "category": "Transition Metal"},
    "Fe": {"name": "Iron", "symbol": "Fe", "number": 26, "mass": 55.845, "category": "Transition Metal"},
    "Ni": {"name": "Nickel", "symbol": "Ni", "number": 28, "mass": 58.6934, "category": "Transition Metal"},
    "Cu": {"name": "Copper", "symbol": "Cu", "number": 29, "mass": 63.546, "category": "Transition Metal"},
    "Zn": {"name": "Zinc", "symbol": "Zn", "number": 30, "mass": 65.38, "category": "Transition Metal"},
    "Ga": {"name": "Gallium", "symbol": "Ga", "number": 31, "mass": 69.723, "category": "Post-Transition Metal"},
    "Ge": {"name": "Germanium", "symbol": "Ge", "number": 32, "mass": 72.63, "category": "Metalloid"},
    "As": {"name": "Arsenic", "symbol": "As", "number": 33, "mass": 74.921595, "category": "Metalloid"},
    "Se": {"name": "Selenium", "symbol": "Se", "number": 34, "mass": 78.971, "category": "Nonmetal"},
    "Br": {"name": "Bromine", "symbol": "Br", "number": 35, "mass": 79.904, "category": "Halogen"},
    "Kr": {"name": "Krypton", "symbol": "Kr", "number": 36, "mass": 83.798, "category": "Noble Gas"},
    "Rb": {"name": "Rubidium", "symbol": "Rb", "number": 37, "mass": 85.4678, "category": "Alkali Metal"},
    "Sr": {"name": "Strontium", "symbol": "Sr", "number": 38, "mass": 87.62, "category": "Alkaline Earth Metal"},
    "Y": {"name": "Yttrium", "symbol": "Y", "number": 39, "mass": 88.90584, "category": "Transition Metal"},
    "Zr": {"name": "Zirconium", "symbol": "Zr", "number": 40, "mass": 91.224, "category": "Transition Metal"},
    "Nb": {"name": "Niobium", "symbol": "Nb", "number": 41, "mass": 92.90637, "category": "Transition Metal"},
    "Mo": {"name": "Molybdenum", "symbol": "Mo", "number": 42, "mass": 95.95, "category": "Transition Metal"},
    "Tc": {"name": "Technetium", "symbol": "Tc", "number": 43, "mass": 98, "category": "Transition Metal"},
    "Ru": {"name": "Ruthenium", "symbol": "Ru", "number": 44, "mass": 101.07, "category": "Transition Metal"},
    "Rh": {"name": "Rhodium", "symbol": "Rh", "number": 45, "mass": 102.90550, "category": "Transition Metal"},
    "Pd": {"name": "Palladium", "symbol": "Pd", "number": 46, "mass": 106.42, "category": "Transition Metal"},
    "Ag": {"name": "Silver", "symbol": "Ag", "number": 47, "mass": 107.8682, "category": "Transition Metal"},
    "Cd": {"name": "Cadmium", "symbol": "Cd", "number": 48, "mass": 112.414, "category": "Transition Metal"},
    "In": {"name": "Indium", "symbol": "In", "number": 49, "mass": 114.818, "category": "Post-Transition Metal"},
    "Sn": {"name": "Tin", "symbol": "Sn", "number": 50, "mass": 118.71, "category": "Post-Transition Metal"},
    "Sb": {"name": "Antimony", "symbol": "Sb", "number": 51, "mass": 121.760, "category": "Metalloid"},
    "Te": {"name": "Tellurium", "symbol": "Te", "number": 52, "mass": 127.60, "category": "Metalloid"},
    "I": {"name": "Iodine", "symbol": "I", "number": 53, "mass": 126.90447, "category": "Halogen"},
    "Xe": {"name": "Xenon", "symbol": "Xe", "number": 54, "mass": 131.293, "category": "Noble Gas"},
    "Cs": {"name": "Cesium", "symbol": "Cs", "number": 55, "mass": 132.90545196, "category": "Alkali Metal"},
    "Ba": {"name": "Barium", "symbol": "Ba", "number": 56, "mass": 137.327, "category": "Alkaline Earth Metal"},
    "La": {"name": "Lanthanum", "symbol": "La", "number": 57, "mass": 138.90547, "category": "Lanthanide"},
    "Ce": {"name": "Cerium", "symbol": "Ce", "number": 58, "mass": 140.116, "category": "Lanthanide"},
    "Pr": {"name": "Praseodymium", "symbol": "Pr", "number": 59, "mass": 140.90766, "category": "Lanthanide"},
    "Nd": {"name": "Neodymium", "symbol": "Nd", "number": 60, "mass": 144.242, "category": "Lanthanide"},
    "Pm": {"name": "Promethium", "symbol": "Pm", "number": 61, "mass": 145, "category": "Lanthanide"},
    "Sm": {"name": "Samarium", "symbol": "Sm", "number": 62, "mass": 150.36, "category": "Lanthanide"},
    "Eu": {"name": "Europium", "symbol": "Eu", "number": 63, "mass": 151.964, "category": "Lanthanide"},
    "Gd": {"name": "Gadolinium", "symbol": "Gd", "number": 64, "mass": 157.25, "category": "Lanthanide"},
    "Tb": {"name": "Terbium", "symbol": "Tb", "number": 65, "mass": 158.92535, "category": "Lanthanide"},
    "Dy": {"name": "Dysprosium", "symbol": "Dy", "number": 66, "mass": 162.500, "category": "Lanthanide"},
    "Ho": {"name": "Holmium", "symbol": "Ho", "number": 67, "mass": 164.93033, "category": "Lanthanide"},
    "Er": {"name": "Erbium", "symbol": "Er", "number": 68, "mass": 167.259, "category": "Lanthanide"},
    "Tm": {"name": "Thulium", "symbol": "Tm", "number": 69, "mass": 168.93422, "category": "Lanthanide"},
    "Yb": {"name": "Ytterbium", "symbol": "Yb", "number": 70, "mass": 173.045, "category": "Lanthanide"},
    "Lu": {"name": "Lutetium", "symbol": "Lu", "number": 71, "mass": 174.9668, "category": "Lanthanide"},
    "Hf": {"name": "Hafnium", "symbol": "Hf", "number": 72, "mass": 178.49, "category": "Transition Metal"},
    "Ta": {"name": "Tantalum", "symbol": "Ta", "number": 73, "mass": 180.94788, "category": "Transition Metal"},
    "W": {"name": "Tungsten", "symbol": "W", "number": 74, "mass": 183.84, "category": "Transition Metal"},
    "Re": {"name": "Rhenium", "symbol": "Re", "number": 75, "mass": 186.207, "category": "Transition Metal"},
    "Os": {"name": "Osmium", "symbol": "Os", "number": 76, "mass": 190.23, "category": "Transition Metal"},
    "Ir": {"name": "Iridium", "symbol": "Ir", "number": 77, "mass": 192.217, "category": "Transition Metal"},
    "Pt": {"name": "Platinum", "symbol": "Pt", "number": 78, "mass": 195.084, "category": "Transition Metal"},
    "Au": {"name": "Gold", "symbol": "Au", "number": 79, "mass": 196.966569, "category": "Transition Metal"},
    "Hg": {"name": "Mercury", "symbol": "Hg", "number": 80, "mass": 200.592, "category": "Transition Metal"},
    "Tl": {"name": "Thallium", "symbol": "Tl", "number": 81, "mass": 204.38, "category": "Post-Transition Metal"},
    "Pb": {"name": "Lead", "symbol": "Pb", "number": 82, "mass": 207.2, "category": "Post-Transition Metal"},
    "Bi": {"name": "Bismuth", "symbol": "Bi", "number": 83, "mass": 208.98040, "category": "Post-Transition Metal"},
    "Po": {"name": "Polonium", "symbol": "Po", "number": 84, "mass": 209, "category": "Metalloid"},
    "At": {"name": "Astatine", "symbol": "At", "number": 85, "mass": 210, "category": "Halogen"},
    "Rn": {"name": "Radon", "symbol": "Rn", "number": 86, "mass": 222, "category": "Noble Gas"},
    "Fr": {"name": "Francium", "symbol": "Fr", "number": 87, "mass": 223, "category": "Alkali Metal"},
    "Ra": {"name": "Radium", "symbol": "Ra", "number": 88, "mass": 226, "category": "Alkaline Earth Metal"},
    "Ac": {"name": "Actinium", "symbol": "Ac", "number": 89, "mass": 227, "category": "Actinide"},
    "Th": {"name": "Thorium", "symbol": "Th", "number": 90, "mass": 232.0377, "category": "Actinide"},
    "Pa": {"name": "Protactinium", "symbol": "Pa", "number": 91, "mass": 231.03588, "category": "Actinide"},
    "U": {"name": "Uranium", "symbol": "U", "number": 92, "mass": 238.02891, "category": "Actinide"},
    "Np": {"name": "Neptunium", "symbol": "Np", "number": 93, "mass": 237, "category": "Actinide"},
    "Pu": {"name": "Plutonium", "symbol": "Pu", "number": 94, "mass": 244, "category": "Actinide"},
    "Am": {"name": "Americium", "symbol": "Am", "number": 95, "mass": 243, "category": "Actinide"},
    "Cm": {"name": "Curium", "symbol": "Cm", "number": 96, "mass": 247, "category": "Actinide"},
    "Bk": {"name": "Berkelium", "symbol": "Bk", "number": 97, "mass": 247, "category": "Actinide"},
    "Cf": {"name": "Californium", "symbol": "Cf", "number": 98, "mass": 251, "category": "Actinide"},
    "Es": {"name": "Einsteinium", "symbol": "Es", "number": 99, "mass": 252, "category": "Actinide"},
    "Fm": {"name": "Fermium", "symbol": "Fm", "number": 100, "mass": 257, "category": "Actinide"},
    "Md": {"name": "Mendelevium", "symbol": "Md", "number": 101, "mass": 258, "category": "Actinide"},
    "No": {"name": "Nobelium", "symbol": "No", "number": 102, "mass": 259, "category": "Actinide"},
    "Lr": {"name": "Lawrencium", "symbol": "Lr", "number": 103, "mass": 262, "category": "Actinide"},
    "Rf": {"name": "Rutherfordium", "symbol": "Rf", "number": 104, "mass": 267, "category": "Transition Metal"},
    "Db": {"name": "Dubnium", "symbol": "Db", "number": 105, "mass": 270, "category": "Transition Metal"},
    "Sg": {"name": "Seaborgium", "symbol": "Sg", "number": 106, "mass": 271, "category": "Transition Metal"},
    "Bh": {"name": "Bohrium", "symbol": "Bh", "number": 107, "mass": 270, "category": "Transition Metal"},
    "Hs": {"name": "Hassium", "symbol": "Hs", "number": 108, "mass": 269, "category": "Transition Metal"},
    "Mt": {"name": "Meitnerium", "symbol": "Mt", "number": 109, "mass": 278, "category": "Unknown"},
    "Ds": {"name": "Darmstadtium", "symbol": "Ds", "number": 110, "mass": 281, "category": "Unknown"},
    "Rg": {"name": "Roentgenium", "symbol": "Rg", "number": 111, "mass": 280, "category": "Unknown"},
    "Cn": {"name": "Copernicium", "symbol": "Cn", "number": 112, "mass": 285, "category": "Unknown"},
    "Nh": {"name": "Nihonium", "symbol": "Nh", "number": 113, "mass": 284, "category": "Unknown"},
    "Fl": {"name": "Flerovium", "symbol": "Fl", "number": 114, "mass": 289, "category": "Unknown"},
    "Mc": {"name": "Moscovium", "symbol": "Mc", "number": 115, "mass": 288, "category": "Unknown"},
    "Lv": {"name": "Livermorium", "symbol": "Lv", "number": 116, "mass": 293, "category": "Unknown"},
    "Ts": {"name": "Tennessine", "symbol": "Ts", "number": 117, "mass": 294, "category": "Unknown"},
    "Og": {"name": "Oganesson", "symbol": "Og", "number": 118, "mass": 294, "category": "Unknown"}
}

def find_element(identifier):
    element = None
    if identifier in elements:
        element = elements[identifier]
    else:
        for symbol, data in elements.items():
            if data["name"].lower() == identifier.lower():
                element = data
                break
    return element

def main():
    print("Chemy Chemist Assistant - Periodic Table Reference")
    print("===========================================")

    while True:
        query = input("Enter the symbol or name of an element (or 'exit' to quit): ")

        if query.lower() == "exit":
            break

        element_info = find_element(query)
        if element_info:
            print("\nElement:", element_info["name"])
            print("Symbol:", element_info["symbol"])
            print("Atomic Number:", element_info["number"])
            print("Atomic Mass:", element_info["mass"])
            print("Category:", element_info["category"])
        else:
            print("Element not found in the periodic table.")

    print("Thank you, see you next time!")

if __name__ == "__main__":
    main()

def run_test(symbol_or_name):
    element_info = find_element(symbol_or_name)
    if element_info:
        print("\nElement:", element_info["name"])
        print("Symbol:", element_info["symbol"])
        print("Atomic Number:", element_info["number"])
        print("Atomic Mass:", element_info["mass"])
        print("Category:", element_info["category"])
    else:
        print("Element not found in the periodic table.")

if __name__ == "__main__":
    # Test cases for different elements
    test_elements = ["H", "He", "Li", "C", "N", "O", "F", "Na", "Mg", "Si", "Cl", "Ca", "Fe", "Cu", "Zn", "Ag", "Au"]
    
    print("Testing different elements:")
    for element in test_elements:
        run_test(element)

    # Test cases for different element names
    test_names = ["Hydrogen", "Helium", "Lithium", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Sodium", "Magnesium", "Silicon", "Chlorine", "Calcium", "Iron", "Copper", "Zinc", "Silver", "Gold"]
    
    print("\nTesting different element names:")
    for name in test_names:
        run_test(name)
