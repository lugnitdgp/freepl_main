from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sqlite3
import time

def get_score():
	# url of scoreboard for a particular match to be provided e.g. given below
	url = "http://www.espncricinfo.com/series/18808/scorecard/1153691/new-zealand-vs-india-1st-odi-india-in-new-zealand-2018-19"
	
	browser_name = "firefox"
	
	firefox_profile = webdriver.FirefoxProfile()
	
	# Disable images
	firefox_profile.set_preference('permissions.default.image', 2)
	
	# disable css if required
	# firefox_profile.set_preference('permissions.default.stylesheet', 2)

	if browser_name == "firefox":
		
		driver = webdriver.Firefox(firefox_profile=firefox_profile)

		driver.get(url)

		# wait till timeout hits
		timeout = 0

		try:
			WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='gp-inning-00']")))
		except TimeoutException:
			print("Timed out waiting for website")
			driver.quit()

		# content_all = driver.find_elements_by_xpath("//div[@id='gp-inning-00']")
		batsmen = driver.find_element_by_xpath("//div[contains(@class, 'batsmen')]")
		bowler = driver.find_element_by_xpath("//div[contains(@class, 'bowling')]")

		batsmen_score = batsmen.text
		bowler_score = bowler.text

		time.sleep(1)

		driver.quit()

		return [batsmen_score, bowler_score]

	# Not working(tested) for chrome
	if browser_name == "chrome":

		driver = webdriver.Chrome()

		driver.get(url)

		names = driver.find_elements_by_tag_name('title')
		address = driver.find_elements_by_tag_name('link')

		match_href = {}

		for name in names:
			print(name.text)

		for name,links in zip(names,address):
			match_href.update({name.text: links.get_attribute('text')})
		print (match_href)

		my_match = [(value) for key, value in match_href.items() if key.startswith("India")]

		time.sleep(5)

		driver.quit()

		return my_match


def store_score(match):

	# location can be changed
	conn = sqlite3.connect('db.sqlite3')
	print("connection successfull")
	curr = conn.cursor()
	
	# creating table for bowling
	tmp = "CREATE TABLE IF NOT EXISTS bowler(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,O INT NOT NULL,M INT NOT NULL,R INT NOT NULL,W INT NOT NULL,ECON REAL NOT NULL,ZEROES INT NOT NULL,FOURS INT NOT NULL,SIXES INT NOT NULL,WD INT NOT NULL, NB INT NOT NULL, SCORE INT NOT NULL);"
	curr.execute(tmp)

	print("table bowling created successfully")

	match[1] = match[1].split('\n')
	k=0
	for i in match[1][1:]:
		sco = 0
		k+=1
		j = i.split()

		# score calculation in bowling
		if j[5] != '0':
			sco = 20 + (int(j[5])-1)*10 + int(j[3])*20
		if int(j[2])*6-int(j[4]) > 0:
			sco += (int(j[2])*6-int(j[4]))*2
		
		# inserting the values in tables with score of respective players
		tmp = "INSERT INTO bowler(ID, NAME, O, M, R, W, ECON, ZEROES, FOURS, SIXES, WD, NB, SCORE) VALUES("+str(k)+", '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {});".format(j[0]+' '+j[1], j[2], j[3], j[4], j[5], j[6], j[7], j[8], j[9], j[10], j[11], sco)
		curr.execute(tmp)
	print("inserted bowling successfully")

	#creating table for batting
	match[0] = match[0].split("Extras")[0]
	match[0] = match[0].split('\n')
	i = 1
	while 7*i+1< len(match[0]):
		del match[0][7*i+1]
		i+=1
	
	tmp = "CREATE TABLE batsmen(ID INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,R INT NOT NULL,B INT NOT NULL,M INT NOT NULL,FOURS INT NOT NULL,SIXES INT NOT NULL,SR INT NOT NULL, SCORE INT NOT NULL);"
	curr.execute(tmp)
	print("created batsmen table")

	k=1
	for i in range(0, len(match[0][7:])-7, 7):
		
		# score calculation for batting
		sco = 0
		if int(match[0][8+i]) - int(match[0][9+i]) > 0:
			sco += int(match[0][8+i]) - int(match[0][9+i])
		if int(match[0][8+i]) != 0:
			sco += int(match[0][8+i]) + 2*int(match[0][12+i]) + 10*(int(match[0][8+i])//25)
		else:
			sco -= 5

		# inserting the values in tables with score of respective players
		tmp = "INSERT INTO batsmen(ID, NAME, R, B, M, FOURS, SIXES, SR, SCORE) VALUES("+str(k)+", '{}', {}, {}, {}, {}, {}, {}, {});".format(match[0][7+i], match[0][8+i], match[0][9+i], match[0][10+i], match[0][11+i], match[0][12+i], match[0][13+i], str(sco))
		k+=1
		curr.execute(tmp)
	
	print("inserted data in batsmen table")
	curr.execute("COMMIT")

	# closing database
	conn.close()

if __name__=="__main__":
	match = get_score()
	store_score(match)
