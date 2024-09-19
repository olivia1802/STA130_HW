#!/usr/bin/env python
# coding: utf-8

# <Prelecture>

# #1
# Explanation of the Monte Hall problem:
# 1. Initial choice:
# - there are 3 doors: one has a car(the prize), and the other two have goats
# - I choose one door
# - each door has a probability of 1/3 of having the car behind it
# 
# 2. Decision to switch:
# - there are 2 options: stick with my initial choice or switch to other unopened door
# - if I switch, winning probability becomes 2/3
# - initial choice was the car(1/3 chance) -> switching will cause me to lose
# - initial choice was a goat(2/3 chance) -> switching will give me the car

# Summary:
# 1. The player always chooses 1 door
# 2. The winning door is randomly chosen
# 3. Monte reveals a losing(where the goat is) door
# 4. THe player switches to the remaining door
# 5. If the new door is winning door, the player wins
# 6. This code is repeated 100,000 times to estimate the probability of winning by switching
# 
# The result (i_won / reps) shows the probability of winning is around 66.7%, and this aligns with the Monty Hall problem's solution. 
# 
# chaptGPT: https://chat.chatbotapp.ai/chats/-O6lufe4nKWdtEm9I3fQ?model=gpt-3.5

# #2
# Improved version of the code that chaptGPT provided:

# In[ ]:


import numpy as np

def monty_hall_simulation(reps=100000):
    wins_by_switching = 0
    all_doors = [1, 2, 3]  # List of doors

    for _ in range(reps):
        # Randomly choose the door with the car
        winning_door = np.random.choice(all_doors)
        # Randomly choose a door (contestant's initial choice)
        contestant_choice = np.random.choice(all_doors)

        # Determine the door to reveal (the door with a goat)
        doors_left = [door for door in all_doors if door != contestant_choice and door != winning_door]
        door_revealed = np.random.choice(doors_left)

        # Simulate switching by selecting the other unopened door
        # The remaining door is not the contestant's choice and not the revealed door
        remaining_doors = [door for door in all_doors if door != contestant_choice and door != door_revealed]
        contestant_choice = remaining_doors[0]  # Switch to the remaining door

        # Check if the contestant won by switching
        if contestant_choice == winning_door:
            wins_by_switching += 1

    win_rate = wins_by_switching / reps
    return win_rate

# Run the simulation and print the result
win_rate = monty_hall_simulation()
print(f"Win rate by switching: {win_rate:.2%}")


# I prefer the simplified version of the code that chatGPT provided since it is easier to understand. 
# Key differences are:
# 1. Uses all_doors = [1, 2, 3] as a list
# 2. Door is randomly selected each iteration
# 3. Removes the non-winning doors directly after comparing them with the contestant's choice
# 4. Switches to the remaining door directly after determining which door is revealed by the host
# 5. Filter doors using list comprehensions to handle edge cases
# 
# Overall, the first code is generally more concise and the second code is following step-by-step operations. 

# ChatGPT Summary: https://chatgpt.com/c/66e5e3ba-4ec4-800e-82e7-76b00063e7dd

# #3

# In[2]:


import numpy as np

def monty_hall_simulation(reps=100000): # defining function to work on monty hall problem
    wins_by_switching = 0 # set our initial value as 0
    all_doors = [1, 2, 3]  # List of doors

    for _ in range(reps): # defining function to work on for loops
        # Randomly choose the door with the car
        winning_door = np.random.choice(all_doors)
        # Randomly choose a door (contestant's initial choice)
        contestant_choice = np.random.choice(all_doors)

        # Determine the door to reveal (the door with a goat)
        # doors_left is not the contestant's choice as well as not the winning door
        # door is revealed randomly by importing np.random.choice() method
        doors_left = [door for door in all_doors if door != contestant_choice and door != winning_door]
        door_revealed = np.random.choice(doors_left)

        # Simulate switching by selecting the other unopened door
        # The remaining door is not the contestant's choice and not the revealed door
        remaining_doors = [door for door in all_doors if door != contestant_choice and door != door_revealed]
        contestant_choice = remaining_doors[0]  # Switch to the remaining door

        # Check if the contestant won by switching
        # If the contestant's choice is the winning door,
        # We inclement 1 of wins_by_switching
        if contestant_choice == winning_door: 
            wins_by_switching += 1
    # After going through the loop 100,000 times
    # Calculate the win rate by dividing wins_by_switching by reps
    # Used / instead of // to make sure that the answer is in decimal form
    # After calculation it returs the value stored in win_rate
    win_rate = wins_by_switching / reps
    return win_rate

# Run the simulation and print the result
win_rate = monty_hall_simulation()
print(f"Win rate by switching: {win_rate:.2%}")


# #4
# Markov Chain
# - stores word frequencies and the probabilities of transitions between words
# - allows to generate text by traversing the chain of words
# - it is based on their relative frequencies
# 
# 1. Use of defaultdict:
# - simplifies the code as defaultdict would automatically initialize dicitonary entries
# - avoiding the need to check word_used[word] and next_word[word]
# 
# 2. Building the Markov Chain:
# Updated code using defaultdict

