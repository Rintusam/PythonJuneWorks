placements={"testing":45,"python":25,"asp":64,"bigdata":56,"java":60}


srt=sorted(placements,key=lambda key: placements.get(key),reverse=True)
print(srt)
