#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    if len(recipe) != len(ingredients):
        return 0
    else:
        recipe = [recipe]
        ingredients = [ingredients]
        rNums = []
        iNums = []
        for i in range(len(recipe)):
            for i, j in recipe[i].items():
                rNums.append(j)

        for i in range(len(ingredients)):
            for i, j in ingredients[i].items():
                iNums.append(j)

        for i in range(len(rNums)):
            rNums[i] = iNums[i]//rNums[i]

        return min(rNums)

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
