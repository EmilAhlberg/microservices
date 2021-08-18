import React, { useEffect, useState } from "react";
import MyChart from "./components/MyChart.js";

import "./App.css";

function App() {
  const [state, setState] = useState([]);
  useEffect(() => {
    fetch("http://localhost:9100/gameData").then(res => {
      res
        .json()
        .then(result => setState(result))
        .catch(err => console.log(err));
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <MyChart data={state} />
      </header>
    </div>
  );
}

export default App;
