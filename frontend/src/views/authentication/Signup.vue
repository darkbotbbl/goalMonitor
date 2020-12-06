<template>
	<div>
		<h2>Signup</h2>
		<hr/>
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
				<label for="password1">Password:</label><br>
				<input type="password" name="password1" v-model="form.password1" />
			</div>
			<div>
				<label for="password2">Confirm Password:</label><br>
				<input type="password" name="password2" v-model="form.password2" />
			</div><br>
			<button type="submit">Signup</button>
		</form>
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

</style>