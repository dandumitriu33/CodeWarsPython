def song_decoder(song):
    g = song.replace('WUB', ' ')
    return ' '.join(g.split())


print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))