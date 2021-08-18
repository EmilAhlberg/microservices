import React, { useEffect, useState } from "react";

const CheckBox = ({ gameTitle }) => {
  const [isChecked, setIsChecked] = useState(false);

  const handleOnChange = () => {
    setIsChecked(!isChecked);
  };

  return (
    <label key={`checkBox${gameTitle}`}>
      <input
        type="checkbox"
        name={gameTitle}
        checked={isChecked}
        onChange={handleOnChange}
      />
      <span style={{ color: "black" }}>{gameTitle}</span>
    </label>
  );
};

export default CheckBox;
