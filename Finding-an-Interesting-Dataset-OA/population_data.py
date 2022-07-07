import pandas

pandas.options.display.max_columns = None
pandas.options.display.max_rows = None

Population_data = pandas.read_csv("world_population_by_country.csv")

print(Population_data)