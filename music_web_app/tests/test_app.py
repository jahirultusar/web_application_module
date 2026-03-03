"""
Call POST 
"""

# POST /albums
#    title: Hyperspace Sunrise
#    release_year: 2038
#    artist_id: 1
#  Expected response (200 OK):
"""
No Content Returns
"""

# GET /albums
#  Expected response (200 OK):
"""
Returns:
Albums(1, 'Hyperspace Sunset', 2035, 1)
Albums(2, 'Hyperspace Sunrise', 2038, 1)
"""

# POST /albums
# Expected response (400 Bad Request):
"""
You need to Submit a title, realease year and title
"""