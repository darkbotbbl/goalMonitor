<template>
    <section id="hero-section">
        <b-container>
            <h1 class="hero-section-message">{{ heroMessage }}</h1>
            <p class="hero-section-subtext">{{ heroSubtext }}</p>

            <a href="#" class="cta-btn-hero">Get Started Now
                <span class=""><font-awesome-icon icon="sign-in-alt"></font-awesome-icon></span>
            </a>
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
        // TODO - continue from here, add this as tagline on the hero section
    }
}
</script>


<style scoped>
#hero-section {
    text-align: center;
    min-height: 500px;
    background-color: whitesmoke;
}

.hero-section-message {
    font-size: 3.2rem;
    padding-top: 0.8em;
    line-height: 1.2em;
    font-weight: 700;
    font-family: 'Open Sans', sans-serif;
}

.hero-section-subtext {
    font-size: 1.8rem;
    font-weight: 300;
    margin: 1em 0 2em 0;
}

.cta-btn-hero {
    text-decoration: none;
    padding: 1em;
    font-size: 1.4rem;
    font-weight: 500;
    color: black;
    border: 2px solid var(--accent-color-1);
    border-radius: 1.5em;
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