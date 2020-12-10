import axios from 'axios'

const state = {
    username: null,
}

const getters = {
    getUsername(state) {
        return state.username
    }
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
        UserLoginForm.append("password", form.password1)
        await dispatch("Login", UserLoginForm)
    },
    async Login({commit}, form) {
        console.log(form)
        let response = await axios.post("api/v1/rest-auth/login/", form)
        console.log(response)
        await commit("SET_USER", form.username)
        // make a call to the api to get user data and add it to the state
    }
}


export default {
    state,
    getters,
    mutations,
    actions
}