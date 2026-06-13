 #!/bin/bash
   container run --rm -it --name blog -p 4000:4000 -v "$PWD":/srv/jekyll blog-jekyll
