/* eslint-disable */

export default function cleanSet(set, startString) {
  let word = "";
  let i = 0;
  for (let item of set) {
    if (item[0] === startString[0] && item.startsWith(startString)) {
      i++;
      word += `${item.split(startString).join("")}`;
      if (i < set.size - 1) {
        word += "-";
      }
    }
  }

  return word;
}
