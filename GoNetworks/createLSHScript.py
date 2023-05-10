from LSHEngine.ModelManager import LSHClientDB
from LSHEngine import LSHEngine
DB = LSHClientDB.Manager()
DB.create_db(["C:/Users/Matteo/Desktop/DEVELOP/Current/DocFlow/workspace/GoNetworks/NERModel/raw.csv"])
Instance = LSHEngine.Engine()
Instance.GO()
Instance.include_custom_manager(DB)
Instance.save_model_to_bin("C:/Users/Matteo/Desktop/DEVELOP/Current/DocFlow/workspace/GoNetworks/NERModel/baseapp.bin")
print("Saved Model")

#Import Engine Class
#from LSHEngine import LSHEngine
#Create an instance of the Engine Class
#EngineInstance = LSHEngine.Engine()
#Start Engine
#EngineInstance.GO()
#Load Database into Engine
#EngineInstance.load("workspace/GoNetworks/NERModel/baseapp.bin")
#EngineInstance.define_current_scope(["value"])
#for i in range(1):
#    i = 24
#    EngineInstance.perms = i
#    EngineInstance.train_forest()
#    rec = EngineInstance.recommendations("ATHLETHEN STRASSE 123, 48469 GERMANY", as_df=False)
#    print(i)
#    print(rec)
#    print(rec[rec["jaccard_value"] > 0.3].iloc[0]["text"])
#if rec[rec["jaccard_value"] > 0.3].iloc[0]["group"] == "Company":
#    print("Whuuuu")