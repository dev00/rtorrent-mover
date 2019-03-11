import bencode
import os

session_folder = '/home/user/session'
old_dl = '/var/www/downloads/'
new_dl = '/downloads/completed/'

files = [f for f in os.listdir(session_folder) if f.endswith('.rtorrent')]

for torrent_file in files:
  with open(os.path.join(session_folder,torrent_file), 'rb') as f:
    decoded = bencode.decode(f.read())
    decoded['directory'] = decoded['directory'].replace(old_dl, new_dl)
    newfile = open(os.path.join(session_folder, 'new', torrent_file), 'w')
    newfile.write(bencode.encode(decoded))
    newfile.close()
