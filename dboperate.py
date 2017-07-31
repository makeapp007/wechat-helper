#!/usr/bin/python3
#-*- coding:UTF-8 -*-
import _sqlite3
import xlrd
import uuid

#init
cx = _sqlite3.connect("tickets.db")

xlsfile_early = r'name.xlsx'

book_early = xlrd.open_workbook(xlsfile_early)
print(book_early)

class ticketInfo:
    def initInfo(name,ephone,cell,email,wechatID):
        self.tid = uuid.uuid1()
        self.tname = name
        self.tcell = cell
        self.temail = email
        self.wechatID = wechatID
        self.tstatus = 0

    # db operate
    def insert_db(self):
        sql = "insert into TB_TICKETINFO(TID ,TNAME  ,TCELL,TEMAIL,TSTATUS,wechatID) \
               VALUES ( %s,%s,%s,%s,%s,%s)" % (self.tid,self.tname, self.tcell,self.temail, self.tstatus,self.wechatID)
        cx.execute(sql)
        cx.commit()
    # end

#excel operate
def read_excel():
    #early excel
    sheet = book_early.sheets()[0]  # sheets返回一个sheet列表
    nrows = sheet.nrows  # 行总数
    ncols = sheet.ncols  # 列总数

    tInfo = ticketInfo()

    for i in range(1,nrows):
        tInfo.tid =  "'" + str(uuid.uuid1()) + "'"
        tInfo.tstatus = "'" + str(0) + "'"
        tInfo.tname = "'" + sheet.cell_value(i, 1) + "'"
        tInfo.tcell = "'" + str(sheet.cell_value(i, 2)) + "'"
        tInfo.temail = "'" + sheet.cell_value(i, 3) + "'"
        wechatID=""
        try:
            wechatID=str(int(sheet.cell_value(i, 4)))
        except:
            wechatID=str(sheet.cell_value(i, 4))
        tInfo.wechatID = "'" + wechatID+ "'"
        tInfo.insert_db()
    #end


read_excel()

cx.close()
