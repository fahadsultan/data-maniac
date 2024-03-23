import json
with open('mjTopTracks.json') as f: 
    songs = json.loads(f.read())
    
def most_popular_song_finder(songs_list:list) -> str():
    """Returns a tuple of the most popular song and the title"""
    max_popularity = int(songs_list[0]['popularity'])
    max_popularity_title = songs_list[0]['title']
    for song in songs_list:
        if int(song['popularity']) > max_popularity:
            max_popularity = (song['popularity'])
            max_popularity_title = song['title']
    return max_popularity, max_popularity_title

def least_popular_song_finder(songs_list:list) -> str():
    """Returns a tuple of the least popular song and title"""
    min_popularity = int(songs_list[0]['popularity'])
    min_popularity_title = songs_list[0]['title']
    for song in songs_list:
        if int(song['popularity']) < min_popularity:
            min_popularity = (song['popularity'])
            min_popularity_title = song['title']
    return min_popularity, min_popularity_title

def most_popular_explicit(songs_list:list) -> list():
    """Returns the most popular explicit song information"""
    explicit_list = []
    for song in songs_list:
        if song['explicit'] == True:
            explicit_list.append(song)
    for explicit_song in explicit_list:
        max_pop_explicit = most_popular_song_finder(explicit_list)
    return(max_pop_explicit)

def most_popular_non_explicit(songs_list:list) -> list():
    """Returns the most popular clean song information"""
    non_explicit_list = []
    for song in songs_list:
        if song['explicit'] == False:
            non_explicit_list.append(song)
    for non_explicit_song in non_explicit_list:
        max_pop_explicit = most_popular_song_finder(non_explicit_list)
    return(max_pop_explicit)

def generals_genres (lst:list) -> list():
    """ Returns the all the genres """
    genre = []
    for song in songs:
        genre += (song['genres'])
    return genre

def find_unique_genres (lst: list) -> list():
    """ Returns all the unique genres """
    unique = []
    for item in lst:
            if not item in unique:
                unique.append(item)
    return "There were " + str (len (unique))+ " Unique genres"

def all_artists (song):
    """ Returns all the artists """
    artists = []
    for song in songs:
        artists += (song['artists'])
    return artists

def count_songs(lst: list) -> dict: 
    """Returns the number of times each element appeared in lst""" 
    el_counts = {}
    for element in lst:
        if element in el_counts:
            el_counts[element] += 1
        else:
            el_counts[element] = 1
    return el_counts

def elements_swapped (number_counts: list) -> dict: 
    """ Swaps the dictionary around, where the values are keys and the keys are values """
    number_counts_swapped = {}
    for number, count in number_counts.items():
        if count in number_counts_swapped:
            number_counts_swapped[count].append(number)
            number_counts_swapped[count].sort()
        else:
            number_counts_swapped[count] = [number]
    for count, number_list in sorted(number_counts_swapped.items(), reverse=True):
        for number in number_list:
            return('{} appeared {} time(s) in the Top Tracks'.format(number, count))
def main():
#About the Artists
     artist_list = all_artists(songs)
     songs_counted = (count_songs(artist_list))
     print (elements_swapped(songs_counted))
#About the Genres
     all_genres = (generals_genres(songs))
     unique_genres = (find_unique_genres(all_genres))
     print (unique_genres)
#About the Songs
     print ("The most Popular song is " + str (most_popular_song_finder(songs)))
     print ("The least Popular song is " + str (least_popular_song_finder(songs)))
     print ("The most Popular Explicit song is " + str (most_popular_explicit(songs)))
     print ("The most Popular Non-Explicit song is " + str (most_popular_non_explicit(songs)))
     
    
if __name__ == '__main__':
    main()
                    