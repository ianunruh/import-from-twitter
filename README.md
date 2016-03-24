# import-from-twitter

Don't trust PyPI for some reason? That's ok, now you can rely on Twitter for your dependencies!

Inspired by [require-from-twitter](https://gist.github.com/rauchg/5b032c2c2166e4e36713).

## Usage

First, hop on over to [Twitter Developers](https://dev.twitter.com/oauth/overview/application-owner-access-tokens) and
get an API key for Twitter. Throw those keys into `config.json` in your working directory.

```bash
pip install git+https://github.com/ianunruh/import-from-twitter.git
```

Then import `ift` and start importing modules from Twitter today! For example, use my
[left_pad module](https://twitter.com/ianunruh/status/713091939805966337).

```python
import ift
mymodule = ift.import_from_twitter('713091939805966337')

print(mymodule.left_pad('helloworld', 15)) # => "     helloworld"
```
