def climbingLeaderboard(ranked, player):
    # Write your code here
    places = []
    ranked = set(ranked)
    ranked = list(ranked)
    ranked.sort(reverse=True)
    player.sort(reverse=True)
    i, j = 0
    pos = 1

    while j < len(places):
      r = ranked[i]
      p = player[j]

      if (p >= r):
        places.append(pos)
        j += 1
        pos += 1
      elif (p < r and i == len(ranked)):
        pos += 1
        places.append(pos)
      else:
        i += 1
      


    return places
