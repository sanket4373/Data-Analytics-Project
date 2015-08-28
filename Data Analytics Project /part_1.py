"""
PART-I RELATIONAL THEORY

FROM THE MAIN TABLE 4 ADDTIONAL TABLES HAVE BEEN CREATED USING 5TH DEGREE NORMALIZATION. 
THE TABLE ARE AS FOLLOWS:
 1. site_table Table
 2. date_time Table
 3. sensor_site Table
 4. panel_site Table
 


"""


import sqlite3
import csv

conn = sqlite3.connect('database_part22.db')
print " Opened Database Successfully!!! "

c = conn.cursor()



# (site) Table1
c.execute('''CREATE TABLE site (SiteID int, SiteName text, SiteAddress text, SiteCity text)''')

input1 = [(1,'NW-Vista','100AeroSt','Boerne'),
	  	  (2,'GreatPlains','5StateHwy1','Paris'),
	  	  (3,'BatCave','1856ScenicLoop','Bulverde'),
	  	  (4,'RiverBend','20987SmithRd.','FallsCity')
	  	  ]


c.executemany('INSERT INTO site VALUES (?,?,?,?)',input1)


#Table 2 date_time Table
c.execute('''CREATE TABLE date_time (DateTime int, Date int, Time int)''')

input2 = [(1,'2000-01-01','00:00'),
	      (2,'2000-01-01','08:00'),
	      (3,'2000-01-01','12:00'),
	      (4,'2000-01-01','20:00'),
	      (5,'2000-02-01','00:00'),
	      (6,'2000-02-01','08:00'),
	      (7,'2000-02-01','12:00'),
	      (8,'2000-02-01','20:00'),
	      (9,'2000-03-01','00:00'),
	      (10,'2000-03-01','08:00'),
	      (11,'2000-03-01','12:00'),
	      (12,'2000-03-01','20:00')
	      ]

c.executemany('INSERT INTO date_time VALUES (?,?,?)',input2 )


#Table 3 - panel_data_site1 
c.execute('''CREATE TABLE panel_data_site1 (datetime int, SiteID int, PanelNum int, PanelWatts int )''')

site1 = open('panel_data_site1.csv','rb')

r1 = csv.reader(site1)
i = 0
for line in r1:
	if (i%2 == 0):
		c.execute("INSERT INTO panel_data_site1 VALUES (?,?,?,?)",line )
	i += 1



#Table 4 - panel_data_site2 
c.execute('''CREATE TABLE panel_data_site2 (datetime int, SiteID int, PanelNum int, PanelWatts int)''')

site2 = open('panel_data_site2.csv','rb')

r2 = csv.reader(site2)
i = 0
for line in r2:
	if (i%2 == 0):
		c.execute("INSERT INTO panel_data_site2 VALUES (?,?,?,?)",line )
	i += 1


#Table 5 - panel_data_site3 
c.execute('''CREATE TABLE panel_data_site3 (datetime int, SiteID int, PanelNum int, PanelWatts int)''')

site3 = open('panel_data_site3.csv','rb')

r3 = csv.reader(site3)
i = 0
for line in r3:
	if (i%2 == 0):
		c.execute("INSERT INTO panel_data_site3 VALUES (?,?,?,?)",line )
	i += 1


#Table 6 - panel_data_site4	

c.execute('''CREATE TABLE panel_data_site4 (datetime int, SiteID int, PanelNum int, PanelWatts int)''')

site4 = open('panel_data_site4.csv','rb')

r4 = csv.reader(site4)
i = 0
for line in r4:
	if (i%2 == 0):
		c.execute("INSERT INTO panel_data_site4 VALUES (?,?,?,?)",line )
	i += 1





#Table 7 - sensor_data_site1 
c.execute('''CREATE TABLE sensor_data_site1 (datetime int, SiteID int, SensorNum int, SensorTemp int, SensorIrradiance int)''')

site11 = open('sensor_data_site1.csv','rb')

r11 = csv.reader(site11)

for line in r11:
	c.execute("INSERT INTO sensor_data_site1 VALUES (?,?,?,?,?)",line )


#Table 7 - sensor_data_site2 
c.execute('''CREATE TABLE sensor_data_site2 (datetime int, SiteID int, SensorNum int, SensorTemp int, SensorIrradiance int)''')

site22 = open('sensor_data_site2.csv','rb')

r22 = csv.reader(site22)

for line in r22:
	c.execute("INSERT INTO sensor_data_site2 VALUES (?,?,?,?,?)",line )

#Table 7 - sensor_data_site3 
c.execute('''CREATE TABLE sensor_data_site3 (datetime int, SiteID int, SensorNum int, SensorTemp int, SensorIrradiance int)''')

site33 = open('sensor_data_site3.csv','rb')

r33 = csv.reader(site33)

for line in r33:
	c.execute("INSERT INTO sensor_data_site3 VALUES (?,?,?,?,?)",line )

#Table 7 - sensor_data_site1 
c.execute('''CREATE TABLE sensor_data_site4 (datetime int, SiteID int, SensorNum int, SensorTemp int, SensorIrradiance int)''')

site44 = open('sensor_data_site4.csv','rb')

r44 = csv.reader(site44)

for line in r44:
	c.execute("INSERT INTO sensor_data_site4 VALUES (?,?,?,?,?)",line )




conn.commit()
conn.close()
