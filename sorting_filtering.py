# find index:
# vehicle_counts = vehicles['vehicle_type'].value_counts() // <- note .value_counts()
# vehicle_counts
# The output we’ll receive is

# sedan/wagon                  1205
# suv                           742
# pickup                        373
# van                           189
# passenger van/shuttle bus       7
# vocational/cab chassis          4
# Here, each row is labeled with the vehicle type as text. If we call

# vehicle_counts.index
# we’ll receive the output

# Index(['sedan/wagon', 'suv', 'pickup', 'van', 'passenger van/shuttle bus', 
# 'vocational/cab chassis'], dtype='object')


# reset the index:
# vehicle_counts.reset_index()

# -----------------------------------------------------

# The syntax to sort a DataFrame df in pandas by a particular column is

# df = df.sort_values(by = 'Column')

# df = df.sort_values(by = 'Column', ascending = False)

# Calling .sort_values() will only sort values by a column. 
# To sort rows by the index values instead, use .sort_index(). 
# There’s no need to specify a by parameter, since the method will already sort by the index.

