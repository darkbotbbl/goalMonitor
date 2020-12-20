<template>
	<div>
		<div class="auth-form">
			<h1 class="heading">Login</h1>
			<form method="POST">
				<label for="login-email">Email: </label>
				<input type="email" name="email" id="login-email" class="text-input" />

				<label for="login-password">Password: </label>
				<input type="password" name="password" id="login-password" class="text-input" />

				<button type="submit">Login</button>
			</form>

			<div class="social-accounts-links">
				<a href="#">Google</a>
				<a href="#">LinkedIn</a>
			</div>

			<span>Not having an account?</span>
			<router-link to="user/account/signup" tag="a">signup</router-link>

			<span>Forgot your password?</span>
			<router-link to="#" tag="a">reset password</router-link>
		</div>
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
div.auth-form {
	width: 280px;
	height: 400px;
	padding: 2em;
	border: 1px solid black;
	margin: 5em 0;
	background-color: blue;
	color: white;
	position: relative;
	align-self: center;
}

.text-input {
	border: none;
	padding: 0.5em;
	
}

</style> 