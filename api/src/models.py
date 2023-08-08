import uuid
import random


class Account:
   
   def __init__(self,name,value,acc_id= "",account = 0) -> None:
      self.id: str = acc_id
      self.name : str = name
      self.account: int = account
      self.value: float =  value
     
   def to_dict(self):
        return {
            "name": self.name,
            "account": self.account,
            "value": self.value
        }  