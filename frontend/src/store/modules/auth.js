import axios from 'axios'

const state = {
    username: null,
}

const getters = {

}

const mutations = {
    SET_USER(state, username) {
        state.username = username
    }
}

const actions = {
    async Signup({dispatch}, form) {
        await axios.post("api/v1/rest-auth/registration/", form);
        let UserLoginForm = new FormData();
        UserLoginForm.append("username", form.username)
        UserLoginForm.append("password", form.password)
        await dispatch("Login", UserLoginForm)
    },
    async Login({commit}, UserLoginForm) {
        await axios.post("api/v1/rest-auth/login/", UserLoginForm)
        await commit("SET_USER", UserLoginForm.username)
    }
}


export default {
    state,
    getters,
    mutations,
    actions
}