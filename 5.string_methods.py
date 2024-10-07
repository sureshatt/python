# lower and upper case
s1 = "tom"
s2 = s1.capitalize()
print(s1 + "=>" + s2)
print(s1.islower())

# poistioning and padding
s3 = "cat"
print(s3.center(7,"-"))
print(s3.ljust(7, "_"))
print(s3.rjust(7, "_"))

#find/count pattern
s4 = "occurrences"
print(s4.count("r", 0))

#index
print(s4.find("r"))
print(s4.index("r"))
print(s4.rindex("r"))

#ends and starts
print(s4.endswith("es"))
print(s4.startswith("oc"))

# validations
s5 = "This is @2025"
print(s5.isalpha())
print(s5.isalnum())
print(s5.isprintable())
print(s5.isascii())
print(s5.isdigit())
print(s5.isnumeric())

# stripping
s6 = "    mid   "
print(s6.strip())
print(s6.lstrip())
print(s6.rstrip())

# slicing and partitioning 
s7 = "Ship shipping ships"
print(s7.partition("pp"))
print(s7.split("ip"))

# prefix - suffix
s8 = "00times--"
print(s8.removeprefix("00"))
print(s8.removesuffix("--"))

# replace
s9 = "Straße"
print(s9.replace("ß", "ss"))