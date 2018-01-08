# -*- coding: utf-8 -*-
#Cat_Bot
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,ast,os,subprocess,requests

cl = LINETCR.LINE()
cl.login(token='EogKbEyCe7yYekgBHbT8.6S7B6iV24SxpyyIZPkjUga.P2Sp7DZuGNcfESz/YOr3WOauimX07jn0tONXkIcTZ00=')
cl.loginResult()

ki = LINETCR.LINE()
ki.login(token='EotW0N3d7wwrh5YXZ9J0.wO8FExqopCH2OtQ39ZGtqa.zn33Vv29GlNwK/8fPsgbLAXk5qhaWZ+iIDZiVTGpxdI=')
ki.loginResult()

ki2 = LINETCR.LINE()
ki2.login(token='Eo7uWMiKIBMErQ7satZ8.Y2rawCeX0fURueP0mx/hoa.Ql5xEva7uo1cNnSamgj6wcT1QhGqkXPexPE0BOR0qEY=')
ki2.loginResult()

ki3 = LINETCR.LINE()
ki3.login(token='EoYyjBmwBaWF9pXGw0t9.VuiggVG+2eQkzNXltNSfMq.Z4l/lYE4vEXJYnog8BDoX9PoDEwc1a9XTriIHZ+NgNg=')
ki3.loginResult()
print "= = = = = = BOT CAT LOGIN SUCCESS = = = = = ="
reload(sys)
sys.setdefaultencoding('utf-8')
helpMessage ="""╔════════════════
║Fuck♥ FUCK-U ♥Fuck
╠══════════════════
║❂͜͡☆➣Set:changenamelock:on/off
║   ☆ล็อคชื่อกลุ่ม [เปิด/ปิด]
╠══════════════════
║❂͜͡☆➣Set:blockinvite:on/off
║   ☆ล็อคการเชิญสมาชิก [เปิด/ปิด]
╠══════════════════
║❂͜͡☆➣Set:ownerlock:on/off
║   ☆ล็อคแอดมินกลุ่ม [เปิด/ปิด]
╠══════════════════
║❂͜͡☆➣Set:addblacklist
║   ☆เพิ่มบัญชีดำ
╠══════════════════
║❂͜͡☆➣Set:addwhitelist
║   ☆เพิ่มบัญชีขาว
╠══════════════════
║❂͜͡☆➣Sp:inviteurl
║   ☆เปิดลิงก์
╠══════════════════
║❂͜͡☆➣Sp:DenyURLInvite
║   ☆ปิดลิงก์
╠══════════════════
║❂͜͡☆➣Sp:cancelinvite
║   ☆ยกเลิกค้างเชิญ
╠══════════════════
║❂͜͡☆➣Sp:groupcreator
║   ☆เช็คเจ้าของกลุ่ม
╠══════════════════
║❂͜͡☆➣Setlastpoint
║   ☆ตั่งจุดอ่าน
╠══════════════════
║❂͜͡☆➣Viewlastseen
║   ☆ดูผู้ใช้ที่อ่าน
╠══════════════════
║ZssiK♥ line://ti/p/~esci_ ♥KissZ
╚════════════════
"""
KAC=[cl,ki,ki2,ki3]
Amid = cl.getProfile().mid
Bmid = ki.getProfile().mid
Cmid = ki2.getProfile().mid
Dmid = ki3.getProfile().mid
Bots=[Amid,Bmid,Cmid,Dmid]
Creator="u541bbaba15d68f3a652106a0de5a3e94"
admin=["u541bbaba15d68f3a652106a0de5a3e94"]

wait = {
    "LeaveRoom":True,
    "AutoJoin":True,
    "Members":1,
    "AutoCancel":True,
    "AutoKick":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Qr":True,
    "Timeline":True,
    "Contact":True,
    "lang":"JP",
    "BlGroup":{}
    }

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1


def bot(op):
    try:
#--------------------END_OF_OPERATION--------------------
        if op.type == 0:
            return
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------NOTIFIED_INVITE_INTO_ROOM-------------
        if op.type == 22:
            cl.leaveRoom(op.param1)
#--------------------INVITE_INTO_ROOM--------------------
        if op.type == 21:
            cl.leaveRoom(op.param1)
#--------------NOTIFIED_INVITE_INTO_GROUP----------------
        if op.type == 13:
	    print op.param3
            if op.param3 in Amid:
		if op.param2 in Creator:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Creator:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Creator:
		    ki2.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Amid:
		if op.param2 in Bmid:
		    cl.acceptGroupInvitation(op.param1)
            if op.param3 in Amid:
		if op.param2 in Cmid:
		    cl.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Bmid:
		if op.param2 in Amid:
		    ki.acceptGroupInvitation(op.param1)
            if op.param3 in Bmid:
		if op.param2 in Cmid:
		    ki.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
            if op.param3 in Cmid:
		if op.param2 in Amid:
		    ki3.acceptGroupInvitation(op.param1)
            if op.param3 in Cmid:
		if op.param2 in Bmid:
		    ki2.acceptGroupInvitation(op.param1)
