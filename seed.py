from api_olympic_history.models import Region, Noc, Team, Sport, Event, Athlete, Medal, Game, AthleteEvent
import pandas as pd
import numpy as np

regions_csv = pd.read_csv('noc_regions.csv')

regions1 = regions_csv['region'].dropna(axis='index').unique()
regions2 = regions_csv[regions_csv['region'].isna()]
regions3 = regions_csv[regions_csv['notes'].notna()].dropna(axis='index')

print('Populando Region')
for region in regions1:
    r = Region(name=region, note=None)
    r.save()

for region in regions2.iloc():
    r = Region(name=None, note=region['notes'])
    r.save()

for region in regions3.iloc():
    r = Region(name=region['region'], note=region['notes'])
    r.save()
print('Ok')

regions_csv = regions_csv.fillna('')

print('Populando Noc')
for noc_region in regions_csv.iloc():
    region_name = None if noc_region['region'] == '' else noc_region['region']
    note = None if noc_region['notes'] == '' else noc_region['notes']
    region = Region.objects.get(name=region_name, note=note)
    n = Noc(flag=noc_region['NOC'], region=region)
    n.save()


athlete_events_csv = pd.read_csv('athlete_events.csv')

regions_nocs = regions_csv['NOC'].unique()

for noc in athlete_events_csv['NOC'].unique():
    if noc not in regions_nocs:
        n = Noc(flag=noc)
        n.save()
print('OK')

teams = athlete_events_csv.drop_duplicates(subset=['Team'])[['Team', 'NOC']]

print('Populando Team')
for team in teams.iloc():
    noc = Noc.objects.get(flag=team['NOC'])
    t = Team(name=team['Team'], noc=noc)
    t.save()
print('OK')

games = athlete_events_csv['Games'].unique()

print('Populando Game')
for game in games:
    arr = game.split(' ')
    g = Game(season=arr[1], year=arr[0])
    g.save()
print('OK')

medals = athlete_events_csv['Medal'].unique()
medals = [None if x is np.nan else x for x in medals]

print('Populando Medal')
for medal in medals:
    m = Medal(type=medal)
    m.save()
print('OK')

sports = athlete_events_csv['Sport'].unique()

print('Populando Sport')
for sport in sports:
    s = Sport(name=sport)
    s.save()
print('OK')

events = athlete_events_csv.drop_duplicates(subset=['Event'])[
    ['Event', 'Sport']]

print('Populando Event')
for event in events.iloc():
    sport = Sport.objects.get(name=event['Sport'])
    e = Event(name=event['Event'], sport=sport)
    e.save()
print('OK')

athletes = athlete_events_csv.drop_duplicates(subset=['Name'])[['Name', 'Sex']]

print('Populando Athlete')
for athlete in athletes.iloc():
    a = Athlete(name=athlete['Name'], sex=athlete['Sex'])
    a.save()
print('OK')

print('Populando AthleteEvent')
for athlete_event in athlete_events_csv.iloc():
    athlete = Athlete.objects.get(name=athlete_event['Name'])
    event = Event.objects.get(name=athlete_event['Event'])
    game = Game.objects.get(
        season=athlete_event['Season'], year=int(athlete_event['Year']))
    medal_type = None if athlete_event['Medal'] is np.nan else athlete_event['Medal']
    medal = Medal.objects.get(type=medal_type)
    team = Team.objects.get(name=athlete_event['Team'])
    height = None if athlete_event['Height'] is np.nan else athlete_event['Height']
    weight = None if athlete_event['Weight'] is np.nan else athlete_event['Weight']
    age = None if athlete_event['Age'] is np.nan else athlete_event['Age']
    av = AthleteEvent(
        athlete=athlete,
        event=event,
        game=game,
        medal=medal,
        team=team,
        athlete_height=height,
        athlete_weight=weight,
        athlete_age=age
    )
    av.save()
print('Ok')
