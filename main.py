from parser.views import AnnouncementParser


def main():
    page = 1
    while True:
        print(f'страница {page} загружается ...')
        url = f'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/page-{page}/c37l1700273'
        parser = AnnouncementParser(url)
        parser.get_data()
        print(f'{page} страница загружена ...')
        if not parser.find_button_next():
            break
        page += 1


if __name__ == '__main__':
    main()