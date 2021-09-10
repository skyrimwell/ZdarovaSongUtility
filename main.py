import lyricsgenius as lg

file= open("song1.txt" , "a")
file2= open("song2.txt" , "a")
genius = lg.Genius('d7nKnf5f_foFmU7URjdw-8p6JMfMY_RC67EIe68--0ykmn-pjOXBk-7YNFexEwRl',
                   skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"],
                   remove_section_headers=True)
artists = ['Metallica', 'Ghost B.C.']


def start():
    print("Чего изволите?" "\n" "1 - Вывод топа песен группы" "\n" "2 - Поиск группы по треку")
    a = input()
    if a== '1':
        get_lyrics(artists, 5)
    elif a== '2':
        get_lyrics_by_song()


def get_lyrics(arr, k):
    c = 0
    for name in arr:
        try:
            songs = (genius.search_artist(name, max_songs=k, sort='popularity')).songs
            s = [song.lyrics for song in songs]
            file.write("\n \n   <|endoftext|>   \n \n".join(s))
            c += 1
            print(f"Количество песен:{len(s)}")
        except:
            print(f"проблемы с: {name}: {c}")


def get_lyrics_by_song():
    title = input()
    onesong = (genius.search_song(title=title)).artist
    print(f"Автор: {onesong}")
    file2.write("".join(genius.search_song(title=title).lyrics))
    file2.write("\n \n")


start()