# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:57:47 2020

@author: user
"""
import random


class whispers():
  def __init__(self):
    self.strWord = ""
    self.lisLove = ["「 你真的跟北科很有緣。」\n「 但我更想跟你有緣。」" , 
                    "「 我不是天生溫柔，而是只想對你溫柔。」",
                    "「 我最近要去配眼鏡了」\n「為什麼？」\n「除了你，我看不見別人。」",
                    "「 我一點都不遺憾沒有在過去遇見你，因為遇見你以後，最美好的時光正開始了。」" ,
                    "「 不是我喜歡的樣子你都有，而是你有的樣子，我都喜歡。」" ,
                    "「你猜猜我的心在哪邊？」\n「肯定左邊。」\n「錯，在你那邊。」" ,
                    "「你再怎麼完美，還是會有缺點。」\n「什麼？」\n「缺點我。」" , 
                    "「總會有一個人出現，讓人原諒過去日子的艱難。\n當找到最好的那個，以前過往真的都不重要了，那個人就是你。" ,
                    "「不是因為需要你，所以愛你，而是因為愛你，所以需要你。」" , 
                    "「 你知道我有一個超能力嗎？」\n「什麼？」\n「超級喜歡你。」" , 
                    "「只要你的心中有我，我的心中有你，到哪都是天堂。」" ,
                    "「我要的很簡單，只要你在，我在。」" , 
                    "「我的青春，就是用來尋找你。」" , 
                    "「花有什麼好種的？來跟我種草莓。」" ,
                    "「我們浪漫一點好不好，……我浪點，你慢點。」" ,
                    "「 你知道什麼蛋最漂亮嗎？」\n「你的臉蛋。」" ,
                    "「就算你站在千萬人之中，我也能一眼看到你。」" ,
                    "「想和你喝酒是假的，想醉你懷裡是真的。」"]
    
    
  def random_love(self):
    self.strWord = random.choice(self.lisLove)
    self.lisLove.remove(self.strWord)
    print( '\n' + self.strWord + '\n' )
    
  
  @staticmethod
  def say_patient_to_user():
    print("請耐心等候...(預估時間為 10 秒鐘)")
      
    