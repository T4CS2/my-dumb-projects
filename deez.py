import time
import webbrowser 
import random
import os

charity_donate_websites = [
    "https://www.redcross.org/donate/",
    "https://www.unicef.org/donate/",
    "https://donate.doctorswithoutborders.org/",
    "https://support.worldwildlife.org/",
    "https://www.oxfam.org/donate",
    "https://www.savethechildren.org/donate",
    "https://www.habitat.org/donate/",
    "https://www.feedingamerica.org/take-action/donate",
    "https://www.amnesty.org/en/donate/",
    "https://www.charitywater.org/donate/",
    "https://www.directrelief.org/donate/",
    "https://donate.cancer.org/",
    "https://www.charitynavigator.org/index.cfm?bay=content.view&cpid=31",
    "https://www.wateraid.org/us/donate",
    "https://support.nature.org/site/Donation2",
    "https://www.heifer.org/give",
    "https://give.hrc.org/page/31037/donate/1",
    "https://www.smiletrain.org/donate",
    "https://www.plannedparenthood.org/donate",
    "https://www.stjude.org/donate",
    "https://www.mercycorps.org/donate",
    "https://www.actionagainsthunger.org/donate",
    "https://www.charitysmith.org/donate",
    "https://donate.thp.org/",
    "https://www.redcross.ca/donate",
    "https://donate.unhcr.org/int/",
    "https://www.charity.org/donate",
    "https://support.crs.org/donate",
    "https://www.care.org/donate",
    "https://www.charitywatch.org/donate",
    "https://www.kiva.org/donate",
    "https://www.sos-usa.org/ways-to-help/donate",
    "https://www.samaritanspurse.org/our-ministry/donate-online/",
    "https://support.wwf.org.uk/donate",
    "https://donate.msf.org/",
    "https://unfoundation.org/ways-to-give/",
    "https://www.icrc.org/en/donate",
    "https://www.wish.org/donate",
    "https://www.globalgiving.org/donate/",
    "https://www.orphandoctor.com/donate/",
    "https://support.peta.org/page/7/donate",
    "https://www.feedthechildren.org/give/",
    "https://www.americares.org/en/donate/",
    "https://www.wfp.org/donate",
    "https://engage.us.greenpeace.org/donate/",
    "https://www.bbrfoundation.org/donate",
    "https://www.rainforest-alliance.org/donate",
    "https://www.alsa.org/donate/",
    # this took me already so long i cant add more
]

random_website = random.choice(charity_donate_websites)
os.system('clear')
print('The Random Charity Donation Game')
print('\n\n')

time.sleep(0.3)
print('How this works: The Script picks a random charity site included in its database, and it will redirect you to the website.')
time.sleep(1)
print('\nYou are going to set a limit for yourself from "x" to "y" so you dont go bankrupt.')
time.sleep(1)
print('\nAfter setting the money number, the site will automatically open after 1 second.')
time.sleep(1)
print("\nPlease select the money limit.")
print('\n')
RandomMoneyFrom = int(input('From: ')) 
RandomMoneyTo = int(input('To: '))
print('\nYou have set your limit as ' + str(RandomMoneyFrom) + ' to ' + str(RandomMoneyTo) + '$')
print('\n')

random_number = random.randint(RandomMoneyFrom, RandomMoneyTo)
print('\nYou will have to donate: $' + str(random_number))
print('incase of an error/acces denied, use the script again')
time.sleep(5)

print('\nRandom charity site will open soon.')
time.sleep(1)
webbrowser.open(random_website)


