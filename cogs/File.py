import nextcord
import ast
from nextcord.ext import commands


class File(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def writefile(self, user_id, writedata):
      with open(f"database/{user_id}.txt","w+") as data_write:
          data_write.write(str(writedata))

    def readfile(self, user_id):
      with open(f"database/{user_id}.txt","r") as data_read:
          d=ast.literal_eval(data_read.read())
          return d



def setup(bot):
    bot.add_cog(File(bot))