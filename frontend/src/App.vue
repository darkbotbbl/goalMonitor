<template>
	<!-- TODO Move all these to it's own component and import it here -->

	<div>
		<!-- Navigation -->
		<g-main-navigation></g-main-navigation>

		<!-- Hero Section -->
		<g-hero-section></g-hero-section>

	</div>
</template>


<script>
import MainNavigation from "./components/navigation/MainNavigation"
import HeroSection from "./components/navigation/homepage/HeroSection"


export default {
	name: "App",
	data() {
		return {

		}
	},
	components: {
		gMainNavigation: MainNavigation,
		gHeroSection: HeroSection,
	}
}


</script>

/** Global styles */
<style>
@import url('https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Josefin+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500;1,600;1,700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,500;1,600;1,700;1,800;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,600;0,700;0,800;1,400;1,600;1,700;1,800&display=swap');


*{
	margin: 0;
	padding: 0;
	text-decoration: none;
	list-style: none;
}

:root {
	--navbar-height: 100px;
	--mobile-nav-width: 100%;
	--accent-color-1: #FC466B;
	--accent-color-2:  #f1859a;
}
</style>

<style scoped>

</style>