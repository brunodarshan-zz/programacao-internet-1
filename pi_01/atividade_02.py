import requests

def main():
    response = requests.get('https://i2.wp.com/cwalocal4009.org/wp-content/uploads/2017/01/spoc.jpg')
    if (response.status_code == 200):
        fl = open('image.jpg', 'wb+')
        fl.write(response.content)
        fl.close()

if __name__ == '__main__':
    main()