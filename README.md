# CoWinNotification
This repo contain python code which send notification via telegram for cowin slots available

# To generate Token for telegram:
1. Open the telegram app and search for @BotFather.
2. Click on the start button or send “/start”.
3. Then send “/newbot” message to set up a name and a username.
4. After that you will receive a token. Replace this token in code.

# To generate chat id:
1. Create or go to telegram group which you want to send messages.
2. add the bot user you created in generate token process.
3. send following message to this group: /my_id @YourBotUserName
4. Open your brower and go to below URL(Replace TOKENID in url with your tokenID which you generated)
https://api.telegram.org/botTOKENID/getUpdates
5. You will get a chat id. If you dont get a chat id then perform step 3 and 4 again

Replace Pincode, token id and chat id in above code.

You need to setup cron to run above code every minute
crontab -e
cron expression: * * * * * /usr/bin/python CowinNotificationByPincode.py
