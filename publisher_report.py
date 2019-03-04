
# coding: utf-8

# In[1]:


import mysql.connector
from selenium import webdriver
import json, base64
import time
#import urllib
from PIL import Image
import os

def chrome_takeFullScreenshot(driver) :

  def send(cmd, params):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({'cmd':cmd, 'params': params})
    response = driver.command_executor._request('POST', url, body)
    return response.get('value')

  def evaluate(script):
    response = send('Runtime.evaluate', {'returnByValue': True, 'expression': script})
    return response['result']['value']

  metrics = evaluate(     "({" +       "width: Math.max(window.innerWidth, document.body.scrollWidth, document.documentElement.scrollWidth)|0," +       "height: Math.max(innerHeight, document.body.scrollHeight, document.documentElement.scrollHeight)|0," +       "deviceScaleFactor: window.devicePixelRatio || 1," +       "mobile: typeof window.orientation !== 'undefined'" +     "})")
  send('Emulation.setDeviceMetricsOverride', metrics)
  screenshot = send('Page.captureScreenshot', {'format': 'png', 'fromSurface': True})
  send('Emulation.clearDeviceMetricsOverride', {})

  return base64.b64decode(screenshot['data'])


capabilities = {
  'browserName': 'chrome',
  'chromeOptions':  {
    'useAutomationExtension': False,
    'args': ['--disable-infobars']
  }
}
#connect to mysql
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123speakol",
  database="testing"  
)
mycursor = mydb.cursor()
mycursor.execute("select distinct domain_id from testing.widgets where id in (select widget_id from testing.reports where widget_id=widget_id) order by domain_id asc LIMIT 0,1;")
myresult = mycursor.fetchall()
count=0
for x in myresult: 
  driver = webdriver.Chrome(desired_capabilities=capabilities)
  driver.maximize_window()
  driver.get("https://redash.speakol.com/dashboard/publisher-report-board?p_domain_id="+str(x[0])+"&p_start=2019-01-01&p_end=2019-01-31#1244")
  #wait to pass log in values
  time.sleep(5)
  user = driver.find_element_by_name("email")
  password = driver.find_element_by_name("password")
  user.clear()
  user.send_keys("mostafa.abdelsalam@speakol.com")
  password.clear()
  password.send_keys("1234mostafaml")
  login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
  login_attempt.submit()
 #wait until page load to take FullScreenshot
  time.sleep(20)
  driver.set_page_load_timeout(25)
  png = chrome_takeFullScreenshot(driver)
  filename = str(x[0])+'.png'
  foldername = str(x[0])
  with open(r"/home/amira/Desktop/publisher report_full screen/"+filename, 'wb') as f:
   f.write(png)
   
  os.chdir('/home/amira/Desktop/publisher report')
  file_exist=os.path.exists('./'+foldername)
  if file_exist == True:
    print("file exist") 
  if file_exist == False:  
   myfolder=os.mkdir('/home/amira/Desktop/publisher report/'+foldername)
   full_path=os.path.realpath(foldername)

   first_part =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename) 
   #to crop domainInfo
   box=(5, 200, 1300,700)
   cropped_image1 = first_part.crop(box)
   cropped_image1.save(full_path + "/" +"domainInfo_"+filename)
   im1 = Image.open(full_path + "/" +"domainInfo_"+filename)
   im2 = im1.resize((1295, 400))         
   im2.save(full_path + "/" +"domainInfo_"+filename)
   
    
   first_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename) 
   #to crop widget views vs days graph
   box=(5, 700, 1300,1100)
   cropped_image2 = first_graph.crop(box)
   cropped_image2.save(full_path + "/" +"CTR vs days_"+filename)
   
   middle_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename)
   #to crop widget views vs days graph
   box=(5, 1100, 1300,1500)
   cropped_image3 = middle_graph.crop(box)
   cropped_image3.save(full_path + "/" +"widget views vs days_"+filename)
   
  
   imp_click_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename)
   #to crop viewAbility vs days graph
   box=(5, 1500, 1300,1900)
   cropped_image4 = imp_click_graph.crop(box)
   cropped_image4.save(full_path + "/" +"viewAbility vs days_"+filename)
    

   clicks_earnings_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename)
   #to crop clicks & earnings graph
   box=(5, 1900, 1300,2300)
   cropped_image4 = clicks_earnings_graph.crop(box)
   cropped_image4.save(full_path + "/" +"clicks & earnings_"+filename)
   

   widge_pageviews_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename)
   #to crop page views&widge views chart
   box=(5, 2300, 1300,2700)
   cropped_image4 = widge_pageviews_graph.crop(box)
   cropped_image4.save(full_path + "/" +"page views&widge views_"+filename)
   
   viewAbility_graph =Image.open("/home/amira/Desktop/publisher report_full screen/"+filename)
   #to crop viewAbility chart
   box=(5, 2700, 1300,3100)
   cropped_image4 = viewAbility_graph.crop(box)
   cropped_image4.save(full_path + "/" +"viewAbility_"+filename)
   
   
   
  driver.close()
  count+=1
#to avoid Too Many Requests
  if count==25 or count==50 or count==75 or count==100 or count==125 or count==150 or count==175 or count==200 or count==225 or count==250 or count==275 or count==300 or count==325 or count==350 or count==375 or count==400 or count==425 or count==450 or count==475 or count==500 or count==525 or count==550 or count==575 or count==600 or count==625 or count==650 or count==675 or count==700 or count==725 or count==750 or count==775 or count==800 or count==825 or count==850 or count==875 or count==900 or count==925 or count==950 or count==975 or count==1000 or count==1025 or count==1050 or count==1075 or count==1100 or count==1125 or count==1150 or count==1175:
   time.sleep(3600)
   continue

