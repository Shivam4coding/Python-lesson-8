"""
1) Add the project title.
   a) Use a comment to label the program as "Recipe Explorer".

2) Create tuples for recipe details.
   a) Store pasta details in a tuple.
   b) Store biryani details in a tuple.
   c) Print recipe details using index positions.

3) Use nested tuples and slicing.
   a) Store both recipe tuples inside one tuple.
   b) Access details from nested tuples.
   c) Use slicing to print selected pasta details.

4) Iterate through a tuple.
   a) Use a `for` loop to go through each pasta detail.
   b) Print each detail one by one.

5) Create sets for ingredients.
   a) Store pasta ingredients in a set.
   b) Store biryani ingredients in a set.
   c) Show that duplicate ingredients are not repeated.
   d) Use `len()` to count ingredients.

6) Modify a set.
   a) Use `add()` to add a new ingredient.
   b) Use `discard()` to remove an ingredient.

7) Perform set operations.
   a) Use `union()` to combine all ingredients.
   b) Use `intersection()` to find common ingredients.
   c) Use `difference()` to find ingredients only in pasta.
   d) Use `symmetric_difference()` to find ingredients not shared.
"""

# "Recipe Explorer"

pasta = ("Pasta Arabbiata", "Italian", 20, "medium")
biryani = ("Biryani", "Indian", 45, "hard")

print("Pasta Recipe Details:")
print("Name:", pasta[0])
print("Cuisine:", pasta[1])
print("Difficulty level:", pasta[-1])

all_recipes = (pasta, biryani)

print("All recipes:", all_recipes[0][0])
print("All recipes:", all_recipes[1][0])

print("Pasta Details (Sliced):", pasta[1:3])

for detail in pasta:
    print(detail)

pasta_ingredients = {"pasta", "tomato sauce", "garlic", "garlic", "olive oil", "basil"}
biryani_ingredients = {"biryani", "yogurt", "lemon juice", "salt", "salt", "pepper"}

print("Pasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)


print( "Length of Pasta Ingredients:", len(pasta_ingredients))
print("Length of Biryani Ingredients:", len(biryani_ingredients))

pasta_ingredients.add("tomato")
biryani_ingredients.discard("salt")

print("Pasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
print("All Ingredients:", all_ingredients)

common_ingredients = pasta_ingredients.intersection(biryani_ingredients)
print("Common Ingredients:", common_ingredients)

difference_ingredients = pasta_ingredients.difference(biryani_ingredients)
print("Difference Ingredients:", difference_ingredients)

symmetric_difference_ingredients = pasta_ingredients.symmetric_difference(biryani_ingredients)  
print("Symmetric Difference Ingredients:", symmetric_difference_ingredients)
