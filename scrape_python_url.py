# $ pip3 install requests beautifulsoup4
import requests, bs4, os, sys

try:
    response   = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
    document   = bs4.BeautifulSoup(response.text, 'html.parser')
    table      = document.find('table', class_='infobox vevent')
    python_url = table.find('th', text='Website').next_sibling.a['href']
    logo_url   = table.find('img')['src']
    logo       = requests.get(f'https:{logo_url}').content
    filename   = os.path.basename(logo_url)
    with open(filename, 'wb') as file:
        file.write(logo)
    print(f'{python_url}, file://{os.path.abspath(filename)}')
except requests.exceptions.ConnectionError:
    print("You've got problems with connection.", file=sys.stderr)

