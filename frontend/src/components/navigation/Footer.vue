<!-- The footer is not yet complete, the layout is not best as it
is not. When you use the bootstrap layout features, they tend to
show above the navigation you have set for mobile, that is, they 
show above it -->
<template>
    <footer id="footer">
        <div class="container-fluid content">
            <div class="row justify-content-center">
                <div class="col-lg-3 col-md-6 col-12">
                    <h4>Social Links</h4>
                    <div>
                        <ul>
                            <li><a href="#">Twitter <font-awesome-icon icon="twitter"></font-awesome-icon></a></li>
                            <li><a href="#">Product Hunt</a></li>
                            <li><a href="#">Email</a></li>
                            <li><a href="#">LinkedIn</a></li>
                            <li><a href="#">Facebook</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-3 col-md-6 col-12">
                    <h4>Useful Links</h4>
                    <div>
                        <ul>
                            <li><a href="#">Privacy Terms</a></li>
                            <li><a href="#">Terms of Service</a></li>
                            <li><a href="#">Terms and Agreement</a></li>
                            <li><a href="#">About</a></li>
                            <li><a href="#">Products</a></li>
                        </ul>
                    </div>
                </div>
                <div class="col-lg-3 col-md-12 col-12">
                    <h4>Subscribe to our email listing</h4>
                    <div>
                        <form>
                            <label for="email-listing-name" class="listing-label">Full Name</label>
                            <input type="text" name="email-listing-name" class="listing-field" />

                            <label for="email-listing-email" class="listing-label">Email</label>
                            <input type="email" name="email-listing-email" class="listing-field" />

                            <button class="listing-btn">Subscribe</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>


<script>
export default {
    name: "Footer",
    data() {
        return {

        }
    }
}
</script>


<style scoped>
#footer {
    background-color: rgba(0, 0, 0, 0.884);
    color: white;
    margin-top: 3em;
    padding: 0 0 4em 0;

}

.content {
    padding-top: 4em;
}

.content h4 {
    border-bottom: 3px solid var(--accent-color-2);
    padding-bottom: 4px;
}

.content div {
    margin-top: 1em;
}

.listing-field {
    width: 100%;
    border: none;
    height: 2.2em;
    margin-bottom: 0.5em;
    padding: 0.8em;
    letter-spacing: 0.1em;
}

.listing-btn:focus {
    outline: none;
}

.listing-field::placeholder {
    font-weight: bold;
}

.listing-btn {
    border: none;
    padding: 0.5em;
    color: black;
    font-size: 1.2em;
    font-weight: 600;
    background-color: #ffaa00;
    box-shadow: inset 0 0 0.1em 0.3em rgba(0, 0, 0, 0.3);
    width: 100%;
}

.listing-btn:focus {
    outline: none;
}

@media screen and (max-width: 767px){
    .content {
        padding-top: 1em;
    }
    .content:nth-child(1) {
        padding-top: 3em;
    }
}

</style>