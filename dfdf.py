dict = {
  "books": [
    {
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee",
      "published": "1960",
      "genre": "Southern Gothic",
      "rating": 4.27
    },
    {
      "title": "1984",
      "author": "George Orwell",
      "published": "1949",
      "genre": "Dystopian",
      "rating": 4.19
    }
  ]
}


print(dict.get('books')[0]['title'])