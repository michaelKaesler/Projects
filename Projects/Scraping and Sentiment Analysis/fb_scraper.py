# -*- coding: utf-8 -*-
"""
Created on Tue Oct 04 19:47:38 2016

@author: mkaesler

note: as of now this is only a scraper for the lincoln park zoo
"""


import urllib2
import json
import datetime
import fb_filter
import csv

# need to include this to get around encoding error when porting to csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def create_post_url(graph_url, APP_ID, APP_SECRET):
    #method to return 
    post_args = "/posts/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
    post_url = graph_url + post_args
 
    return post_url


def render_to_json(graph_url):
	#render graph url call to JSON
	web_response = urllib2.urlopen(graph_url)
	readable_page = web_response.read()
	json_data = json.loads(readable_page)
	
	return json_data

def scrape_posts_by_date(graph_url, date, post_data, APP_ID, APP_SECRET):
    
    
    #render URL to JSON
    page_posts = render_to_json(graph_url)
    
    #extract next page
    next_page = page_posts["paging"]["next"]
    
    #grab all posts
    page_posts = page_posts["data"]
    
    #boolean to tell us when to stop collecting
    collecting = True
    
    #for each post capture data
    for post in page_posts:
        try:
 
            current_post = [post["id"], post["message"],
                    post["created_time"]]
                                        #post["shares"]["count"]]        
                            
        except Exception:
            current_post = [ "error", "error", "error"] #, "error"]
            
        #print current_post
        if current_post[2] != "error":
                #compare dates
            # print date
            if date <= current_post[2]:
                # filtering to only the relevant posts
                filter_bool = fb_filter.filter_posts(current_post[1])
                
                if filter_bool == True:
                    post_data.append(current_post)
            
            elif date > current_post[2]:
                print "Done collecting"
                collecting = False
                break
        
            
    #If we still don't meet date requirements, run on next page            
    if collecting == True:
        scrape_posts_by_date(next_page, date, post_data, APP_ID, APP_SECRET)
        
    return post_data
    
def create_comments_url(graph_url, post_id, APP_ID, APP_SECRET):
    comments_args = post_id + "/comments/?key=value&access_token=" + APP_ID + "|" + APP_SECRET
    comments_url = graph_url + comments_args
    
    return comments_url
    
def get_comments_data(comments_url, comment_data, post_id):
    # render url to jason
    comments = render_to_json(comments_url)["data"]
    
    #for each comment capture data
    for comment in comments:
        try:
            current_comments = [comment["id"], comment["message"],
                            comment["created_time"], post_id]
            #print current_comments
            comment_data.append(current_comments)
            
        except Exception:
            current_comments = ["error", "error", "error","error"]
    
    #check if there is another page
    try:
        #extract next page
        next_page = comments["paging"]["next"]
    except Exception:
        next_page = None
            
            
    #if we have another page, recurse
    if next_page is not None:
        get_comments_data(next_page, comment_data, post_id)
    else:
        return comment_data


def write_csv_file_post(fname, data, *args, **kwargs):
    
    mycsv = csv.writer(open(fname, 'wb'), *args, **kwargs)
    for row in data:
       # row[0].encode('utf-8')
        #row[1].encode('utf-8')
       # row[2].encode('utf-8')
        mycsv.writerow(row)
        
def write_csv_file_comment(fname, data, *args, **kwargs):
    
    mycsv = csv.writer(open(fname, 'wb'), *args, **kwargs)
    for row in data:
       # row[0].encode('utf-8')
       # row[1].encode('utf-8')
       # row[2].encode('utf-8')
       # row[3].encode('utf-8')
        mycsv.writerow(row)
    
def main():
    
    print 'main called'
    
    APP_ID = '892623490881720'
    APP_SECRET = 'a6eea5fb91fa8315d1d4ba394c6034b4'
    
    company = 'lincolnparkzoo'
    graph_url = 'https://graph.facebook.com/'
    
    #the time of last weeks crawl
    last_crawl = datetime.datetime.now() - datetime.timedelta(weeks=198)
    last_crawl = last_crawl.isoformat()
    
    current_page = graph_url + company
    
    #extract post data
    post_url = create_post_url(current_page, APP_ID, APP_SECRET)
        
    post_data = []
    post_data = scrape_posts_by_date(post_url, last_crawl, post_data, APP_ID, APP_SECRET)
    
    print post_data
    print ""
    print "comments below"
    print ""
    
    # create list of comments
    comment_data = []
    # loop through and insert
    for post in post_data:
        comment_url = create_comments_url(graph_url, post[0], APP_ID, APP_SECRET)
        comments = get_comments_data(comment_url, comment_data, post[0])
        
    print comments
    print ""
    print "number of posts collected:", len(post_data)
    print "number of comments collected:", len(comments)
    
    print "writing posts"
    write_csv_file_post('posts.csv', post_data)
    print "writing comments"
    write_csv_file_comment('comments.csv', comments)
        
    
    
if __name__ == '__main__':
    main()
    