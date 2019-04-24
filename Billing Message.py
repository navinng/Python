import datetime

class Msg_User():
    user_details = []
    messages = []
    common_msg = "Hi {name},\nThank you for the purchase on {date}.\nWe hope you are excited about using the product.\nJust as a remainder the purchase total was ${amount}.\nHave a great day.\n\n Team CFE"
    def add_usr(self,usr_name,usr_bill):
        today = datetime.date.today()
        todays_date = '{today.day}/{today.month}/{today.year}'.format(today=today)
        name = usr_name.capitalize()
        amt = "%.2f" %(usr_bill)
        detail = {
            "name": name, 
            "amt" : amt
            }
        detail["date"] = todays_date
        self.user_details.append(detail)
    
    def make_msgs(self):
        if len(self.user_details) > 0 :
            for detail in self.user_details :
                name = detail["name"]
                amount = detail["amt"]
                date = detail["date"]
                message = self.common_msg
                new_msg = message.format(name=name,amount=amount,date=date)
                self.messages.append(new_msg)
            return self.messages
  

obj = Msg_User()
obj.add_usr('John',100)
obj.add_usr('jIm',80)
obj.add_usr('MiKE',75)
obj.add_usr('cena',50)
obj.add_usr('maT',100)
print(obj.user_details)
mademsgs = obj.make_msgs()
print(mademsgs)