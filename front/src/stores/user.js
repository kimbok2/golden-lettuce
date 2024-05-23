// 회원가입 및 로그인
import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useUserStore = defineStore(
  "user",
  () => {
    const name = ref(null);
    // 유저의 모든 정보를 담을 변수
    const userInfo = ref(null);
    const API_URL = "https://kgarrry.pythonanywhere.com";
    const token = ref(null);
    const userSearchMapInfo = ref([]);
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
      const { username, password1, password2, date_of_birth, nickname } =
        payload;

      console.log(date_of_birth);
      console.log(nickname);
      // 2. axios로 django에 요청을 보냄
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          password1,
          password2,
          date_of_birth: date_of_birth,
          nickname: nickname,
        },
      })
        .then((response) => {
          console.log("회원가입 성공!");
          const password = password1;
          logIn({ username, password });
        })
        .catch((error) => {
          console.log(error);
          if (error.response.data.username) {
            alert(error.response.data.username[0]);
          }
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
        .then((response) => {
          getUserInfo();
        })
        .catch((error) => {
          alert("아이디 혹은 비밀번호를 잘못 입력하셨습니다.");
          console.log(error);
        });
    };

    const logOut = function () {
      console.log(token.value);

      if (confirm("로그아웃 하시겠습니까?")) {
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
            userInfo.value = null;
            router.push({ name: "login" }); // 로그인 페이지로 리다이렉션
          })
          .catch((err) => console.log(err));
      }
    };

    const getUserInfo = function () {
      axios({
        method: "get",
        url: `${API_URL}/accounts/profile/${name.value}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((response) => {
          userInfo.value = response.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      API_URL,
      name,
      signUp,
      logIn,
      token,
      isLogin,
      logOut,
      userInfo,
      getUserInfo,
      userSearchMapInfo,
    };
  },
  { persist: true }
);
