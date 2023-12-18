# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# In this file characters, their colors, emotions and stuff are defined                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





image hikari a1 = "/images/characters/hikari/hikari idle.png"
image hikari a2 = "images/characters/hikari/hikari happy.png"

# image=hikari takes that "hikari" from above line, and I we can use a1 and a2 tags in dialogue to represent different emotions
# example:
# 		hi a1 "Test example"
# otherwise it would be
# 		show hikari a1 at centre
# 		hi "Test example

define hi = Character("Hikari", image="hikari", ctc="ctc_anchored",ctc_position="fixed")
define re = Character("Reki")
define ra = Character("Rakka")
define ch = Character("Chie", color="#deddd5", ctc="ctc_anchored",ctc_position="fixed")
