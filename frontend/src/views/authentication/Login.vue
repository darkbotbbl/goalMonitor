<template>
	<div>
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
import { mapActions } from "vuex"

export default {
	name: "Login",
	data() {
		return {
			form: {
				username: "",
				password: ""
			}
		}
	},
	methods: {
		...mapActions(["Login"]),
		async login() {
			try {
				await this.Login(this.form)
				this.$router.push("/user/profile")
			} catch (error) {
				console.log(error)
			}
		}
	}
}
</script>


<style scoped>

</style>