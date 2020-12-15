<template>
    <section id="hero-section">
        <b-container>
            <h1 class="hero-section-message">{{ heroMessage }}</h1>
            <p class="hero-section-subtext">{{ heroSubtext }}</p>

            <a href="#" class="">
                <button class="cta-btn-hero">Get Started Now <font-awesome-icon icon="sign-in-alt"></font-awesome-icon></button>
            </a>
            <div style="padding-bottom: 5em"></div> <!-- This is a spacer -->
        </b-container>
    </section>
</template>


<script>
export default {
    name: "HeroSection",
    data() {
        return {
            hero_message: "Set long term goals, track your daily tasks, and visually see how they impact your Long Term Goals",
            hero_subtext: "Setting goals and checking tasks off your todo list is great, but won't you want to know how they affect your future goals? Let us help."
        }
    },
    computed: {
        heroMessage() {
            return this.hero_message
        },
        heroSubtext() {
            return this.hero_subtext
        }
    }
}
</script>


<style scoped>
#hero-section {
    text-align: center;
    min-height: fit-content;
    background-color: whitesmoke;
}

.hero-section-message {
    padding: 0;
    margin: 0;
    font-size: 3.5rem;
    font-weight: bold;
    font-family: var(--heading-font-family);
    padding: 1em 0 0 0;
    line-height: 1.1em;
    color: blue;
}

.hero-section-subtext {
    padding: 0;
    margin: 0;
    font-size: 1.7rem;
    font-weight: 200;
    font-family: var(--body-font-family);
    padding: 1em 0 1.2em 0;
}

.cta-btn-hero {
    text-decoration: none;
    padding: 1em;
    font-size: 1.4rem;
    font-weight: 600;
    color: black;
    border: 2px solid var(--accent-color-1);
    border-radius: 2em;
    background-color: white;
}

.cta-btn-hero:hover {
    background-color: black;
    color: white;
}

@media screen and (max-width: 600px){
    .hero-section-message {
        font-size: 2.5rem;
    }

    .hero-section-subtext {
        font-size: 1.3rem;
    }
}

</style>