#--------------------------------------------------------
	    if Amid in op.param3:
                if wait["AutoJoin"] == True:
		    G = cl.getGroup(op.param1)
                    if len(G.members) <= wait["Members"]:
                        cl.rejectGroupInvitation(op.param1)
		    else:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			ki2.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
                else:
		    if op.param2 in admin:
                        cl.acceptGroupInvitation(op.param1)
			G = cl.getGroup(op.param1)
			G.preventJoinByTicket = False
			cl.updateGroup(G)
			Ti = cl.reissueGroupTicket(op.param1)
			ki.acceptGroupInvitationByTicket(op.param1,Ti)
			ki2.acceptGroupInvitationByTicket(op.param1,Ti)
			G.preventJoinByTicket = True
			cl.updateGroup(G)
		    else:
                        cl.rejectGroupInvitation(op.param1)
	    else:
                if wait["AutoCancel"] == True:
		    if op.param3 in Bots:
			pass
		    else:
                        cl.cancelGroupInvitation(op.param1, [op.param3])
		else:
		    if op.param3 in wait["blacklist"]:
			cl.cancelGroupInvitation(op.param1, [op.param3])
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendText(msg.to,"ลบบัญชีดำสำเร็จ (｀・ω・´)"+tm)
		    else:
			pass
#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["AutoKick"] == True:
		    try:
			if op.param3 in Bots:
			    pass
		        if op.param2 in Bots:
			    pass
		        else:
                            G = ki2.getGroup(op.param1)
                            G.preventJoinByTicket = False
                            ki2.updateGroup(G)
                            Ti = ki2.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                            G.preventJoinByTicket = True
                            ki2.updateGroup(G)
		            ki3.kickoutFromGroup(op.param1,[op.param2])
                            ki3.leaveGroup(msg.to)
                        if op.param2 in wait["blacklist"]:
                            pass
		        else:
			    ki2.inviteIntoGroup(op.param1,[op.param3])
		    except:
		        try:
			    if op.param2 not in Bots:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        ki2.inviteIntoGroup(op.param1,[op.param3])
		        except:
			    print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
		    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
		else:
		    pass
		
#-----------------------------------------------------------------
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        G = ki3.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki3.updateGroup(G)
                        Ti = ki3.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
		        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
			    ki3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    ki3.leaveGroup(msg.to)
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
		        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki3.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    ki3.leaveGroup(msg.to)
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ti = ki.reissueGroupTicket(op.param1)
                        ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
		        ki3.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            ki2.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in Bots:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    ki3.leaveGroup(msg.to)
                    G = ki2.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki2.updateGroup(G)
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in Bots:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------------------------------------
                if Creator in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        ki3.acceptGroupInvitationByTicket(op.param1,Ti)
		        ki3.kickoutFromGroup(op.param1,[op.param2])
                        ki3.leaveGroup(msg.to)
                    except:
                        try:
			    if op.param2 not in Bots:
                                ki2.kickoutFromGroup(op.param1,[op.param2])
			    if op.param2 in wait["blacklist"]:
			        pass
			    else:
			        cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    cl.inviteIntoGroup(op.param1,[op.param3])
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

#--------------------------NOTIFIED_UPDATE_GROUP---------------------
        if op.type == 11:
            if wait["Qr"] == True:
		if op.param2 in Bots:
		    pass
		else:
                    X = ki2.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ki2.updateGroup(X)
                    Ti = ki2.reissueGroupTicket(msg.to)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ti) #kicker join
                    X.preventJoinByTicket = True
                    ki2.updateGroup(X)
                    ki3.kickoutFromGroup(msg.to,[op.param2])
                    ki3.leaveGroup(msg.to)
            else:
                pass
#--------------------------RECEIVE_MESSAGE---------------------------
        if op.type == 26:
            msg = op.message
#----------------------------------------------------------------------------
            if msg.contentType == 13:
                if wait["wblacklist"] == True:
		    if msg.contentMetadata["mid"] not in admin:
                        if msg.contentMetadata["mid"] in wait["blacklist"]:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            ki.sendText(msg.to,"ผู้ใช้นี้ได้อยู่ในบัญชีดำอยู่แล้ว (｀・ω・´)"+tm)
                            wait["wblacklist"] = False
                        else:
                            wait["blacklist"][msg.contentMetadata["mid"]] = True
                            wait["wblacklist"] = False
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            ki.sendText(msg.to,"เพิ่มผู้ใช้นี้ในบัญชีดำแล้ว (｀・ω・´)"+tm)
		    else:
			pass
			

                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendText(msg.to,"ลบผู้ใช้นี้ในบัญชีดำแล้ว (｀・ω・´)"+tm)
                        wait["dblacklist"] = False

                    else:
                        wait["dblacklist"] = False
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendText(msg.to,"ผู้ใช้นี้ไม่ได้อยู่ในบัญชีดำ (｀・ω・´)"+tm)
#--------------------------------------------------------
            elif msg.text is None:
                return
