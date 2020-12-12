<template>
	<!-- TODO Move all these to it's own component and import it here -->

	<div>
		<!-- Navigation -->
		<g-main-navigation></g-main-navigation>
		<section>
			
		</section>

	</div>
</template>


<script>
import MainNavigation from "./components/navigation/MainNavigation"


export default {
	name: "App",
	data() {
		return {

		}
	},
	components: {
		gMainNavigation: MainNavigation
	}
}


</script>

/** Global styles */
<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');


*{
	margin: 0;
	padding: 0;
	text-decoration: none;
	list-style: none;
}

:root {
	--navbar-height: 70px;
	--mobile-nav-width: 100%;
}
</style>

<style scoped>

</style>