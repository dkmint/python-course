plt.figure(figsize = (10, 8))

# plot the map related stuff
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution = '10m')
ax.set_extent([-122.8, -122, 37.3, 38.3])

# we can add high-resolution land and water
# LAND = cfeature.NaturalEarthFeature('physical', 'land', '10m', 
#                                     edgecolor = 'face',
#                                     facecolor = cfeature.COLORS['land'],
#                                     linewidth = .1)
# OCEAN = cfeature.NaturalEarthFeature('physical', 'ocean', '10m', 
#                                     edgecolor = 'face',
#                                     facecolor = cfeature.COLORS['water'],
#                                     linewidth = .1)

ax.add_feature(LAND, zorder = 0)
ax.add_feature(OCEAN, zorder = 0)

# plot the data related stuff
berkeley_lon, berkeley_lat = -122.2585, 37.8719
stanford_lon, stanford_lat = -122.1661, 37.4241

# plot the two universities as blue dots
ax.plot([berkeley_lon, stanford_lon],
       [berkeley_lat, stanford_lat],
       color = 'blue', linewidth = 2, marker = 'o')

# add labels for the two universities
ax.text(berkeley_lon + .16, berkeley_lat - 0.02,
       'US Berkeley', horizontalalignment = 'right')

ax.text(stanford_lon + 0.02, stanford_lat - 0.02,
       'Stanford', horizontalalignment = 'left')
plt.show()
