<template>
    <div>
        <h1>Welcome to your profile</h1>
        <h3>Username: {{ getUsername }}</h3>
    </div>
</template>


<script>
import { mapGetters } from "vuex"

export default {
    name: "UserProfile",
    computed: {
        ...mapGetters({
            getUsername: "getUsername"
        })
    }
}
</script>


<style scoped>
h1{
    color: green;
}
</style>