import speedtest
from tabulate import tabulate

def check():
        s = speedtest.Speedtest()
        s.get_servers()
        s.get_best_server()
        s.download()
        s.upload()
        res = s.results.dict()
        return res


checkconnect = check()
#tampilkan data
download = round(checkconnect["download"]/1000,2)
upload = round(checkconnect["upload"]/1000,2)
ping = round(checkconnect["ping"])
client = checkconnect["client"]["isp"]
country = checkconnect["client"]["country"]

print(' * Running Module: SpeedTest')

