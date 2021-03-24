from igramscraper.instagram import Instagram
from time import sleep

class Get_followers:

    '''
    This class will recieve two seperate users as inputs then compare both of thier followers to find mutual
    followers. It will then return a list of followers

    '''

    def __init__(this, user1,user2):
        this.user1 = user1
        this.user2 = user2


        instagram = Instagram()
        instagram.with_credentials('shaungumbaketi@gmail.com', 'Yakapus0123')
        instagram.login()

        sleep(3)

        user1FollowersList = []
        user2FollowersList = []
        this.mutualFollowers = []

        account1 = instagram.get_account(this.user1)
        sleep(2)
        account2 = instagram.get_account(this.user2)
        sleep(2)


        user1Followers = instagram.get_followers(account1.identifier,account1.followed_by_count,100,delayed=True)
        user2Followers = instagram.get_followers(account2.identifier, account1.followed_by_count, 100, delayed=True)

        print (user1Followers)

        for f in user1Followers['accounts']:
            user1FollowersList.append(f.username)

        for f in user2Followers['accounts']:
            user2FollowersList.append(f.username)

        this.mutualFollowers = set(user1FollowersList) & set(user2FollowersList)



    def get_mutual_followers(this):
        for mf in this.mutualFollowers:
            print (mf)




user1 = input("enter user 1: ")
user2 = input("enter user 2: ")

getFollowers = Get_followers(user1,user2)
getFollowers.get_mutual_followers()











