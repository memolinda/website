from flask import Flask, render_template

app=Flask(__name__)

@app.route('/') #create a decorator for the home page

def home(): #content in the decorator
    return render_template("home.html")

@app.route('/about/') #create an about page

def about():
    return render_template("about.html")

@app.route('/plot/')

def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure, output_notebook, output_file, show


    start = datetime.datetime(2020,1,1)
    end = datetime.datetime(2020, 7, 1)
    type(data.DataReader(name="AAPL", data_source ="yahoo", start=start, end=end))

    df =data.DataReader(name="AAPL", data_source ="yahoo", start=start, end=end)
    def inc_dec(Close,Open):
        if Close > Open:
            value="increase"
        elif Close<Open:
            value="decrease"
        else:
            value="equal"
        return value

    df["Status"] =[inc_dec(c,o) for c, o in zip(df.Close, df.Open)]

    df["middle_point"]=(df.Close+df.Open)/2

    df["height"] = abs(df.Close-df.Open)

    p = figure(x_axis_type='datetime', width =1000, height=300, title="Candelstick chart Apple stockmarket", sizing_mode='scale_width')
    p.grid.grid_line_alpha=0.3

    hours_12 = 12*60*60*1000

    p.segment(df.index,df.High,df.index,df.Low, color="black")
    p.rect(df.index[df.Status=="increase"], df.middle_point[df.Status=="increase"],
           hours_12, df.height[df.Status=="increase"], fill_color="#3CB371", line_color="black")
    p.rect(df.index[df.Status=="decrease"], df.middle_point[df.Status=="decrease"],
           hours_12, df.height[df.Status=="decrease"], fill_color="#CD5C5C", line_color="black")

    from bokeh.embed import components

    scrip1, div1 = components(p) # two strings : script = javascript, div1 = html

    from bokeh.resources import CDN #CDN = content delivery method

    cdn_js = CDN.js_files
    cdn_css = CDN.css_files


if __name__=="__main__":
    app.run(debug=True)
