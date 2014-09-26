#### Autofame

Ever wanted to be tumblr famous for your selfies? Me too! But it takes so much effort.
With this script, you can just collect up all your selfies and have them automatically
posted to your tumblr. The fame will find you!

For more, see [the blog post](http://scottvanderlind.com/weekday-project-autofame/)
that I wrote about it.


##### Running

First, clone the repo using the link in the sidebar. Then, run the bash script
`setup.sh` (included), which will create two subfolders and install the
`pytumblr` dependency using pip.

Load the `selfies` folder with your glamor shots, plug in your oAuth credentials
in the `tumble.py` script as well as your tumblr name, a post caption, the tags
you want to go with each post, and if you want you can adjust the post delay
(which I used as a API rate-limiter).

Then, run the script with `python tumble.py` and sit back and watch it do the do.
There IS one race condition that I know of which could cuase double-posting
if you run more than one instance at a time. This is because the script lists
the directory contents first thing instead of grabbing photos one by one. So
don't do that.
