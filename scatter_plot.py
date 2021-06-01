#!/usr/bin/env python3

import matplotlib.pyplot as pyplot

# Create data
cities = ('Bristol', 'Cardiff', 'Bath', 'Liverpool', 'Glasgow', 'Edinburgh', 'Leeds', 'Reading', 'Swansea', 'Manchester')
population = [617280, 447287, 94782, 864122, 591620, 464990, 455123, 318014, 300352, 395515]

# Plot the data
pyplot.scatter(x=cities, y=population, c='g', marker='o')

# Configure graph
pyplot.xlabel('Cities', fontsize=9)
pyplot.ylabel('Population', fontsize=8)
pyplot.title('Cities in the UK and their populations', fontsize=12)
pyplot.xticks(cities, rotation=45, fontsize=8)

# Display the chart
pyplot.show()

