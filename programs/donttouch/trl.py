import os
import pyrogram
from pyrogram.types import Message




START_TEXT = """<b> 👋Hello {message.from_user.mention} ,
        
</code>Am a telegraph Uploader That Can Upload Photo, Video And Gif     
Simply send me photo, video or gif under 5MB I will upload it to Telegra.ph
want know more about this bot click help button        
Made With Love By</code> </b> <a href="t.me/devourdevils">DEVOURDEVIL </a>"""

HELP_TEXT = """`hello`  {message.from_user.mention},
</code>this bot par may be add somany cool and hot fewtures in feuture want know the
present commands of this bot click or press cmd button
and Just Send Me A Video/gif/photo under 5mb.
i'll upload it to telegra.ph and give you the direct link**</code>"""

CMD_TEXT = """Hello  {message.from_user.mention}
  my commands are"""

ID_TEXT = """THIS IS YOUR ID  </code>-{message.from_user.id}</code> """

DEV_TEXT = """this is my developer information
FIRST NAME:</code>DEVOUR</code>
LAST NAME :</code>DEVIL</code>
USERNAME  :@DEVOURDEVILS
GITHUB PRO:</b> <a href="github.com/kamarjahan">GITHUB </a>
WHO ASKED DEV INFO :{message.from_user.mention}"""

TGP_TEXT = """</code>SENT ME A PHOTO,VIDEO,GIF,OR ANY ANIMATION I WILL UPLOADNIT TO TELEGRAPH AND GIVE THE PERMENENT LINK</code>"""

ABOUT_TEXT = """
MY NAME:</code>TELEGRAPH BOT</code>
CREATOR:@DEVOURDEVILS
LIBRARY:</code>PYROGRAM</code>
LANGUAGE:</code>PYTHON 3</code>
DATABASE:</code>MONGO DB</code>
        :</code>redislabs</code>
BOT SERVER:</code>railway current</code>
BUILD STATUS:</code>V2.0.0 [edit]</code>"""

STATUS_INFO = """
TOTAL TIME:</code>500h</code>
TIME SPENT:</code>96H</code>
TIME LEFT.:</code>404H</code>(THEN IDLING)
BOT STATUS:</code>ACTIVE</code> SINCE 96H
TOTAL USER:</code>4529</code>
TOTAL CHAT:</code>567</code>
BANNEDUSER:</code>56</code>
GLOBAL BAN:</code>8</code>
BOT BANNED:</code>12</code>
BOT ADMINS:</code>452</code>
   (IDLING)"""


