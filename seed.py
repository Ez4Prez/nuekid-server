#!/usr/bin/env python3

from app import app, bcrypt
from models import db, Location, Event, User, Date

with app.app_context():
    
    Location.query.delete()
    Event.query.delete()
    User.query.delete()
    Date.query.delete()

    
    locations = []
    
    locations.append(Location(
        name='Sid Luckman Field',
        address='1463-1469 McDonald Ave, Brooklyn, NY 11230',
        lat="40.617482",
        long="-73.973687",
        img="https://ir.4sqi.net/img/general/original/29363372_dMEVVoPJn6g4uVpk2nGiwvfoJiFGIF9yM92zoSTPw8w.jpg",
        location_type="Football"
    ))
    locations.append(Location(
        name='Brooklyn Bridge Park Pier 5',
        address='334 Furmant St, Brooklyn, NY 11201',
        lat="40.694438",
        long="-74.001049",
        img="https://brooklynbridgeparents.com/wp-content/uploads/2021/01/unnamed.jpg",
        location_type="Football"
    ))
    locations.append(Location(
        name='Globall Sports Center',
        address='1561 Bedford Ave, Brooklyn, NY 11225',
        lat="40.668893",
        long="-73.955491",
        img="https://globallconcepts.com/wp-content/uploads/2022/01/nasssindoor-768x576.jpg",
        location_type="Football"
    ))
    locations.append(Location(
        name='Verrazano Sports Complex',
        address='1990 Shore Pkwy, Brooklyn, NY 11214',
        lat="40.587382",
        long="-73.992417",
        img="https://cdn.businessyab.com/assets/uploads/4a168e15fd679ec892b0250bbee48de2_-united-states-new-york-kings-county-brooklyn-gravesend-shore-parkway-1990-verrazano-sports-complex.jpg",
        location_type="Soccer"
    ))
    locations.append(Location(
        name='Buddy Keaton Fields',
        address='Bergen St. &, Schenectady Ave, Brooklyn, NY 11213',
        lat="40.674682",
        long="-73.934162",
        img="https://images.squarespace-cdn.com/content/v1/5af1f41c96e76f0fffa9a9be/56e8ba59-5f67-45e2-9e95-de20afc3d208/SJP4.jpeg",
        location_type="Soccer"
    ))
    locations.append(Location(
        name='Prospect Park',
        address='Prospect Heights, Brooklyn, NY 11215',
        lat="40.661041",
        long="-73.968445",
        img="https://theagencyre.com/blog/wp-content/uploads/2021/09/shutterstock_1558169030.jpg",
        location_type="Bicycle"
    ))
    locations.append(Location(
        name='Canarsie Park',
        address='Seaview Ave & Remsen Ave, Brooklyn, NY 11236',
        lat="40.633756678705694",
        long="-73.8938727197795",
        img="https://www.nycgovparks.org/photo_gallery/full_size/23751.jpg",
        location_type="Bicycle"
    ))
    locations.append(Location(
        name='Brooklyn Bridge Park',
        address='334 Furman St, Brooklyn, NY 11201',
        lat="40.70287661973249",
        long="-73.99579221481221",
        img="https://theagencyre.com/blog/wp-content/uploads/2021/09/Brookklyn-bridge-park.jpg",
        location_type="Bicycle"
    ))
    locations.append(Location(
        name='Adams Street Library',
        address='9 Adams St, Brooklyn, NY 11201',
        lat="40.704341417064455",
        long="-73.98826757260288",
        img="https://www.vmcdn.ca/f/files/bkreader/import/2021_10_Adams-Street-Take-2-interior-Childrens-area-1-scaled.jpg",
        location_type="Books"
    ))
    locations.append(Location(
        name='Park Slope Library',
        address='431 6th Ave, Brooklyn, NY 11215',
        lat="40.66938322477015",
        long="-73.98377452336914",
        img="https://www.bklynlibrary.org/sites/default/files/styles/eventcal_large_split/public/images/page/RESIZE_pic_0018_2.jpg",
        location_type="Books"
    ))
    locations.append(Location(
        name='Washington Park',
        address='4th St. &, 5th Ave, Brooklyn, NY 11215',
        lat="40.67620873496912",
        long="-73.9854892706327",
        img="https://images.fineartamerica.com/images/artworkimages/mediumlarge/1/1-outdoor-chess-boards-washington-square-park-new-york-city-usa-joe-fox.jpg",
        location_type="Chess"
    ))
    locations.append(Location(
        name='Brooklyn Museum',
        address='200 Eastern Pkwy, Brooklyn, NY 11238',
        lat="40.672761568523526",
        long="-73.96345828598297",
        img="https://upload.wikimedia.org/wikipedia/commons/3/3a/Brooklyn_Museum_-_Entrance_%2852302265063%29.jpg",
        location_type="Chess"
    ))
    locations.append(Location(
        name='The Brooklyn Strategist',
        address='333 Court St, Brooklyn, NY 11231',
        lat="40.68567889748258",
        long="-73.99540488252826",
        img="https://s3-media0.fl.yelpcdn.com/bphoto/lpaqWfMxpLeQV_AIsHG9lw/348s.jpg",
        location_type="Chess"
    ))

    locations.append(Location(
        name='Next Level',
        address='874 4th Ave, Brooklyn, NY 11232',
        lat="40.66007618299216",
        long="-74.00103169302449",
        img="https://s3-media0.fl.yelpcdn.com/bphoto/lkWRI6nB0VU8ViAyYPDWQw/348s.jpg",
        location_type="Game"
    ))
    locations.append(Location(
        name='Alamo Drafthouse',
        address='445 Albee Square W 4th floor, Brooklyn, NY 11201',
        lat="40.69398791247702",
        long="-73.98314911526691",
        img="https://www.indiewire.com/wp-content/uploads/2016/10/img_6141.jpg",
        location_type="Game"
    ))
    locations.append(Location(
        name='Geek Forest',
        address='122 Bedford Ave, Brooklyn, NY 11249',
        lat="40.712203",
        long="-73.955887",
        img="https://c8.alamy.com/comp/RBMG5F/geek-forest-358-grand-street-brooklyn-ny-exterior-of-a-science-and-art-focused-afterschool-program-in-the-williamsburg-neighborhood-RBMG5F.jpg",
        location_type="Game"
    ))
    locations.append(Location(
        name='Home',
        address='1444 Flatbush Ave, Brooklyn, NY 11210',
        lat="40.63558295842797",
        long="-73.95077298074986",
        img="images/home1.png",
        location_type="Home1"
    ))
    locations.append(Location(
        name="Jomo's Spot",
        address='1446 Flatbush Ave, Brooklyn, NY 11210',
        lat="40.642543873740884",
        long="-73.95184584323957",
        img="images/home2.png",
        location_type="Home2"
    ))
    locations.append(Location(
        name="SoFive Brooklyn",
        address='2015 Pitkin Ave, Brooklyn, NY 11207',
        lat="40.672148",
        long="-73.898350",
        img="https://media.bizj.us/view/img/11066486/sofive-rockville*1200xx2016-1134-0-189.jpg",
        location_type="Soccer"
    ))
    locations.append(Location(
        name="Alicia's Spot",
        address='930 Prospect Pl, Brooklyn, NY 11213',
        lat="40.67402775008218",
        long="-73.94582341731473",
        img="images/home2.png",
        location_type="Home2"
    ))
    locations.append(Location(
        name="Sunset Park",
        address='7th Avenue &, 43rd St, Brooklyn, NY 11232',
        lat="40.65287131606477",
        long="-74.00382042189905",
        img="https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/56/a4/fe/the-city-at-sunset-park.jpg?w=1200&h=-1&s=1",
        location_type="Basketball"
    ))
    locations.append(Location(
        name="Dome Playground",
        address='38th Street & 37th Street, Brooklyn, NY 11218',
        lat="40.641749494983046",
        long="-73.9800611660314",
        img="https://www.nycgovparks.org/photo_gallery/full_size/18800.jpg",
        location_type="Basketball"
    ))
   
    





    



    events = []

    events.append(Event(
        title="6 Vs 6 Flag Football",
        description="Football this Saturday!",
        event_type="Flag Football",
        people_needed= 16,
        space_available= 10,
        location_id=2,
        date_id=1
    ))
    events.append(Event(
        title="Group Bike Ride",
        description="Join us bright and early for a group bike at prospect park.",
        event_type="Bicycle",
        people_needed= 10,
        space_available= 3,
        location_id=6,
        date_id=3
    ))
    events.append(Event(
        title="Harry Potter Book Club",
        description="Join Brooklyn's premier Harry Potter book and fan club.",
        event_type="Books",
        people_needed= 25,
        space_available= 4,
        location_id=9,
        date_id=9
    ))
    events.append(Event(
        title="Pick-up Soccer Game",
        description="Family friendly softball game at Buddy Keaton. All are welcome!",
        event_type="Softball",
        people_needed= 18,
        space_available= 7,
        location_id=5,
        date_id=12
    ))
    events.append(Event(
        title="Competitive Touch Football",
        description="Got what it takes? bring your A game",
        event_type="Football",
        people_needed= 12,
        space_available= 3,
        location_id=3,
        date_id=2
    ))
    events.append(Event(
        title="8 Man Bike Race!",
        description="3 Lap race around prospect park skilled riders only.",
        event_type="Bicycle",
        people_needed= 8,
        space_available= 3,
        location_id=6,
        date_id=8
    ))
    events.append(Event(
        title="Speed Chess Tournament",
        description="Speed chess tournament for skilled players only.",
        event_type="Chess",
        people_needed= 10,
        space_available= 2,
        location_id=11,
        date_id=2
    ))
    events.append(Event(
        title="Kids Bike Lessons (ages 4-8)",
        description="Parents must be present. Get the kiddo's comfortable riding bikes!",
        event_type="Bicycle",
        people_needed= 12,
        space_available= 6,
        location_id=6,
        date_id=10
    ))
    events.append(Event(
        title="Archie Comics Fan Club",
        description="Join our monthly fan club of an all-time classic!",
        event_type="Books",
        people_needed= 20,
        space_available= 9,
        location_id=9,
        date_id=5
    ))
    events.append(Event(
        title="Evening Group Ride",
        description="Easy going cycle session at prospect park",
        event_type="Bicycle",
        people_needed= 10,
        space_available= 7,
        location_id=6,
        date_id=3
    ))
    events.append(Event(
        title="A Separate Reality by Carlos Castaneda",
        description="Kick of the beginning of our humble following of this cult classic about the shaman Dan Juan",
        event_type="Books",
        people_needed= 18,
        space_available= 10,
        location_id=9,
        date_id=9
    ))
    events.append(Event(
        title="Chess Hour",
        description="Friendly competition chess games for all skill levels",
        event_type="Chess",
        people_needed= 15,
        space_available= 6,
        location_id=11,
        date_id=5
    ))
    events.append(Event(
        title="PeeWee Football League",
        description="Parents must be present. Brooklyn's safest youth football program.",
        event_type="Football",
        people_needed= 22,
        space_available= 5,
        location_id=2,
        date_id=7
    ))
    events.append(Event(
        title="2 vs 2 Basketball Tournament!",
        description="Which duo will bring home the prize? All day event!",
        event_type="Basketball",
        people_needed= 16,
        space_available= 5,
        location_id=21,
        date_id=5
    ))
    events.append(Event(
        title="12 Player Chess Tournament",
        description="12 player chess tournaments for anybody who wants to put their skills to the test!",
        event_type="Chess",
        people_needed= 12,
        space_available= 8,
        location_id=11,
        date_id=12
    ))
    events.append(Event(
        title="7 v 7 Friendly Football!",
        description="Low competition and minimum contact football for fun",
        event_type="Football",
        people_needed= 14,
        space_available= 10,
        location_id=2,
        date_id=9
    ))
    events.append(Event(
        title="Youth Soccer",
        description="Kids Soccer league, ages 8-12. Parents must be present.",
        event_type="Soccer",
        people_needed= 25,
        space_available= 8,
        location_id=19,
        date_id=4
    ))
    events.append(Event(
        title="Sharks League: 8-vs-8 Full Contact Football",
        description="Game 2 of the season, open positions still available!",
        event_type="Football",
        people_needed= 48,
        space_available= 12,
        location_id=2,
        date_id=10
    ))
    events.append(Event(
        title="Pick-up Basketball Game",
        description="Local pickup after work",
        event_type="Basketball",
        people_needed= 8,
        space_available= 3,
        location_id=21,
        date_id=12
    ))
    events.append(Event(
        title="Pickup Soccer 5 vs 5",
        description="10 man evening pickup soccer game",
        event_type="Soccer",
        people_needed= 10,
        space_available= 2,
        location_id=19,
        date_id=8
    ))




    users = []

    password = 'dogs123'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    users.append(User(
        username="Doug_Dribbles",
        password_hash=hashed_password,
        first_name="Doug",
        last_name="Barnes",
        address="1573 Bedford Ave, Brooklyn, NY 11225",
        age= 32
    ))

    password = 'cats123'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    users.append(User(
        username="ez4prez",
        password_hash=hashed_password,
        first_name="Ezra",
        last_name="Mays-Richards",
        address="1444 Flatbush Ave, Brooklyn, NY 11210",
        age= 29
    ))

    password = 'cats123'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    users.append(User(
        username="TownGirl510",
        password_hash=hashed_password,
        first_name="Alicia",
        last_name="Morales",
        address="930 Prospect Pl, Brooklyn, NY 11213",
        age= 34
    ))

    password = 'cats123'
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    users.append(User(
        username="JimBrown",
        password_hash=hashed_password,
        first_name="Jomo",
        last_name="L",
        address="930 Prospect Pl, Brooklyn, NY 11213",
        age= 41
    ))
    users.append(User(
        username="DaBroes",
        password_hash="cats123",
        first_name="Joe",
        last_name="Dabo",
        address="229 Troy Ave, Brooklyn, NY 11213",
        age= 35
    ))
    users.append(User(
        username="HaloLover03",
        password_hash="cats123",
        first_name="Will",
        last_name="Spears",
        address="224 Kent Ave, Brooklyn, NY 11214",
        age= 43
    ))
    users.append(User(
        username="Dave1998",
        password_hash="cats123",
        first_name="David",
        last_name="Chen",
        address="33 Cat Walk Ave, Brooklyn, NY 11219",
        age= 25
    ))
    users.append(User(
        username="Aaronz",
        password_hash="cats123",
        first_name="Aaron",
        last_name="Z",
        address="14 Ocean Ave, Brooklyn, NY 11209",
        age= 27
    ))
    users.append(User(
        username="MsLarose",
        password_hash="cats123",
        first_name="Shannun",
        last_name="L",
        address="303 Church Ave, Brooklyn, NY 11211",
        age= 26
    ))
    users.append(User(
        username="Pac-manz",
        password_hash="cats123",
        first_name="Rando",
        last_name="Dave",
        address="315 Keller St, Brooklyn, NY 11208",
        age= 31
    ))
    users.append(User(
        username="Last_Guy",
        password_hash="cats123",
        first_name="Steve",
        last_name="Last",
        address="44 Sunshine St, Brooklyn, NY 11210",
        age= 44
    ))
    users.append(User(
        username="sykee112",
        password_hash="cats123",
        first_name="Wanda",
        last_name="Sykes",
        address="18 Dekaulb Ave, Brooklyn, NY 11216",
        age= 42
    ))


    dates = []

    dates.append(Date(
        time="3:30 PM",
        day="2023,7,23"
    ))
    dates.append(Date(
        time="7:00 AM",
        day="2023,7,23"
    ))
    dates.append(Date(
        time="7:00 PM",
        day="2023,7,23"
    ))
    dates.append(Date(
        time="6:00 AM",
        day="2023,7,25"
    ))
    dates.append(Date(
        time="2:00 PM",
        day="2023,7,25"
    ))
    dates.append(Date(
        time="8:00 PM",
        day="2023,7,25"
    ))
    dates.append(Date(
        time="8:00 AM",
        day="2023,7,27"
    ))
    dates.append(Date(
        time="8:00 PM",
        day="2023,7,27"
    ))
    dates.append(Date(
        time="3:30 PM",
        day="2023,7,27"
    ))
    dates.append(Date(
        time="9:00 AM",
        day="2023,7,29"
    ))
    dates.append(Date(
        time="7:15 AM",
        day="2023,7,29"
    ))
    dates.append(Date(
        time="6:00 PM",
        day="2023,7,29"
    ))







    

    

    db.session.add_all(locations)
    db.session.add_all(events)
    db.session.add_all(users)
    db.session.add_all(dates)

    db.session.commit()
    print("🌱 Successfully seeded! 🌱")