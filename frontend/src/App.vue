<template>
	<div>
		<!-- Load router view-->
		<router-view></router-view>
	</div>
</template>


<script>

export default {
	name: "App",
	data() {
		return {

		}
	},
	components: {

	}
}


</script>

/** Global styles */
<style>
/* @import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600;1,700;1,800&display=swap'); */

@font-face {
	font-family: Monserrat;
	src: url("/assets/fonts/Monserrat/Monserrat-Bold.ttf"),
		url("/assets/fonts/Monserrat/Monserrat-Regular.ttf"),
}
@font-face {
	font-family: "Open Sans";
	src: url("/assets/fonts/Open_Sans/OpenSans-Bold.ttf"),
		url("/assets/fonts/Open_Sans/OpenSans-Regular.ttf")
}
@font-face {
	font-family: Lato;
	src: url("/assets/fonts/Lato/Lato-Bold.ttf"),
		url("/assets/fonts/Lato/Lato-Bold.ttf"),
}

*{
	margin: 0;
	padding: 0;
	text-decoration: none;
	list-style: none;
}

:root {
	--navbar-height: 100px;
	--mobile-nav-width: 100%;
	--accent-color-1: #ffaa00;
	--accent-color-2: #e89b00;
	--dark-shade-1: #000000b9;
	--feature-box-height: 200px;
	--navigation-font-family: "Lato", sans-serif;
	--body-font-family: "Open Sans";
	--heading-font-family: "Monserrat";
}
</style>

<style scoped>

</style>