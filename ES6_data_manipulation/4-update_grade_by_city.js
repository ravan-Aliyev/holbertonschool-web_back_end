/* eslint-disable */

export default function updateStudentGradeByCity(arr, city, newGrades) {
  return arr
    .filter((item) => item.location == city)
    .map((item) => {
      const [int] = newGrades.filter((grade) => grade.studentId === item.id);
      return {
        ...item,
        grade: int !== undefined ? int.grade : "N/A",
      };
    });
}
