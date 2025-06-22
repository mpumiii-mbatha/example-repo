import random     # Random module used for the choice function to work

# Jokes taken from website https://www.goodhousekeeping.com/life/entertainment/a63383080/funny-jokes/

questions_list = ["Do you want to hear a pizza joke?", "What did the buffalo say when his son left?", "What do you call a cold dog?", "What do cakes and baseball teams have in common?", "Where do polar bears keep their money?", "Why did the scarecrow win an award?"]
jokes_list = ["Nahhh, it's too cheesy", "Bison!", " A chili dog.", "They both need a good batter", "In a snow bank.", "Because he was outstanding in his field."]  


zip_list = list(zip(questions_list, jokes_list))  # Use the zip function to pair both lists, in the correct order
random_joke = random.choice(zip_list)             # Use the choice function to randomly select an element from the paired list

questions_list, jokes_list = random_joke          # Unpack the list

print(f"{questions_list} {jokes_list}")