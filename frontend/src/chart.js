import React from "react";
import "./App.css";
import ReactApexChart from "react-apexcharts";

// eslint-disable-next-line
function Chart({data}) {
  const series = [
    {
      name: "yhat",
      data: data["yhat"],
    },
    {
      name: "yhat_lower",
      data: data["yhat_lower"],
    },
    {
      name: "yhat_upper",
      data: data["yhat_upper"],
    },
  ];
  const options = {
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    xaxis: {
      type: "datetime",
      categories: data["ds"],
    },
    tooltip: {
      x: {
        format: "yy-MM-dd",
      },
    },
    fill: {
      type: 'gradient',
      gradient: {
        shadeIntensity: 1,
        opacityFrom: 0,
        opacityTo: 0,
        stops: [0, 100]
      },
    }
  };

  return (
    <div className="bg-white text-center">
      <br />
      <h1 className='text-center mb-4 text-base font-bold' >Forcasting Result:</h1>
      <br />
      <div className="w-1/2 mx-auto border-blue-700 border-2 p-4 rounded-lg">
        <ReactApexChart
          options={options}
          series={series}
          type="area"
          height={350}
        />
      </div>
      <br />
    </div>
  );
}

export default Chart;