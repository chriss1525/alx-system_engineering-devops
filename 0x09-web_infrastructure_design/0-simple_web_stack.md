# Simple Web Stack Wireframe

[simple webs stack wireframe](https://photos.app.goo.gl/wWndJM7zJ6TpMaWj6)

When a user types "www.Foobar.com" on their browser, several things happen before they get a response.

- Firstly, the browser's request is sent to the DNS server.
- The DNS server then resolves the domain name to an IP address, in this case the IP address is 8.8.8.8.
- After the domain name and IP address is resolved, the DNS responds back to the user's browser with the IP address.
- Now the browser can send a HTTP request to a server.
- This request is caught by a Nginx server, that acts as our load bearer. This server acts as a barrier between the main app server and the client and it filters information given to it.
- From the nginx server, the request is seant to the main app server.
- When the request gets to the main app server, the server queries data from the MYSQL data getting the required data.
- this data taken from th database then travels back up the ladder, passing throuhg the Nginx server to the user's browser.
