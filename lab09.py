import requests

r = requests.get('http://172.25.0.29/index.php')

web_headers = r.headers
print("Here are the headers returned:")
print (web_headers)

web_html = r.text
print("Here is the HTML returned in the body of the webpage:")
print (web_html)

web_status_code = r.status_code
print(" Here is the HTTP Status Code returned:")
print(web_status_code)

web_cookies = r.cookies
print("Here are the cookies returned from the page:")
print(web_cookies)
