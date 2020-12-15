<template>
    <div id="features">
        <div class="features-heading-box text-center">
            <h1>Features</h1>
            <p>Sample features waiting for you to use to create a better goal setting experience</p>
        </div>

        <div class="container-fluid">
            <div class="row justify-content-center">
                <div class="col-lg-3 col-md-5 col-10 text-center feature-box" v-for="feature in features" :key="feature.title">
                    <div class="feature-icon-box">
                        <font-awesome-icon :icon="feature.icon">
                    </font-awesome-icon></div>
                    <h5>{{ feature.title }}</h5>
                    <p>{{ feature.description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
export default {
    name: "FeatureList",
    data() {
        return {
            features: [
                {icon: "chart-line", title: "Feature 1", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 2", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 3", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 4", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 5", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 6", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 7", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 8", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},
                {icon: "chart-line", title: "Feature 9", description: "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad, delectus dolorum? Adipisci voluptatem quas mollitia minus quo, quasi laboriosam expedita"},            
            ]
        }
    }
}
</script>


<style scoped>
div#features {
    margin-top: 3em;
    font-family: var(--body-font-family);
}

.features-heading-box h1 {
    font-weight: 600;
    font-size: 4rem;
    font-family: var(--heading-font-family);
}

@media screen and (max-width: 500px){
    div#features {
        margin-top: 2em;
    }
    .features-heading-box h1 {
        font-weight: 600;
        font-size: 3rem;
    }
}

.features-heading-box p {
    font-weight: 300;
    font-size: 1.6rem;
}

.feature-box {
    margin: 1.5em 1.5em;
    border-radius: 2em 2em 0 0;
    box-shadow: inset 0 -3em 3em rgba(0,0,0,0.1), 
                0 0  0 2px rgb(255,255,255),
                0.6em 0.8em 0.4em rgba(0,0,0,0.3);
}

.feature-box h5 {
    font-size: 2rem;
    font-weight: 600;
}

.feature-box p {
    font-size: 1.3rem;
    font-weight: 300;
    padding: 0;
    text-align: left;
}

.feature-icon-box {
    width: 100%;
    height: var(--feature-box-height);
    font-size: 10rem;
    line-height: var(--feature-box-height);
}

</style>