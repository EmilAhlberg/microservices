import { LineChart, Legend, Line, XAxis, YAxis } from "recharts";
import React, { useState } from "react";
import MultiSelector from "./MultiSelector.js";
import moment from "moment";

const tempColors = ["#A370A7", "#86468B", "#6A266F", "#4F0F53", "#340138"];

const formatData = data => {
  let filteredData = null;
};

const MyChart = ({ data }) => {
  let [selectedGames, setSelectedGames] = useState([]);

  data = data.slice(10);

  const formatXAxis = tickItem => {
    console.log("...", tickItem);
    return moment(tickItem).valueOf();
    //return new Date(tickItem).getDay();
  };
  console.log("top", selectedGames);
  let displayedData = data.filter(data =>
    selectedGames.includes(data.GameTitle)
  );
  //formatData(data);

  return (
    <React.Fragment>
      <MultiSelector
        data={data}
        selectedGames={selectedGames}
        onSelectedGamesChange={setSelectedGames}
      />
      <LineChart
        width={900}
        height={600}
        data={data}
        margin={{ top: 5, right: 20, bottom: 5, left: 0 }}
      >
        {displayedData.map((gameData, i) => {
          return (
            <Line
              dataKey="ListRank"
              stroke={tempColors[i]}
              dot={false}
              data={gameData.SteamData}
              name={gameData.GameTitle}
              key={`linechartfor${gameData.GameTitle}`}
            />
          );
        })}
        <Legend />
        <XAxis
          name="DD:HH"
          dataKey="Timestamp"
          tickFormatter={formatXAxis}
          tick={{ fontSize: 14 }}
          minTickGap={100}
          angle={-35}
          type="category"
          allowDuplicatedCategory={true}
        />
        <YAxis />
      </LineChart>
    </React.Fragment>
  );
};

export default MyChart;
