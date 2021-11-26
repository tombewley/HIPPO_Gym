import _pickle as cPickle

with open("App/Trials/episode_0_user_4a066d81-7ce0-4dd5-99c6-3a3099de8423", "rb") as f: log = cPickle.load(f)

print(log)