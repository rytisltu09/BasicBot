from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(name="kick", description="Kick a member from the server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f"{member} has been kicked from the server.")
        except Exception as e:
            await ctx.send(f"Failed to kick {member}. Error: {e}")
    
    @commands.hybrid_command(name="ban", description="Ban a member from the server.")
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member} has been banned from the server.")
        except Exception as e:
            await ctx.send(f"Failed to ban {member}. Error: {e}")
    
    @commands.hybrid_command(name="unban", description="Unban a member from the server.")
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")
            for ban_entry in banned_users:
                user = ban_entry.user
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f"{user} has been unbanned from the server.")
                    return
            await ctx.send(f"User {member} not found in the ban list.")
        except Exception as e:
            await ctx.send(f"Failed to unban {member}. Error: {e}")
    
    @commands.hybrid_command(name="timeout", description="Timeout a member for a specified duration.")
    @commands.has_permissions(moderate_members=True)
    async def timeout(self, ctx, member: commands.MemberConverter, duration: int, *, reason=None):
        try:
            await member.timeout(duration=duration, reason=reason)
            await ctx.send(f"{member} has been timed out for {duration} seconds.")
        except Exception as e:
            await ctx.send(f"Failed to timeout {member}. Error: {e}")
    

async def setup(bot):
    await bot.add_cog(Moderation(bot))