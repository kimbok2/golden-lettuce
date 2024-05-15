// 회원가입 및 로그인
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useUserStore = defineStore(
  "user",
  () => {
    const name = ref(null);
    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);
    const isLogin = computed(() => {
      if (token.value === null) {
        return false;
      } else {
        return true;
      }
    });
    const router = useRouter();

    const signUp = function (payload) {
      // 1. 사용자 입력 데이터를 받아
      // const username = payload.username
      // const password1 = payload.password1
      // const password2 = payload.password2
      const { username, password1, password2 } = payload;

      // 2. axios로 django에 요청을 보냄
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          // username: username,
          // password1: password1,
          // password2: password2
          username,
          password1,
          password2,
        },
      })
        .then((response) => {
          console.log("회원가입 성공!");
          const password = password1;
          logIn({ username, password });
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const logIn = function (payload) {
      // 1. 사용자 입력 데이터를 받아
      const { username, password } = payload;
      // 2. axios로 django에 요청을 보냄
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username,
          password,
        },
      })
        .then((response) => {
          name.value = username;
          // console.log(response)
          // console.log(response.data.key)
          // 3. 로그인 성공 후 응답 받은 토큰을 저장
          token.value = response.data.key;
          router.push({ name: "home" });
        })
        .catch((error) => {
          console.log(error);
        });
    };

    const logOut = function () {
      console.log(token.value);
      axios({
        method: "post",
        url: `${API_URL}/accounts/logout/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          name.value = null;
          token.value = null; // 토큰 값 삭제
          router.push({ name: "login" }); // 로그인 페이지로 리다이렉션
        })
        .catch((err) => console.log(err));
    };

    return {
      API_URL,
      name,
      signUp,
      logIn,
      token,
      isLogin,
      logOut,
    };
  },
  { persist: true }
);
