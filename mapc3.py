import cartopy.feature as cfeature

plt.figure(figsize = (10, 5))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()
ax.set_extent([-125, -75, 25, 50])

ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.STATES, linestyle = ':')
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAKES, alpha = 0.5)
ax.add_feature(cfeature.RIVERS)

plt.show()
