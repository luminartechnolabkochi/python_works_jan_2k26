

movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]



languages_list = [m[3] for m in movies]

language_count = {l:languages_list.count(l) for l in languages_list}

language_count_list = [[v,k] for k,v in language_count.items()]

print(sorted(language_count_list,reverse=True)[0])


# list of dictionary => comprehension

# display all movie title

# all_movie_title = [lst[1] for lst in movies ]
# # print(all_movie_title)

# # movie with top rating
# max_rating = max([lst[4] for lst in movies])

# top_movies = [lst[1] for lst in movies if lst[4]==max_rating]
# print(top_movies)

# display kannada movies
# display movies where actor is yash
# which language most number of movies all_lang=["k","m","k","t"]
# movie with max budget
# languages