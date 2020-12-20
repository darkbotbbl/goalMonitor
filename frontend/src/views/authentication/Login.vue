<template>
	<div>
		<div class="auth-form">
			<h1 class="heading">Login</h1>
			<hr class="g-hr"/>
			<form method="POST">
				<div class="form-group">
					<label for="login-email">Email: </label>
					<input type="email" name="email" id="login-email" class="text-input" aria-describedby="login-email-help"/>
					<!-- <small id="login-email-help" class="text-muted">Help text</small> -->
				</div>

				<div class="form-group">
					<label for="login-password">Password: </label>
					<input type="password" name="password" id="login-password" class="text-input" aria-describedby="login-password-help"/>
					<!-- <small id="login-password-help" class="text-muted">Help text</small> -->
				</div>
				
				<button class="form-btn" type="submit">Login</button>
			</form>

			<div class="social-accounts-links text-center">
				or login with: <br> 
				<a href="#">Google</a> |
				<a href="#">LinkedIn</a>
			</div>

			<hr class="g-hr-2"/>
			<div class="other-links text-center">
				<span>Not having an account?</span> <br>
				<router-link class="other-links-a" to="/user/account/signup" tag="a">signup</router-link> <br>

				<span>Forgot your password?</span> <br>
				<router-link class="other-links-a" to="#" tag="a">reset password</router-link> <br>
			</div>
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

</style> 