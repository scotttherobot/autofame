import pytumblr, os, random, time

# Make sure these folders are created in the PWD
# or make them absolute paths. Photos will be moved from
# the source folder to the posted folder when they have been
# posted to the Tumblr API
source_folder = 'selfies'
posted_folder = 'posted'
# The blog name you want to post to
blog_name = ''
# Options include 'queue', 'post', and 'draft'
post_state = 'queue'
# The text to accompany the photograph
post_caption = 'herp derp selfies?'
# omg this is the list of #hashtags to use
post_tags = [
      "selfie",
      "selfies",
      "selfie game",
]
# The time between posts, since the API docs don't really
# mention a rate limit. So I'm self-imposing one.
post_delay = 5

client = pytumblr.TumblrRestClient(
   '<consumer key>',    # Your app's consumer API key
   '<consumer secret>', # Your app's consumer secret
   '<oauth token>',     # The token you got from the console
   '<oauth secret>',    # The secret you got from the console
)

files = os.listdir(source_folder)
# Shuffle the files for fun!
random.shuffle(files)

print str(len(files)) + " files to queue."

for file in files:
   print "Posting " + file + "..."
   full_path = source_folder + "/" + file
   done_path = posted_folder + "/" + file
   try:
      client.create_photo(
            blog_name,
            state = post_state,
            tags = post_tags,
            data = full_path,
            caption = post_caption
      )
      print "Moving " + full_path + " to " + done_path
      os.rename(full_path, done_path)
   except IOError:
      print "IOError caught. Maybe that was a folder?"
   print "Sleeping for " + str(post_delay) + " seconds for rate limiting"
   time.sleep(post_delay)
