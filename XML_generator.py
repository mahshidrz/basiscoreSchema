# import pymssql, sqlite3
#
#
# def XML_generator(usedforid, LID, xml, propertyid=0, typeid=0, ownerid=0):
#     usedforid = 1002830
#     flag = 0
#     con = pymssql.connect(server='192.168.96.8', user='basiscore', password='BasisCore!1', database='exhibitor')
#     cursor = con.cursor()
#     cursor.execute('''select schemaid, parentid, id from  [exhibitor].[dbo].[Maintable] where id = {}'''.format(usedforid))
#
#     ret = cursor.fetchall()
#     schemaid = ret[0][0]
#     parentid = ret[0][1]
#     if parentid > 0:
#         usedforid = parentid
#         belongs = 3
#
#     conn = sqlite3.connect(':memory:')
#     cur = conn.cursor()
#     if (propertyid == 0) and (typeid == 0):
#         cur.execute('CREATE TABLE temp (prpid int , valueid int , multi int , question nvarchar, blongs int)')
#         cursor.execute('''
#         select propertyid, pv.ID, 0 from [exhibitor].[dbo].[prpValues] pv inner join[exhibitor].[dbo].[prpProperties]
#         pp on PropertyID = pp.ID where UsedForID = 1002830
#         and TypeID not in (199, 160, 161, 162) and (LID = {} or LID=0)
#         AND TypeID > 127 AND(pp.OwnerID = 0) order by pv.ID'''.format(LID))
#
#
#         # cur.execute('''insert into temp(prpid, valueid, blongs) {}'''.format(cursor.fetchall()))
#         result = cursor.fetchall()
#         return result
#
#
# print(XML_generator(1002830, 2, '', 0, 0, 0))

import pymssql
import xmltodict

db = pymssql.connect(server='172.19.20.46', user='sa', password='Salam1Salam2', database='exhibitor')
cursor = db.cursor()


def XML_generator(mid, used_for_id, lid, prp_id, type_id, owner_id, json_result):
    cursor.execute('''declare @xml nvarchar(max)
        EXECUTE  [dbo].[xmlGenerateDBsource]
        {},
        {},
        {},
        @xml out,
        {},
        {},
        {}

     select @xml'''.format(mid, used_for_id, lid, prp_id, type_id, owner_id))

    XML = cursor.fetchall()
    xml_to_dict = xmltodict.parse(XML)

    for key, value in json_result.items():
        for k, v in xml_to_dict.items():
            if key == v['question']:
                pass
