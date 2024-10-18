sec = int(input())

hours = int(sec / 3600)
minutes = int((sec-(hours*3600)) / 60)
secounds = int(sec-((hours*3600)+(minutes*60)))

print(f'{hours}:{minutes}:{secounds}')s