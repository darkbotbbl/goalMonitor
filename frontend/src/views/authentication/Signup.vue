<template>
	<div>
		<h1>Welcome to the Signup Page</h1>
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