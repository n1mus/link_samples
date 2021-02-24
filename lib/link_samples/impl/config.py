from dotmap import DotMap

config = dict(

)

app = DotMap(config) # app globals

def reset():
    app.clear()
    app.update(config)


