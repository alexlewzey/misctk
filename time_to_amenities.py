import webbrowser
import fire


def load_distance(start: str, destination: str) -> None:
    start, destination = '+'.join(start.split()), '+'.join(destination.split())
    url = fr"""https://www.google.com/maps/dir/{start}/{destination}"""
    webbrowser.open(url)


def open_distances_in_gmap(start) -> None:
    for dst in ['Stockport Train Station', 'Aldi', 'Lidl', 'Levenshulme Train Station']:
        load_distance(start, dst)


if __name__ == '__main__':
    fire.Fire(open_distances_in_gmap)
