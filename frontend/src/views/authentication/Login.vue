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

			<hr />
			<div class="other-links text-center">
				<span>Not having an account?</span> <br>
				<router-link class="other-links-a" to="user/account/signup" tag="a">signup</router-link> <br>

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
div.auth-form {
	--width-of-form: 400px;
}

@media screen and (max-width: 399px){
	div.auth-form {
		--width-of-form: 92vw;
	}
}

div.auth-form {
	background-color: var(--dark-shade-1);
	color: whitesmoke;
	width: var(--width-of-form);
	padding: 1em;
	margin: 5em 0;
	border-radius: 0.5em;
	position: relative;
	left: 50%;
	transform: translate(-50%, 0);
	font-family: var(--navigation-font-family);
}

.auth-form h1.heading {
	text-align: center;
	color: white;
	text-transform: uppercase;
	font-weight: 800;
}

.g-hr {
	border: 1px solid white;
}

.auth-form form label {
	font-size: 1.2rem;
	font-weight: bold;
	color: var(--accent-color-1);
}

.auth-form .text-input {
	padding: 0.5em;
	font-size: 1.1rem;
	width: calc(var(--width-of-form) - 2em);
	letter-spacing: 2px;
}

.auth-form .text-input:focus {
	border: none;
}

button.form-btn {
	border: none;
	padding: 0.4em 0.8em;
	margin: 0.4em 0;
	font-size: 1.4rem;
	font-weight: 800;
	width: calc(var(--width-of-form) - 1.60em);
	background-color: green;
	color: white;
}

.auth-form .social-accounts-links {
	font-size: 1.2rem;
	margin: 0.3em;
}

.auth-form .social-accounts-links a {
	text-decoration: none;
	margin: 0 0.3em;
	font-size: 1.2rem;
	font-weight: bold;
}

.social-accounts-links a:hover {
	color: hotpink;
}

.other-links {
	font-size: 1.1rem;
	text-transform: lowercase;
}

.other-links-a {
	font-weight: bold;
}

.other-links-a:hover {
	text-decoration: none;
	color: hotpink;
}
</style> 