mu = 5; sigma = 2
mu + sigma * np.random.randn(5) # scaled random numbers
x1 = np.random.randn(1000)
x2 = mu + sigma * np.random.randn(1000)
plt.figure(figsize=(10,6))
plt.hist(x1, bins = 20, alpha = 0.4)
plt.hist(x2, bins = 20, alpha = 0.4)
plt.show()
