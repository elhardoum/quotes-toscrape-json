## Quotes to Scrape - JSON

This quick script will scrape quotes from ScrapingHub's scraping site [quotes.toscrape.com](http://quotes.toscrape.com). The only difference is, you skip all the scraping work and get a JSON object of the quotes available in the page you passed, as well as the pagination links.

Just pass the quotes page full URL after your http server's web address, example below.

### Example

```bash
$ curl -s http://0.0.0.0:8083/http://quotes.toscrape.com/ | jq .
{
  "success": true,
  "items": [
    {
      "text": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”",
      "author": "Albert Einstein",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/change/page/1/",
          "text": "change"
        },
        {
          "link": "http://quotes.toscrape.com/tag/deep-thoughts/page/1/",
          "text": "deep-thoughts"
        },
        {
          "link": "http://quotes.toscrape.com/tag/thinking/page/1/",
          "text": "thinking"
        },
        {
          "link": "http://quotes.toscrape.com/tag/world/page/1/",
          "text": "world"
        }
      ]
    },
    {
      "text": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”",
      "author": "J.K. Rowling",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/abilities/page/1/",
          "text": "abilities"
        },
        {
          "link": "http://quotes.toscrape.com/tag/choices/page/1/",
          "text": "choices"
        }
      ]
    },
    {
      "text": "“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”",
      "author": "Albert Einstein",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/inspirational/page/1/",
          "text": "inspirational"
        },
        {
          "link": "http://quotes.toscrape.com/tag/life/page/1/",
          "text": "life"
        },
        {
          "link": "http://quotes.toscrape.com/tag/live/page/1/",
          "text": "live"
        },
        {
          "link": "http://quotes.toscrape.com/tag/miracle/page/1/",
          "text": "miracle"
        },
        {
          "link": "http://quotes.toscrape.com/tag/miracles/page/1/",
          "text": "miracles"
        }
      ]
    },
    {
      "text": "“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”",
      "author": "Jane Austen",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/aliteracy/page/1/",
          "text": "aliteracy"
        },
        {
          "link": "http://quotes.toscrape.com/tag/books/page/1/",
          "text": "books"
        },
        {
          "link": "http://quotes.toscrape.com/tag/classic/page/1/",
          "text": "classic"
        },
        {
          "link": "http://quotes.toscrape.com/tag/humor/page/1/",
          "text": "humor"
        }
      ]
    },
    {
      "text": "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”",
      "author": "Marilyn Monroe",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/be-yourself/page/1/",
          "text": "be-yourself"
        },
        {
          "link": "http://quotes.toscrape.com/tag/inspirational/page/1/",
          "text": "inspirational"
        }
      ]
    },
    {
      "text": "“Try not to become a man of success. Rather become a man of value.”",
      "author": "Albert Einstein",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/adulthood/page/1/",
          "text": "adulthood"
        },
        {
          "link": "http://quotes.toscrape.com/tag/success/page/1/",
          "text": "success"
        },
        {
          "link": "http://quotes.toscrape.com/tag/value/page/1/",
          "text": "value"
        }
      ]
    },
    {
      "text": "“It is better to be hated for what you are than to be loved for what you are not.”",
      "author": "André Gide",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/life/page/1/",
          "text": "life"
        },
        {
          "link": "http://quotes.toscrape.com/tag/love/page/1/",
          "text": "love"
        }
      ]
    },
    {
      "text": "“I have not failed. I've just found 10,000 ways that won't work.”",
      "author": "Thomas A. Edison",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/edison/page/1/",
          "text": "edison"
        },
        {
          "link": "http://quotes.toscrape.com/tag/failure/page/1/",
          "text": "failure"
        },
        {
          "link": "http://quotes.toscrape.com/tag/inspirational/page/1/",
          "text": "inspirational"
        },
        {
          "link": "http://quotes.toscrape.com/tag/paraphrased/page/1/",
          "text": "paraphrased"
        }
      ]
    },
    {
      "text": "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”",
      "author": "Eleanor Roosevelt",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/misattributed-eleanor-roosevelt/page/1/",
          "text": "misattributed-eleanor-roosevelt"
        }
      ]
    },
    {
      "text": "“A day without sunshine is like, you know, night.”",
      "author": "Steve Martin",
      "tags": [
        {
          "link": "http://quotes.toscrape.com/tag/humor/page/1/",
          "text": "humor"
        },
        {
          "link": "http://quotes.toscrape.com/tag/obvious/page/1/",
          "text": "obvious"
        },
        {
          "link": "http://quotes.toscrape.com/tag/simile/page/1/",
          "text": "simile"
        }
      ]
    }
  ],
  "pagination": {
    "url_previous": null,
    "url_next": "http://quotes.toscrape.com/page/2/"
  }
}
```

### Install

```bash
# create a virtual env
virtualenv -p python3 env

# install dependencies (bs4 and requests)
./env/bin/pip install -r requirements.txt

# run server
./env/bin/python server.py
```

### Further traits

```
# Run forever in the background
nohup sh -c './env/bin/python server.py' &

# Get a public web address to run your scraper (using ngrok proxy)
ngrok http 8083 # pass whatever port you used
```

### Notes

This was originally created as a practical resource for an upcoming ES6 workshop (Promises).
