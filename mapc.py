import cartopy.crs as ccrs
import matplotlib.pyplot as plt
%matplotlib inline

plt.figure(figsize = (12, 8))
ax = plt.axes(projection = ccrs.PlateCarree())
ax.coastlines()
ax.stock_img()
ax.gridlines(draw_labels = True)
plt.show()
