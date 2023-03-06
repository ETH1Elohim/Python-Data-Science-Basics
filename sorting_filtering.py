import pandas as pd
vehicles = pd.read_csv('vehicles.csv')
vehicles.head()

# find index:
vehicle_counts = vehicles['vehicle_type'].value_counts() # <- note .value_counts()
vehicle_counts
# The output we’ll receive is

# sedan/wagon                  1205
# suv                           742
# pickup                        373
# van                           189
# passenger van/shuttle bus       7
# vocational/cab chassis          4
# Here, each row is labeled with the vehicle type as text. If we call

vehicle_counts.index
# we’ll receive the output

# Index(['sedan/wagon', 'suv', 'pickup', 'van', 'passenger van/shuttle bus', 
# 'vocational/cab chassis'], dtype='object')


# reset the index:
vehicle_counts.reset_index()

# -----------------------------------------------------

# The syntax to sort a DataFrame df in pandas by a particular column is

# df = df.sort_values(by = 'Column')

# df = df.sort_values(by = 'Column', ascending = False)

# Calling .sort_values() will only sort values by a column. 
# To sort rows by the index values instead, use .sort_index(). 
# There’s no need to specify a by parameter, since the method will already sort by the index.

# -----------------------------------------------------

# Selecting Specific Rows:

# df.loc[list_of_row_labels, list_of_column_labels]

# .iloc works using the position ([index]) vs. their labels

# df.iloc[list_of_row_positions, list_of_column_positions]

# slice info by using [start_position:stop_position] vs. listing all rows &/or columns
# :3 will produce 0 to 3. Just : will produce all.

# -----------------------------------------------------

# Filtering with Booleans:

# vehicle data:
# 	id	model	year	transmission	manufacturer	vehicle_type	fuel	fuel_configuration	best_mpge
# 0	12988	amg e53 4matic+ (convertible)	2022	auto	mercedes-benz	sedan/wagon	hybrid electric	hybrid electric	28.0
# 1	689	avalanche ffv	2007	auto	chevrolet	pickup	ethanol (e85)	flexible fuel	21.0
# 2	950	impala	2010	auto	chevrolet	sedan/wagon	ethanol (e85)	flexible fuel	29.0
# 3	250	yukon xl ffv	2004	auto	gmc	suv	ethanol (e85)	flexible fuel	18.0
# 4	13089	sf90 spyder	2022	auto	ferrari	sedan/wagon	plug-in hybrid electric	hybrid electric	19.0

# example:
import pandas as pd
vehicles = pd.read_csv('vehicles.csv')
vehicles.head()

gt25 = vehicles['best_mpge'] >= 25
gt25.head()

is_sedanwagon = vehicles['vehicle_type'] == 'sedan/wagon'
is_sedanwagon.head()

# mpg > 40 
gt40 = vehicles['best_mpge'] > 40


above_average = vehicles[gt40]
above_average.head()

is_auto = vehicles['transmission'] == 'auto'
auto_transmission = vehicles[is_auto]
auto_transmission.head()


# combining booleans example:
year_gt2016 = vehicles['year'] > 2016
is_electric = vehicles['fuel'] == 'electric'
combined = year_gt2016 & is_electric

electric_and_after_2016 = vehicles[combined]
electric_and_after_2016.sort_values(by='year').head()

is_biodiesel = vehicles['fuel'] == 'biodiesel (b20)'
is_above_average = vehicles['best_mpge'] > 40
efficient_biodiesel = vehicles[is_biodiesel & is_above_average]
efficient_biodiesel.head()


# combining booleans with or:
is_ethanol = vehicles['fuel'] == 'ethanol (e85)'
is_methanol = vehicles['fuel'] == 'methanol'
combined = is_ethanol | is_methanol

ol_vehicles = vehicles[combined]
ol_vehicles.head()

is_electric = vehicles['fuel'] == 'electric'
gt_40 = vehicles['best_mpge'] > 40
electric_or_above_average = vehicles[is_electric | gt_40]

electric_or_above_average.head()


# Inverting booleans using not:

# Pandas uses the symbol ~ for not/non. 
# example:
# not_electric = ~electric

is_ford = vehicles['manufacturer'] == 'ford'
is_truck = vehicles['vehicle_type'] == 'pickup'
is_ford_truck = is_ford & is_truck
not_ford_truck = ~is_ford_truck

not_ford_truck_vehicles = vehicles[not_ford_truck]
not_ford_truck_vehicles.head()

is_chevrolet = vehicles['manufacturer'] == 'chevrolet'
is_gmc = vehicles['manufacturer'] == 'gmc'
is_chevrolet_gmc = is_chevrolet | is_gmc
not_chevrolet_gmc = ~is_chevrolet_gmc
not_chevrolet_gmc = vehicles[not_chevrolet_gmc]
not_chevrolet_gmc.head()