import numpy as np
#Given the prices, quantities, change in prices, and change in quantities, one would derive elasticities for each good
#Obviously the only limitation to the model is finding the neccessary data

#The vector of elasticities for A
#For cross-section, represents elasticity for location A for n goods
MarketA = []
#The Vector of elasticities for B
#For Cross-section, represents elasticity for location B for n goods
MarketB = []
OutputMarket = []

OutputMarket = [a - b for a, b in zip(MarketA, MarketB)]
OutputMarket = [abs(x) for x in OutputMarket]
OutputMarket = [np.log(x) for x in OutputMarket]

#The greater the value of the output, the more opportunity for arbitrage exist in said market/good
print(OutputMarket)