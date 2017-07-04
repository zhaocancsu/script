#!/usr/bin/env python
#coding=utf8


'''
Created on 2017-05-22

@author: zhaocan
'''
import random
import httplib,urllib
import json
import threading
import datetime


def listSub(pList,sList):
    for l in sList:
        pList.remove(l)
        
def listSubHex(pList,sList):
    for l in sList:
        pList.remove(str(int(l,16)))        
        
def httpPost(uri,data):
    httpClient = None
    try:
        params = urllib.urlencode(data)
        headers = {"Content-type": "application/x-www-form-urlencoded"}
        #, "Accept": "text/plain"
 
        httpClient = httplib.HTTPConnection("localhost:8080",timeout=30)
        httpClient.request("POST", '/guandan-pokerbot/'+uri, params, headers)
 
        response = httpClient.getresponse()
        #print response.status
        #print response.reason
        #print response.getheaders() #获取头信息
        return response.read()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()

def fourRobotplay():
    cardnumstatus = [0,0,0,0]
    thenprofitlist = []
    cardset = ['5','10','56','42','24','37','25','52','20','57','78','29','61','1','6','60','28','38','21','33','9','53','13','41','2','34','45','17','22','44','59','27','12','54','49','7','39','3','35','18','50','11','43','40','26','55','23','8','58','36','51','19','4','79']
    fullDeck = cardset*2

    u1pc = random.sample(fullDeck,27)

    listSub(fullDeck,u1pc)
    u2pc = random.sample(fullDeck,27)

    listSub(fullDeck,u2pc)
    u3pc = random.sample(fullDeck,27)

    listSub(fullDeck,u3pc)
    u4pc = fullDeck

    
    batchNo = str(random.randint(1, 100000000))
    roomNo = str(random.randint(1,100))
    tableNo = str(random.randint(1,100))

    
    print(batchNo+"_"+roomNo+"_"+tableNo+".txt")
    
    httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8001','identity':'1','init_cards':','.join(u1pc)})
    httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8002','identity':'1','init_cards':','.join(u2pc)})
    httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8003','identity':'1','init_cards':','.join(u3pc)})
    httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8004','identity':'1','init_cards':','.join(u4pc)})
    
    #u1pcStr = '22,23,59,12,79,34,34,19,54,17,36,9,55,42,35,79,49,53,51,24,13,10,78,8,28,37,1'
    #u1pc = u1pcStr.split(',')
    #u2pcStr = '39,36,55,45,6,10,18,39,23,20,8,7,40,52,56,60,58,41,43,33,7,5,45,25,61,29,17'
    #u2pc = u2pcStr.split(',')
    #u3pcStr = '18,53,21,59,51,22,13,52,44,24,50,9,61,11,42,29,27,21,11,27,2,6,57,35,33,41,26'
    #u3pc = u3pcStr.split(',')
    #u4pcStr = '38,3,4,5,56,37,25,20,57,78,1,60,28,38,2,44,12,54,49,3,50,43,40,26,58,19,4'
    #u4pc = u4pcStr.split(',')
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8001','identity':'1','init_cards':u1pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8002','identity':'1','init_cards':u2pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8003','identity':'1','init_cards':u3pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8004','identity':'1','init_cards':u4pcStr})
    
    #u1pcStr = '78,11,12,22,50,25,56,3,43,8,4,36,28,21,40,8,23,26,10,20,26,20,45,1,51,54,37'
    #u1pc = u1pcStr.split(',')
    #u2pcStr = '40,17,59,27,54,57,22,42,42,56,12,49,29,29,35,6,34,2,78,27,39,19,58,52,35,53,28'
    #u2pc = u2pcStr.split(',')
    #u3pcStr = '60,33,5,79,4,52,5,44,19,13,10,17,55,34,23,6,79,61,21,39,24,36,41,24,53,7,9'
    #u3pc = u3pcStr.split(',')
    #u4pcStr = '38,18,37,25,57,61,1,60,38,33,9,13,41,2,45,44,59,49,7,3,18,50,11,43,55,58,51'
    #u4pc = u4pcStr.split(',')
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8001','identity':'1','init_cards':u1pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8002','identity':'1','init_cards':u2pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8003','identity':'1','init_cards':u3pcStr})
    #httpPost("dealcards", {'batch_no':batchNo,'room_no':roomNo,'table_no':tableNo,'user_id':'8004','identity':'1','init_cards':u4pcStr})
    
    #data = httpPost("startgame", {'batch_no':batchNo,'user_list':'[{"identity":"1","role":"0","user_id":"8001"},{"identity":"1","role":"2","user_id":"8002"},{"identity":"1","role":"1","user_id":"8003"}]','table_cards':','.join(tc)})
    
    
    data = httpPost("startgame", {'batch_no':batchNo,'user_list':'[{"identity":"1","position":"0","user_id":"8001"},{"identity":"1","position":"1","user_id":"8002"},{"identity":"1","position":"2","user_id":"8003"},{"identity":"1","position":"3","user_id":"8004"}]','master_card':'0x22'})
    #print(data)
    jsonObj = json.loads(data)
    if(jsonObj['status'] != '0000'):
        print('牌局开始失败')
        return   
    #print(jsonObj['result'])

    while True:
        #print(thenprofitlist)
        if (0 == len(u1pc) and 0 == len(u3pc)) or (0 == len(u2pc) and 0 == len(u4pc)):
            print('牌局结束')
            break
        if 0 != len(u1pc):
            if (1 != len(thenprofitlist) or (1 == len(thenprofitlist) and '8001' == thenprofitlist[0])):
                upc1 = httpPost("playcards", {'batch_no':batchNo,'user_id':'8001'})
                jsonUpc1 = json.loads(upc1)
                pRst = jsonUpc1['result']
                print('8001->'+pRst)
                if(jsonUpc1['status'] != '0000'):
                    break
                else:
                    if pRst == "" and len(thenprofitlist) > 0 and thenprofitlist[0] == '8001':
                        thenprofitlist.pop(0)
                    if pRst:
                        if len(thenprofitlist) > 0:
                            thenprofitlist = []
                        listSubHex(u1pc,pRst.split(','))
                        if 0 == len(u1pc):
                            if cardnumstatus[0] == 0:
                                if (cardnumstatus[1] == 1):
                                    thenprofitlist = ['8003','8004','8003']
                                elif (cardnumstatus[3] == 1):
                                    thenprofitlist = ['8002','8003']
                                else:
                                    thenprofitlist = ['8002','8003','8004','8003']         
                
                                cardnumstatus[0] = 1

        if 0 != len(u2pc):
            if (1 != len(thenprofitlist) or (1 == len(thenprofitlist) and '8002' == thenprofitlist[0])):
                upc2 = httpPost("playcards", {'batch_no':batchNo,'user_id':'8002'})
                jsonUpc2 = json.loads(upc2)
                pRst = jsonUpc2['result']
                print('8002->'+pRst)
                if(jsonUpc2['status'] != '0000'):
                    break
                else:
                    if pRst == "" and len(thenprofitlist) > 0 and thenprofitlist[0] == '8002':
                        thenprofitlist.pop(0)
                    if pRst:
                        if len(thenprofitlist) > 0:
                            thenprofitlist = []
                        listSubHex(u2pc,pRst.split(','))
                        if 0 == len(u2pc):
                            if cardnumstatus[1] == 0:
                                if (cardnumstatus[2] == 1):
                                    thenprofitlist = ['8004','8001','8004']
                                elif (cardnumstatus[0] == 1):
                                    thenprofitlist = ['8003','8004']
                                else:
                                    thenprofitlist = ['8003','8004','8001','8004']
                                cardnumstatus[1] = 1
        if 0 != len(u3pc):
            if (1 != len(thenprofitlist) or (1 == len(thenprofitlist) and '8003' == thenprofitlist[0])):
                upc3 = httpPost("playcards", {'batch_no':batchNo,'user_id':'8003'})
                jsonUpc3 = json.loads(upc3)
                pRst = jsonUpc3['result']
                print('8003->'+pRst)
                if(jsonUpc3['status'] != '0000'):
                    break
                else:
                    if pRst == "" and len(thenprofitlist) > 0 and thenprofitlist[0] == '8003':
                        thenprofitlist.pop(0)
                    if pRst:
                        if len(thenprofitlist) > 0:
                            thenprofitlist = []
                        listSubHex(u3pc,pRst.split(','))
                        if 0 == len(u3pc):
                            if cardnumstatus[2] == 0:
                                if (cardnumstatus[3] == 1):
                                    thenprofitlist = ['8001','8002','8001']
                                elif (cardnumstatus[0] == 1):
                                    thenprofitlist = ['8004','8001']
                                else:
                                    thenprofitlist = ['8004','8001','8002','8001']
                                cardnumstatus[2] = 1
        if 0 != len(u4pc):
            if (1 != len(thenprofitlist) or (1 == len(thenprofitlist) and '8004' == thenprofitlist[0])):
                upc4 = httpPost("playcards", {'batch_no':batchNo,'user_id':'8004'})
                jsonUpc4 = json.loads(upc4)
                pRst = jsonUpc4['result']
                print('8004->'+pRst)
                if(jsonUpc4['status'] != '0000'):
                    break
                else:
                    if pRst == "" and len(thenprofitlist) > 0 and thenprofitlist[0] == '8004':
                        thenprofitlist.pop(0)
                    if pRst:
                        if len(thenprofitlist) > 0:
                            thenprofitlist = []
                        listSubHex(u4pc,pRst.split(','))
                        if 0 == len(u4pc):
                            if cardnumstatus[3] == 0:
                                if (cardnumstatus[0] == 1):
                                    thenprofitlist = ['8002','8003','8002']
                                elif (cardnumstatus[2] == 1):
                                    thenprofitlist = ['8002','8002']
                                else:
                                    thenprofitlist = ['8001','8002','8003','8002']
                                cardnumstatus[3] = 1

def multiGame():
    threads = []
    for i in range(600):
        t = threading.Thread(target=fourRobotplay)
        threads.append(t)
        t.start()

if __name__ == '__main__':
    begin = datetime.datetime.now()
    fourRobotplay()
    #multiGame()
    end = datetime.datetime.now()
    print(end-begin)
    
    