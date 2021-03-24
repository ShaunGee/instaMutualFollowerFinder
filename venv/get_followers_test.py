from get_followers import Get_followers

user1 = input("enter user 1: ")
user2 = input("enter user 2: ")

getFollowers = Get_followers(user1,user2)
getFollowers.get_mutual_followers()