#--------------------------------------------------------
            elif msg.text in ["Hp","Help","คำสั่ง"]:
                if msg.from_ in admin:
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpMessage)
#--------------------------------------------------------
	    elif msg.text in ["Group creator","Gcreator","gcreator"]:
		ginfo = cl.getGroup(msg.to)
		gCreator = ginfo.creator.mid
                msg.contentType = 13
                msg.contentMetadata = {'mid': gCreator}
                cl.sendMessage(msg)
                now2 = datetime.datetime.now()
                nowT = datetime.datetime.strftime(now2,"%H")
                nowM = datetime.datetime.strftime(now2,"%M")
                nowS = datetime.datetime.strftime(now2,"%S")
                tm = "\n\n"+nowT+":"+nowM+":"+nowS
		cl.sendText(msg.to,"นี่คือผู้สร้างกลุ่ม (｀・ω・´)"+tm)
#--------------------------------------------------------
            elif msg.text in ["Set:cancelinvite","Set:Cancelinvite"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendText(msg.to,"ยกเลิกค้างเชิญสำเร็จ (｀・ω・´)"+tm)
                    else:
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendText(msg.to,"ไม่มีคำเชิญในตอนนี้ (｀・ω・´)"+tm)
                else:
                    pass
#--------------------------------------------------------
            elif msg.text in ["OpenAll","STzOP"]:
		if msg.from_ in admin:
                    wait["AutoJoin"] = True
                    wait["AutoCancel"] = True
                    wait["Qr"] = True
                    wait["AutoKick"] = True
#--------------------------------------------------------
            elif msg.text in ["Sp:inviteurl","Sp:Inviteurl"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    cl.sendText(msg.to,"เปิดลิงก์สำเร็จ (｀・ω・´)"+tm)
                else:
                    pass
#--------------------------------------------------------
            elif msg.text in ["Sp:DenyURLInvite","Sp:Denyurlinvite"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    cl.sendText(msg.to,"ปิดลิงก์สำเร็จ (｀・ω・´)"+tm)
                else:
                    pass
#--------------------------CEK SIDER------------------------------
            elif "Viewlastseen" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          cl.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        cl.sendText(msg.to, "Lurking has not been set.")
            elif "Setlastpoint" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "Setlastpoint-" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))
#--------------------------------------------------------
            elif msg.text in ["Admin:delinvite"]:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                cl.sendText(msg.to,"All invitations have been refused")
#--------------------------------------------------------
            elif msg.text in ["Sp:reinvite"]:
		if msg.from_ in admin:
		    G = cl.getGroup(msg.to)
                    ginfo = cl.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ticket = cl.reissueGroupTicket(msg.to)
                    ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.2)
                    ki3.acceptGroupInvitationByTicket(msg.to,Ticket)
                    G = cl.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    ki3.leaveGroup
		else:
		    pass

#--------------------------------------------------------
            elif msg.text in ["timeline"]:
		try:
                    url = cl.activity(limit=5)
		    cl.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#--------------------------------------------------------
            elif msg.text in ["S:bye"]:
		if msg.from_ in admin:
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                else:
                    pass
#--------------------------------------------------------
            elif msg.text in ["Set:addblacklist"]:
                wait["wblacklist"] = True

            elif msg.text in ["Set:addwhitelist"]:
                wait["dblacklist"] = True
#--------------------------------------------------------
            elif msg.text in ["Kill ban"]:
		if msg.from_ in admin:
                    if msg.toType == 2:
                        G = ki2.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki2.updateGroup(G)
                        Ti = ki2.reissueGroupTicket(op.param1)
                        superkick.acceptGroupInvitationByTicket(op.param1,Ti)     
                        group = superkick.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            now2 = datetime.datetime.now()
                            nowT = datetime.datetime.strftime(now2,"%H")
                            nowM = datetime.datetime.strftime(now2,"%M")
                            nowS = datetime.datetime.strftime(now2,"%S")
                            tm = "\n\n"+nowT+":"+nowM+":"+nowS
                            cl.sendText(msg.to,"ไม่มีสามชิกที่ถูกแบน (｀・ω・´)"+tm)
                            superkick.leaveGroup(msg.to)
                            return
                        for jj in matched_list:
                            superkick.kickoutFromGroup(msg.to,[jj])
                        ki3.leaveGroup(msg.to)
		else:
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    cl.sendText(msg.to,"ไม่สามารถลบผู้สร้างบอทได้ (｀・ω・´)"+tm)

#--------------------------------------------------------



        if op.type == 59:
            print op


    except Exception as error:
        print error


#thread2 = threading.Thread(target=nameUpdate)
#thread2.daemon = True
#thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

