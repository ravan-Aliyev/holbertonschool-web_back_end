/* eslint-disable */

export default function getListStudentIds(arr) {
  let array = [];

  if (arr instanceof Array) {
    array = arr.map((item) => item.id);
  }

  return array;
}
