# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# In this file characters, their colors, emotions and stuff are defined                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #





image hikari n = "/images/characters/hikari/hikari neutral.png"
image hikari h = "images/characters/hikari/hikari happy.png"

image chie n = "/images/characters/chie/chie neutral.png"
image chie h = "/images/characters/chie/chie happy.png"
image chie s = "/images/characters/chie/chie sad.png"


# image=hikari takes that "hikari" from above line, and I we can use a1 and a2 tags in dialogue to represent different emotions
# example:
# 		hi a1 "Test example"
# otherwise it would be
# 		show hikari a1 at centre
# 		hi "Test example

define hi = Character("Hikari", image="hikari", ctc="ctc_anchored",ctc_position="fixed")
define re = Character("Reki")
define ra = Character("Rakka")
define ch = Character("Chie", image="chie", color="#deddd5", ctc="ctc_anchored",ctc_position="fixed")
