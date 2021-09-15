import pandas as pd 
movies = [('2009','The Princess and the Frog'),('2009', 'The Blindside'), ('2009', 'Precious'),('2009','The Lovely Bones'),
('2009','Up'),('2009','500 Days of Summer'),('2009','The Hangover'),('2010','The Social Network'),
('2010','Death at a Funeral'),('2010','Grown Ups'),('2010','Despicable Me'),('2010','Toy Story 3'),('2011','The Help'),
('2011', 'Bridesmaids'),('2011','The Hangover 2'),('2012', 'Silver Linnings Playbook'),('2012', 'Wreck it Ralph'),
('2012', 'Perks of Being a Wallflower'),('2012','Brave'),('2012', 'Magic Mike'),('2012', 'Rise of the Guardians'),
('2012', 'Les Miserables'),('2012', 'Ted'),('2012', 'Pitch Perfect'), ('2012', 'Flight'),
('2013', 'The Wolf of Wallstreet'),('2013', 'The Hunger Games: Catching Fire'),('2013', 'Frozen'), 
('2013', 'Monsters University'),('2014', 'Annie'),('2014', 'The Hunger Games: Mockingjay'), 
('2015', 'Inside Out'),('2015', 'Straight Outta Compton'),('2015', 'Amy'),('2015', 'Pitch Perfect 2'),
('2015', 'The Hunger Games: Mokingjay pt 2'),('2016', 'Moonlight'), ('2016', 'Sing'),('2016', 'Zootopia'),
('2016', 'Moana'),('2016', 'Fences'),('2016', 'Finding Dory'),('2017', 'Get Out'),('2017', 'Mudbound'),
('2017', 'Coco'),('2017',' Pitch Perfect 3'), ('2018', 'Wont You Be My Neighbor'),
('2018', 'Spiderman: Into the Spiderverse'),('2018', 'Ralph Breaks the Internet'),('2019', 'Dolemite'),
('2019', 'High Flying Bird'),
('2019', 'Let it Snow')]
df = pd.DataFrame(movies, columns=['Year', 'Film'])
#print(df)
df.to_csv('movies.csv', index= False)
movies_saved_file = pd.read_csv('movies.csv')
print(movies_saved_file)