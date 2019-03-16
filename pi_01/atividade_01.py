import requests

def header_format(headers):
    print("-----Response Headers-----")
    for header in headers:
        print(header, ": ", headers[header])


def main():
    response = requests.get('https://api.github.com/users/brunodarshan')
    print(response.status_code)
    header_format(response.headers)
    # print(response.content_length)
    print(response.text)

if __name__ == "__main__":
    main()