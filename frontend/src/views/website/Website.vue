<template>
    <div>
        <!-- Main Navigation for Website -->
        <g-main-navigation></g-main-navigation>

        <router-view></router-view>

        <!-- Footer for Website -->
        <g-footer></g-footer>
    </div>

</template>


<script>
import MainNavigation from "../../components/navigation/MainNavigation"
import Footer from "../../components/navigation/Footer"

export default {
    data() {
        return {

        }
    },
    components: {
        gMainNavigation: MainNavigation,
        gFooter: Footer
    }
}
</script>


<style scoped>

</style>