from youtube import test
from spotify import playlist_tracks


def main():
    query_tracks = playlist_tracks()
    print(query_tracks)

if __name__ == "__main__":
    main()
    test()

