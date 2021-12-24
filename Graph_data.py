# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:43:07 2021

@author: user
"""

Places_graph = {
                'Abottabad' : ['Mansehra'],
                'Mansehra' : ['Abottabad','Batgram','Balakot'],
                'Balakot' : ['Mansehra','Naran'],
                'Batgram' : ['Mansehra', 'Besham'],
                'Naran' : ['Balakot','Babusar Pass'],
                'Besham' : ['Batgram','Dasu'],
                'Babusar Pass' : ['Naran','Raikot Bridge'],
                'Dasu' : ['Besham','Chilas'],
                'Chilas' : ['Dasu','Raikot Bridge'],
                'Raikot Bridge' : ['Chilas','Babusar Pass','Astore','Alam Bridge','Hunza', 'Gilgit'],
                'Gilgit' : ['Raikot Bridge','Ghizar','Nomal'],
                'Nomal' : ['Gilgit','Naltar'],
                'Naltar' : ['Nomal'],
                'Ghizar' : ['Gilgit','Khalti Lake','Yasin'],
                'Khalti Lake' : ['Ghizar'],
                'Yasin' : ['Ghizar','Shandur'],
                'Shandur' : ['Yasin','Chitral'],
                'Chitral' : ['Shandur'],
                'Hunza' : ['Raikot Bridge','Attabad Lake'],
                'Attabad Lake' : ['Hunza','Passu'],
                'Passu' : ['Attabad Lake','Khunjrab Pass'],
                'Khunjrab Pass' : ['Passu'],                
                'Alam Bridge' : ['Raikot Bridge','Skardu'],
                'Skardu' : ['Alam Bridge','Shangrilla','Shigar','Deosai'],
                'Shangrilla' : ['Upper Kachur','Skardu'],
                'Upper Kachur' : ['Shangrilla'],
                'Shigar' : ['Skardu'],
                'Deosai' : ['Skardu','Chilam'],
                'Chilam' : ['Astore','Deosai','Burzill Pass'],
                'Burzill Pass' : ['Chilam','Minimerg'],
                'Minimerg' : ['Domel','Kamri'],
                'Kamri' : ['Minimerg'],
                'Domel' : ['Minimerg'],
                'Astore' : ['Chilam','Rama Lake','Raikot Bridge'],
                'Rama Lake' : ['Astore']
              }
                 

Distance_graph = {
                    ('Abottabad','Mansehra') : 3.33,
                    ('Mansehra','Balakot') : 10.00,
                    ('Mansehra','Batgram') : 15.25,
                    ('Batgram','Besham') : 5.00,
                    ('Besham','Dassu') : 15.00,
                    ('Dasu','Chilas') : 15.00,
                    ('Chilas','Raikot Bridge') : 15.50,
                    ('Balakot','Naran') : 10.00,
                    ('Naran','Babusar Pass') : 15.00,
                    ('Babusar Pass','Raikot Bridge') : 20.00,
                    ('Chilas','Raikot Bridge'): 15.00,
                    ('Raikot Bridge','Astore') : 15.75,
                    ('Raikot Bridge','Gilgit') : 7.50,
                    ('Raikot Bridge','Alam Bridge') : 10.00,
                    ('Raikot Bridge','Hunza') : 15.00,
                    ('Gilgat','Ghizar') : 10.00,
                    ('Ghizar','Yasin') : 20.00,
                    ('Yasin','Shandur') : 16.00,
                    ('Shandur','Chitral'): 15.00,
                    ('Ghizar','Khalti Lake') : 9.50,
                    ('Gilgit','Nomal') : 3.33,
                    ('Nomal','Naltar') : 3.33,
                    ('Hunza','Attabad Lake') : 2.00,
                    ('Attabad Lake','Passu') : 10.00,
                    ('Passu','Khunjrab Pass') : 7.50,
                    ('Alam Bridge','Skardu') : 9.50,
                    ('Skardu','Shigar') : 5.00,
                    ('Skardu','Shangrilla') : 2.50,
                    ('Skardu','Deosai') : 15.00,
                    ('Shangrilla','Upper Kachur') : 2.00,
                    ('Deosai','Chilam') : 15.00,
                    ('Chilam','Astore') : 17.00,
                    ('Chilam','Burzill Pass') : 5.50,
                    ('Burzill Pass','Minimerg') : 6.00,
                    ('Minimerg','Domel') : 2.50,
                    ('Minimerg','Kamri') : 2.50,
                    ('Astore','Rama Lake') : 3.75,
               }

Cost_graph = {
                    ('Abottabad','Mansehra') : 100,
                    ('Mansehra','Balakot') : 250,
                    ('Mansehra','Batgram') : 400,
                    ('Batgram','Besham') : 5.00,
                    ('Besham','Dassu') : 380,
                    ('Dasu','Chilas') : 380,
                    ('Chilas','Raikot Bridge') : 440,
                    ('Balakot','Naran') : 250,
                    ('Naran','Babusar Pass') : 380,
                    ('Babusar Pass','Raikot Bridge') : 520,
                    ('Chilas','Raikot Bridge'): 385,
                    ('Raikot Bridge','Astore') : 445,
                    ('Raikot Bridge','Gilgit') : 175,
                    ('Raikot Bridge','Alam Bridge') : 200,
                    ('Raikot Bridge','Hunza') : 380,
                    ('Gilgat','Ghizar') : 210,
                    ('Ghizar','Yasin') : 520,
                    ('Yasin','Shandur') : 410,
                    ('Shandur','Chitral'): 400,
                    ('Ghizar','Khalti Lake') : 190,
                    ('Gilgit','Nomal') : 110,
                    ('Nomal','Naltar') :120,
                    ('Hunza','Attabad Lake') : 70,
                    ('Attabad Lake','Passu') : 200,
                    ('Passu','Khunjrab Pass') : 150,
                    ('Alam Bridge','Skardu') : 190,
                    ('Skardu','Shigar') :90,
                    ('Skardu','Shangrilla') : 60,
                    ('Skardu','Deosai') : 400,
                    ('Shangrilla','Upper Kachur') : 65,
                    ('Deosai','Chilam') : 400,
                    ('Chilam','Astore') : 450,
                    ('Chilam','Burzill Pass') : 80,
                    ('Burzill Pass','Minimerg') : 105,
                    ('Minimerg','Domel') : 65,
                    ('Minimerg','Kamri') : 65,
                    ('Astore','Rama Lake') : 85,
                
                    }

print(Places_graph)
print(Distance_graph)
print(Cost_graph)