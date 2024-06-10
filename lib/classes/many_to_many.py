class Band:
    all=[]

    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        Band.all.append(self)

    def get_name(self):
        return self._name  

    def set_name(self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name=name
    name=property(get_name,set_name)

    def get_hometown(self):
        return self._hometown
    
    def set_hometown(self,hometown):
        if not isinstance(hometown,str):
            return None
        if not len(hometown) > 0:
            return None
        if hasattr(self,'_hometown'):
            return None
        self._hometown=hometown
    hometown=property(get_hometown,set_hometown)

    def concerts(self):
        return [concert for concert in Concert.all if concert.band==self]

    def venues(self):
        return list(set(concert.venue for concert in self.concerts()))

    def play_in_venue(self, venue, date):
        if isinstance(venue,Venue):
            return Concert(date,self,venue)

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts()]


class Concert:
    all=[]

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)
    
    def get_date(self):
        return self._date
    
    def set_date(self,date):
        if isinstance(date,str) and len(date)> 0:
            self._date=date
    date=property(get_date,set_date)

    def get_band(self):
        return self._band
    
    def set_band(self,band):
        if isinstance(band,Band):
            self._band=band
    band=property(get_band,set_band)

    def get_venue(self):
        return self._venue
    
    def set_venue(self,venue):
        if isinstance(venue,Venue):
            self._venue=venue
    venue=property(get_venue,set_venue)

    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    all=[]

    def __init__(self, name, city):
        self.name = name
        self.city = city
        Venue.all.append(self)
    
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if isinstance(name,str) and len(name) > 0:
            self._name=name
    name=property(get_name,set_name)

    def get_city(self):
        return self._city
    
    def set_city(self,city):
        if isinstance(city,str) and len(city) > 0:
            self._city=city
    city=property(get_city,set_city)

    def concerts(self):
        return[concert for concert in Concert.all if concert.venue==self]
    
    def bands(self):
        return list(set(concert.band for concert in self.concerts()))
