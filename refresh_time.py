from datetime import datetime, timedelta


def get_current_time():
    current_time = datetime.now() + timedelta(hours=3)
    return current_time.strftime(
        'Last refresh: %a %b %d %H:%M:%S on profile\n'
        )


if __name__ == '__main__':
    with open('README.md', 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(
            lines[:12] + [get_current_time()] + lines[13:]
            )
