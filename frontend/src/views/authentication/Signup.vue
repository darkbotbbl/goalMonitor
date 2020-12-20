<template>
	<div>
		<div class="auth-form">
			<h1 class="heading">Signup</h1>
			<hr class="g-hr"/>
			<form method="POST">
				<div class="form-group">
					<label for="signup-email">Email: </label>
					<input type="email" name="email" id="signup-email" class="text-input" aria-describedby="signup-email-help"/>
					<!-- <small id="signup-email-help" class="text-muted">Help text</small> -->
				</div>

				<div class="form-group">
					<label for="signup-password">Password: </label>
					<input type="password" name="password" id="signup-password" class="text-input" aria-describedby="signup-password-help"/>
					<!-- <small id="signup-password-help" class="text-muted">Help text</small> -->
				</div>
				
				<button class="form-btn signup-btn" type="submit">Register</button>
			</form>

			<div class="social-accounts-links text-center">
				or signup with: <br> 
				<a href="#">Google</a> |
				<a href="#">LinkedIn</a>
			</div>

			<hr />
			<div class="other-links text-center">
				<span>Already having an account?</span> <br>
				<router-link class="other-links-a" to="/user/account/login" tag="a">login</router-link> <br>

				<span>Forgot your password?</span> <br>
				<router-link class="other-links-a" to="#" tag="a">reset password</router-link> <br>
			</div>
		</div>
	</div>
</template>


<script>
import { mapActions } from "vuex"

export default {
	name: "Signup",
	data() {
		return {
			form: {
				username: "",
				email: "",
				password1: "",
				password2: "",
			}
		}
	},
	methods: {
		...mapActions(["Signup"]),
		async signup() {
			try {
				await this.Signup(this.form)
				this.$router.push("/user/profile")
			} catch (error) {
				console.log(error)
			}
		}
	}
}
</script>


<style scoped>

.signup-btn {
	box-shadow: 0.2em 0.2em 0.3em rgba(0, 0, 0, 0.4),
				-0.2em 0.2em 0.3em rgba(0, 0, 0, 0.4);
}

</style> 