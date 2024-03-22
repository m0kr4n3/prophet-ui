from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
import pandas as pd
from prophet import Prophet
import os, random
from flask_cors import cross_origin

class Forecast(Resource):
    """Create forcasts
    ---
    post:
      tags:
        - api
      summary: Create a forcast from an uploaded csv
      description: Create a forcast with prophet model from an uploaded csv and number of days, then return [ds, y_hat, y_upper, y_lower]
      responses:
        200:
          content:
            application/json:
    """
    #method_decorators = [jwt_required()]
    @cross_origin([])
    def post(self):
        uploaded_csv = request.files['files']
        if uploaded_csv == None:
            return {"msg": "Upload your file"}, 200
        rand_numb = str(random.randint(1, 10 ** 15))
        path = f"uploads/{hex(int(rand_numb))[2:]}.csv"
        filename = os.path.join(os.getcwd(), path)

        if uploaded_csv.filename != '':
            uploaded_csv.save(filename)
        
        model = Prophet()
        df = pd.read_csv(filename)
        model.fit(df)

        future = model.make_future_dataframe(periods=int(request.args['nb_days']))

        forecast = model.predict(future)
        
        dic = {
          "ds": [],
          "yhat": [],
          "yhat_lower": [],
          "yhat_upper": []
        }

        for i in forecast.values.tolist():
          dic["ds"].append(str(i[0]).split(' ')[0])
          dic["yhat"].append(i[1])
          dic["yhat_lower"].append(i[2])
          dic["yhat_upper"].append(i[3])

        return {"data": dic}, 200