http://127.0.0.1:8000/api/register
registers the user using the username and password, format of the body: {username: ”testuser”, password: 123123}
when user gets created the a new client is also created by the signals

http://127.0.0.1:8000/api/works
this endpoint will diplay list(query) all work table fields. It contains id, Link and worktype

http://127.0.0.1:8000/api/works?artist=[Artist Name]
this endpoint will filter the artist accordting to the artist name

http://127.0.0.1:8000/api/works?work_type=Youtube or pk of YouTube
this endpoint will filter the result according to the choice provided in the query string