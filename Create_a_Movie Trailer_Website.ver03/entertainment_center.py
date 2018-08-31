import media
import fresh_tomatoes

annihilation = media.Movie("ANNIHILATION",
                            "A biologist's husband disappears. She puts her name forward for an expedition into an environmental disaster zone, but does not find what she's expecting. The expedition team is made up of the biologist, an anthropologist, a psychologist, a surveyor, and a linguist.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BZWMyM2I5ZmUtNmVlMy00MTY5LTg0M2UtOWJmOTQyY2E3YzVlXkEyXkFqcGdeQXVyMzAwMjMyMjY@._V1_SY1000_SX1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=yBWm4qpTRTQ")



all_the_money_in_the_World = media.Movie("All the Money in the World",
                                         "The story of the kidnapping of 16-year-old John Paul Getty III and the desperate attempt by his devoted mother to convince his billionaire grandfather Jean Paul Getty to pay the ransom.",
                                         "https://images-na.ssl-images-amazon.com/images/M/MV5BNjY3Mjg0OTc1OF5BMl5BanBnXkFtZTgwNDU0MzAyNDM@._V1_.jpg",
                                         "https://www.youtube.com/watch?v=njGneBPdwJI")



thoroughbreds = media.Movie("Thoroughbreds",
                            "Two upper-class teenage girls in suburban Connecticut rekindle. Together, they hatch a plan to solve both of their problems-no matter what the cost.",
                            "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk4MzQ1NDY2OF5BMl5BanBnXkFtZTgwNjA4Nzc4MzI@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=83Eia750V20")


sicario_2_soldado = media.Movie("Sicario 2: Soldado",
                              "The drug war on the US-Mexico border has escalated as the cartels have begun trafficking terrorists across the US border. To fight the war, federal agent Matt Graver re-teams with the mercurial Alejandro.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BZGI5Nzc0OTktOTFhOS00ODVlLThhYjMtMWExOWM5NzJkMmQ3XkEyXkFqcGdeQXVyMTI2NTUxOTE@._V1_SY1000_CR0,0,679,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=4br1A1tltkc")

mortal_engines = media.Movie("Mortal Engines",
                             "Many years after the Sixty Minute War, cities survive a now desolate Earth by moving around on giant wheels attacking and devouring smaller towns to replenish their resources.",
                             "https://images-na.ssl-images-amazon.com/images/M/MV5BMTU4NTEzNzU1NF5BMl5BanBnXkFtZTgwMTg4NTA0NDM@._V1_SY1000_CR0,0,673,1000_AL_.jpg",
                             "https://www.youtube.com/watch?v=tI1BRYqsHoc")

ready_player_one =media.Movie("Ready Player One",
                              "In the near future, Watts escapes from his daily drudgery by logging onto an MMO game called 'The Oasis'. When the game's billionaire founder dies, he offers players his fortune as the prize in an easter egg hunt within the Oasis.",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BODcxNjI4MzY2MF5BMl5BanBnXkFtZTgwMTE0NzUzNDM@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                              "https://www.youtube.com/watch?v=4aifnWlP_sM")


movies=[mortal_engines, ready_player_one, sicario_2_soldado, annihilation, thoroughbreds, all_the_money_in_the_World]
fresh_tomatoes.open_movies_page(movies)
