<template>
    <div>
        <h1>HOMEPAGE</h1>
        <p>Welcome to the Homepage</p>
    </div>
</template>

<script>
    import { mapActions } from "vuex";

    export default {
        data() {
            return {

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
