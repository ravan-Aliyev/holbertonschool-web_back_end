/* eslint-disable */

import { uploadPhoto, createUser } from "./utils";

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((val) => {
      const [photo, user] = val;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => console.log("Signup system offline"));
}
