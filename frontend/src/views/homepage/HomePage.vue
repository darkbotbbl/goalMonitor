<template>
	<!-- TODO Move all these to it's own component and import it here -->

	<div>   
		<!-- Hero Section -->
		<g-hero-section></g-hero-section>
		<!-- Feature List -->
		<g-feature-list></g-feature-list>
	</div>
</template>


<script>
import HeroSection from "../../components/navigation/homepage/HeroSection"
import FeatureList from "../../components/navigation/homepage/FeatureList"


export default {
	name: "App",
	data() {
		return {

		}
	},
	components: {
		gHeroSection: HeroSection,
		gFeatureList: FeatureList,
	}
}


</script>


<style scoped>

</style>