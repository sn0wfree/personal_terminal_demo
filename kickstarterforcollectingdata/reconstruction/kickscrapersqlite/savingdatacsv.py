

import sys
import funcforkick
import time
import pandas as pd
import numpy as np

start = time.time()

global counts
counts = 0
def read_url_file(file):
    with open (file,'r') as file_unclear_file:
        file_unclear = []
        file_unclear_list =file_unclear_file.readlines()
        for x in file_unclear_list:
            #print x
            x = x.split()
            #print x
            file_unclear+=x
        return file_unclear


global index
global total_item
global total_rewards

target_url_file='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/test.txt'
have_collected_url='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/collected.txt'
saving_file ='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/project_data.csv'
rewards_backers_distribution='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/rewards_backers_distribution.csv'
rewards_pledge_limit='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/rewards_pledge_limit.csv'
rewards_pledged_amount='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/rewards_pledged_amount.csv'
item_collect='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/item.txt'
rewards_collect='/Users/sn0wfree/BitTorrent Sync/kickstarterscrapy/kickstarterrunopt/reconstruction/data/test/rewards.txt'




print 'begin to create/read index file'
#read projetc urls


url_list = read_url_file(target_url_file)
collected=read_url_file(have_collected_url)
#index = funcforkick.index_read('data/middle60project/index_value20.txt','data/middle60project/index_keys20.txt')

print len(collected)
#print collected[1]w
w='a'
print w#print url_list[1]
file=list(set(url_list)-set(collected))
print file[1]
rewards_headers=['Project_ID','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89']
item_headers = ['Project_ID','project_name','Goal','url',
          'pledged_amount','backers_count','creator_full_name',
          'creator_personal_url','creator_buildhistory_has_backed_projects_number','creator_built_projects_number',
          'creator_bio_info_url','creator_Facebook_url','currency','duration','location_ID','state_changed_at','created_at','Deadline','description','category','project_state','has_a_video','comments_count','updates_number','data_percent_rasied','hours_left','creator_short_name','creator_friends_facebook_number']
total_item=[]
total_rewards_backers_distribution=[]
total_rewards_pledge_limit=[]
total_rewards_pledged_amount=[]
new_add=0
updated=0
repeated=0
#print 'reading urls file completed'
print 'begin to collecting data'

def operat(someurl,count,total_item,total_rewards_pledge_limit,total_rewards_pledged_amount,total_rewards_backers_distribution):
    start = time.time()
    print someurl
    a=[]
    a.append(someurl)

    #someurl=''.join(someurl)
    if someurl !='':
        global new_add
        global updated
        global repeated
        (state,sel,the_page1) = funcforkick.shortcompareindexprocess(a)
        (item,rewards,ID,state)= funcforkick.datagenerateprocess(someurl,state,sel,the_page1)
        (total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)=funcforkick.savingcsvforalltaskprocess(rewards,item,total_item,total_rewards_backers_distribution,total_rewards_pledge_limit,total_rewards_pledged_amount)
        counts = counts + 1
        collected.append(someurl)
        if len(total_item)>10:
            #print total_rewards_backers_distribution
            #print total_rewards_pledge_limit,total_rewards_pledged_amount
            #print
            funcforkick.projetcdata_txt_write(collected,have_collected_url)
            funcforkick.projetcdata_txt_write(item,item_collect)
            funcforkick.projetcdata_txt_write(rewards,rewards_collect)
            #funcforkick.index_write(index,'data/middle60project/index_value20.txt','data/middle60project/index_keys20.txt')
            funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
            funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
            funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
            funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            #reset list
            total_item=[]
            total_rewards_backers_distribution=[]
            total_rewards_pledge_limit=[]
            total_rewards_pledged_amount=[]
            collectedfile=[]
            time.sleep(5)
        end = time.time()
        #conditional_insert(cursor, item)
    sys.stdout.write("\rthis spider has already read %d projects and time: %.4f/projects and  %d new add, %d updated, %d repeated" % (counts,end-start,new_add,updated,repeated))
    sys.stdout.flush()
    return count,total_item,total_rewards_pledge_limit,total_rewards_pledged_amount,total_rewards_backers_distribution

for someurl in file:
    #@profile
    #someurl=list(someurl)
    print someurl
    print type(someurl)
    (counts,total_item,total_rewards_pledge_limit,total_rewards_pledged_amount,total_rewards_backers_distribution)=operat(counts,someurl,total_item,total_rewards_pledge_limit,total_rewards_pledged_amount,total_rewards_backers_distribution)

#funcforkick.writeacsvprocess(saving_file,item_headers,total_item)
#funcforkick.writeacsvprocess(rewards_backers_distribution,rewards_headers,total_rewards_backers_distribution)
#funcforkick.writeacsvprocess(rewards_pledge_limit,rewards_headers,total_rewards_pledge_limit)
#funcforkick.writeacsvprocess(rewards_pledged_amount,rewards_headers,total_rewards_pledged_amount)
            #reset list
        #time.sleep(1)
#funcforkick.index_write(index,'data/middle60project/index_value20.txt','data/middle60project/index_keys20.txt')
print 'saving process completed'

#end = time.time()
#print end-start