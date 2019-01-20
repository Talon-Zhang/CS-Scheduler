import itchat


status = 0


@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    global status
    print(status)
    defaultReply = '您的消息发送失败，请重新查看您的网络设置。\n是否重新发送？（Y/N)\n'
    alternateReply = '由于检测到您的账号存在短时间内大量登陆，根据相关法规，已将您的账号进行冻结。如有疑问，请联系微信客服。'
    if status:
        return alternateReply
    if msg['Text'] == 'Y'or msg['Text'] == 'y':
        status = 1
        return alternateReply
    elif msg['Text'] == 'N'or msg['Text'] == 'n':
        return
    return defaultReply


itchat.auto_login(hotReload=True)
itchat.run()