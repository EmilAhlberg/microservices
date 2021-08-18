import MultiSelect from "react-multi-select-component";
import "./MultiSelector.css";

const MultiSelector = ({ data, selectedGames, onSelectedGamesChange }) => {
  const updateSelectedGames = selectedOptions => {
    onSelectedGamesChange(selectedOptions.map(option => option.value));
  };

  return (
    <div>
      <h1>Select Fruits</h1>
      <MultiSelect
        className="MultiSelector"
        options={data.map(({ GameTitle }) => ({
          label: GameTitle,
          value: GameTitle
        }))}
        value={selectedGames.map(game => ({ label: game, value: game }))}
        onChange={updateSelectedGames}
        labelledBy="Select"
      />
    </div>
  );
};

export default MultiSelector;