# In[ ]:


from collections import defaultdict

word_used = defaultdict(int)  # Counts occurrences of each word
next_word = defaultdict(lambda: defaultdict(int))  # Counts transitions between words

for i, word in enumerate(words[:-1]):
    word_used[word] += 1  # Count the occurrence of the word
    next_word[word][words[i + 1]] += 1  # Count the transition to the next word


# ChatGPT Summary: https://chatgpt.com/c/66ea5555-e990-800e-9fab-30e38d91b403

# #5
# ChatGPT Summary of Q1&Q2: https://chatgpt.com/c/66ea5555-e990-800e-9fab-30e38d91b403
# ChatGPT Summary of Q3: 

# #6
# 1. ChatGPT was able to provide helpful answers to each of the above questions very quickly. However, sometimes I needed to give the chatbot some hints to get the exact answer I wanted. For the Monty Hall problem, the chatbot provided an improved version of the code and walked through the problem step by step. For the Markovian chatbot, ChatGPT was able to give me a detailed explanation, even with the more complicated extensions.
# 
# 2. Interacting with ChatGPT to figure things out was helpful. Without its assistance, I’m certain I wouldn’t have been able to understand how the code works, especially with advanced topics like nested_dict = lambda: defaultdict(nested_dict).
# 
# 3. Based on my experiences, ChatGPT was very helpful and made me understnad the code more clearly. When interpreting the code, there are some advanced topics that I cannot understand. Whenever I ask ChatGPT to provide me clear explanation on the code that I am confused about, ChatGPT always gave me a good explanation step by step. 

# #7
# 1. From my perspective, interacting with ChatGPT has boosted my confidence in learning coding, statistics, and data science. When I took the course ESC180, I wasn’t able to get much help from ChatGPT because we had to pass all the test cases to receive full marks for assignments, and ChatGPT wasn’t that helpful at the time. However, in STA130, I definitely think ChatGPT helped me a lot and made concepts much clearer. Overall, I feel that my perception of AI-driven assistance tools has evolved in a very positive way.
# 
# 2. Interacting with ChatGPT to figure things out was helpful. Without its assistance, I’m certain I wouldn’t have been able to understand how the code works, especially with advanced topics like nested_dict = lambda: defaultdict(nested_dict).
# 
# 3. Based on my experience, ChatGPT was very helpful in making the code clearer for me. When interpreting the code, there are some advanced topics I still struggle to understand. Whenever I ask ChatGPT for clarification on confusing parts of the code, it always provides a clear, step-by-step explanation.

# #8
# 3. 
# Topic: Data Science Careers in the Sports Field
# 
# Overview: We explored various career options where data science plays a crucial role in the sports field. The conversation highlighted how Olivia’s passion for sports can be combined with data science, offering insights into potential career paths.
# 
# Key Career Options Discussed:
# 
# 1. Sports Data Analyst: Focuses on collecting and analyzing game and player statistics to drive team decisions.
# 2. Performance Analyst: Analyzes player performance and physical conditioning using data from wearables and video footage.
# 3. Sports Data Scientist: Applies machine learning and predictive models to sports data for insights on performance, injuries, and business strategies.
# 4. Video/Match Analyst: Uses video footage to analyze tactics and player performance for strategic improvements.
# 5. Sports Operations Analyst: Focuses on operational aspects like ticket sales, fan engagement, and venue logistics.
# 6. Sports Agent/Data Consultant: Utilizes data to make informed decisions in contract negotiations and athlete management.
# 7. Fantasy Sports Analyst: Analyzes player statistics and trends for the fantasy sports community.
# 8. Sports Marketing Analyst: Uses data to analyze fan behavior and optimize marketing strategies.
# 9. Injury Prevention and Biomechanics Analyst: Analyzes athlete biomechanics to prevent injuries using data from wearable devices.
# 10. eSports Data Scientist/Analyst: Focuses on data analysis in the growing field of competitive gaming (eSports).
# 
# Conclusion: The careers discussed combine sports and data science in ways that can influence athlete performance, team strategy, business operations, and fan engagement, providing multiple pathways depending on Olivia's specific interests within sports.
# 
# https://chatgpt.com/c/66eb8a8d-9cd0-800e-b706-7fd166ac3238

# 4. 
# Reflecting on my recent exploration of data science careers in the sports field, I am excited about the range of opportunities available that align with both my passion for sports and my interest in data science. It is clear that data plays crucial role in shaping the future of sports, influencing everything from player performance to business operations. 
# 
# I am particularly interested in roles like Sports Data Analyst and Performance Analyst, where I could directly impact team strategy and athlete performance through data-driven insights. To achieve my long-term aspirations, I need to focus on building technical skills in areas like data analysis, machine learning, and possibly even video analytics. Coding skills are must, and thorough understanding of sports-specific technologies like wearable data systems would be required. I am hoping to volunteer for FIFA World Cup 2026, which is happening in Toronto. 

# 5. Conversation with ChatGPT was helpful and it gave me more detailed mental concept about what I want to do in the future, and what I need to do if I want to achieve that. I was also surprised that there are huge potential of sports field with variety of career opportunities. 
