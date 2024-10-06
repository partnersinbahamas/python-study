import datetime as dt, sys, os, platform

def getInfo():
    date = dt.datetime.now().date()
    time = dt.datetime.now().time()

    user_os = os.name
    user_platform = platform.system()
    project_path = sys.path

    info = dict(
      date=date,
      time=time,
      user_os=user_os,
      user_platform=user_platform,
      project_path=project_path
    )

    for key, value in info.items():
        print(key, value, sep=": ")
    
    return info
