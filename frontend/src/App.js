import React, { useState } from "react";
import Chart from './chart';
import FileUploadPage from './upload'
import { useEffect } from 'react';

function App() {
  const [data, setData] = useState();
  const [isSubmitted, setIsSubmitted] = useState(false);
  useEffect(() => {
    document.title = 'Prophet forecasting model interface';
  }, []);
    return (
      <div className="app">
        <FileUploadPage setIsSubmitted={setIsSubmitted} setData={setData} />
        { isSubmitted ? (
          <Chart data={data["data"]}/>
        ):(
          <p></p>
        )}
      </div>
    );

}

export default App;