<template>
    <div>
        <h1>HOMEPAGE</h1>
        <hr />
        <h2>Signup</h2>
        <form @submit.prevent="signup">
            <div>
                <label for="username">Username:</label><br>
                <input type="text" name="username" v-model="form.username" />
            </div>
            <div>
                <label for="email">Email:</label><br>
                <input type="email" name="email" v-model="form.email" />
            </div>
            <div>
                <label for="password">Password:</label><br>
                <input type="password" name="password" v-model="form.password" />
            </div>
            <div>
                <label for="password_confirm">Confirm Password:</label><br>
                <input type="password" name="password_confirm" v-model="form.confirm_password" />
            </div><br>
            <button type="submit">Signup</button>
        </form>

        <hr />

        <h2>Login</h2>
        <form @submit.prevent="login">
            <div>
                <label for="username">Username:</label><br>
                <input type="text" name="username" v-model="form.username" />
            </div>
            <div>
                <label for="password">Password:</label><br>
                <input type="password" name="password" v-model="form.password" />
            </div><br>
            <button type="submit">Login</button>
        </form>
    </div>
</template>

<script>
    import { mapActions } from "vuex";

    export default {
        data() {
            return {
                form: {
                    username: '',
                    email: '',
                    password: '',
                    password_confirm: '',
                }
            }
        },
        methods: {
            ...mapActions([
                "Signup",
                "Login",
            ]),
            async signup() {
                try {
                    await this.Signup(this.form)
                    this.$router.push("/goal/daily")
                } catch (error) {
                    console.log(error)
                }
            },
            async login() {
                try {
                    await this.Login(this.form) 
                    this.$router.push("/goal/daily")
                } catch (error) {
                    console.log(error)
                }
            }
        }
    }
</script>

<style scoped>

</style>
