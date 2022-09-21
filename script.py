import tidalapi
session = tidalapi.Session()
# Will run until you visit the printed url and link your account
session.login_oauth_simple()
album = session.album(66236918)
tracks = album.tracks()
#for track in tracks:
#    print(track.name)

playlist = tidalapi.playlist.UserPlaylist(playlist_id='41c39407-25d9-4744-99ed-0163cd2c5fa9', session=session)
for track in playlist.items():
    print(track.name)
print(playlist)
