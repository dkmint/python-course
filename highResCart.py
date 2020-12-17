plt.figure(figsize = (10, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines(resolution = '10m')
ax.set_extent([-122.8, -122, 37.3, 38.3])

# we can add high-resolution land and water
LAND = cfeature.NaturalEarthFeature('physical', 'land', '10m', 
                                    edgecolor = 'face',
                                    facecolor = cfeature.COLORS['land'],
                                    linewidth = .1)
OCEAN = cfeature.NaturalEarthFeature('physical', 'ocean', '10m', 
                                    edgecolor = 'face',
                                    facecolor = cfeature.COLORS['water'],
                                    linewidth = .1)

ax.add_feature(LAND, zorder = 0)
ax.add_feature(OCEAN, zorder = 0)

plt.show()
