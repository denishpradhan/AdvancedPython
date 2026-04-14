from Day6functions1hr import greet
greet("time", "name", "status")


def ProfileGenarator(name, age, gender, professsion, faviorate_music_genre, bio, top10_favourate_songs, Releases, favourate_artists):
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    profession = input("Enter your profession: ")
    faviorate_music_genre = input("Enter your favorite music genre: ")
    bio = input("Write a short bio about yourself: ")
    top10_favourate_songs = input(
        "List your top 10 favorite songs (separated by commas): ")
    releases = input(
        "List your recent releases (if any, separated by commas): ")
    favourate_artists = input(
        "List your favorite artists (separated by commas): ")
    print("\n🎤 Musician Profile:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Gender: {gender}")
    print(f"Profession: {profession}")
    print(f"Favorite Music Genre: {faviorate_music_genre}")
    print(f"Bio: {bio}")
    print(f"Top 10 Favorite Songs: {top10_favourate_songs}")
    print(f"Recent Releases: {releases}")
    print(f"Favorite Artists: {favourate_artists}")
    print("\nWelcome to our Musicians Community! You ahve sucessfully created your profile. Let's connect with other musicians and share your passion for music!")
