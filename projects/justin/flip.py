import random
import matplotlib.pyplot as plt\


def flip_coin() -> int:
  return random.randint(0, 1)


def fill_coin_results(coin_results, epochs):
  for player, results in coin_results.items():
    for _ in range(epochs):
      results.append(flip_coin())


coin_results = {
    1: [],
    2: []
}

fill_coin_results(coin_results, 10)

# create a histogram with 2 bins (one for each player) and only 0 and 1 as possible values
plt.hist(coin_results.values(), bins=2, range=(0, 1), label=coin_results.keys())
plt.legend()
plt.show()