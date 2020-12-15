<template>
	<div>
		<nav id="top-navbar">
			<input type="checkbox" id="check" v-model="checkboxValue"/>

			<label class="logo">
				<span class="desktop-logo">
					<span class="logo-color-deep">goal</span><span class="logo-color-light">Monitor</span>
				</span>
				<span class="mobile-logo">
					<span class="logo-color-deep">g</span><span class="logo-color-light">M</span>
				</span>
			</label>
			
			<ul class="cta-nav">
				<li class="nav-cta-login-link">
					<a href="#" class="nav-cta-btn">Login</a>
				</li>

				<li>
					<a href="#" class="nav-cta-btn">Signup</a>
				</li>
			</ul>

			<label for="check" class="checkbtn" v-if="checkboxValue">
				<font-awesome-icon icon="times" />
			</label>
			<label for="check" class="checkbtn" v-else>
				<font-awesome-icon icon="bars" />
			</label>

			<ul class="main-nav">
				<li v-for="item in menu_items" :key="item.tile">
					<a href="#">
						<div class="m-icon" :style="{backgroundColor: item.color}">
							<font-awesome-icon :icon="item.icon" />
						</div> <span>{{ item.title }}</span>
					</a>
				</li>
				<li class="nav-cta-login-link">
					<a href="#" class="nav-cta-btn">Login</a>
				</li>
			</ul>
		</nav>
	</div>
</template>


<script>

export default {
    name: "MainNavigation",
	data() {
		return {
			menu_items: [
				{
					icon: "question-circle",
					color: "#358600",
					title: "How to Use"
				},
				{
					icon: "chart-line",
					color: "#570000",
					title: "Features",
					submenu: [
						{title: "Feature 1"},
						{title: "Feature 2"},
						{title: "Feature 3"},
					]
				},
				{
					icon: "money-bill-wave",
					color: "#305CC2",
					title: "Pricing",
				},
				{
					icon: "boxes",
					color: "#011638",
					title: "Products",
				},
				{
					icon: "users-cog",
					color: "#311847",
					title: "Free Trial"
				}
			],
			checkboxValue: false,
		}
	},
	components: {
		
	},
}

</script>


<style scoped>

nav#top-navbar {
	font-family: var(--navigation-font-family);
	height: var(--navbar-height);
	width: 100%;
	background-color: #000000;
}

/** site label */
nav label.logo{
	font-size: 1.5rem;
	font-weight: 900;
	line-height: var(--navbar-height);
	margin: 0 1.8em;
}

.logo-color-deep{
	color: var(--accent-color-1);
}
.logo-color-light{
	color: var(--accent-color-2)
}

nav label.logo .mobile-logo {
	display: none;
}

/** desktop navigation */
nav ul.main-nav {
	float: right;
}

nav  li {
	display: inline-block;
	line-height: var(--navbar-height);
	margin-right: 20px;
	cursor: pointer;
}
nav ul.main-nav li:nth-last-child(1) {
	margin-right: 0;
}

nav ul.main-nav li a {
	text-decoration: none;
	font-size: 1rem;
	font-weight: bold;
	color: white;
}

nav ul.main-nav li a:hover {
	border-bottom: 3px solid var(--accent-color-2);
	padding-bottom: 2px;
}

/** check button used to toggle */
label.checkbtn {
	font-size: 1.5rem;
	line-height: var(--navbar-height);
	float: right;
	margin-right: 1.8em;
	cursor: pointer;
	display: none;
	color: var(--accent-color-1);
}

#check {
	display: none;
}

/** Cta buttons - the login and signup on the navbar */
nav ul.cta-nav {
	float: right;
	margin-right: 1.8em;
}

nav ul.cta-nav li a {
	text-decoration: none;
	font-size: 1.2rem;
	font-weight: 500;
	color: black;
}

.nav-cta-btn {
	padding: 10px;
	background: var(--accent-color-1);
}

.nav-cta-btn:hover {
	background: var(--accent-color-2);
}

/** the icon box  on the mobile menu*/
.m-icon {
	display: none;
}

nav ul.main-nav li.nav-cta-login-link {
	display: none;
}


/**  Mobile nav */
@media screen and (max-width: 891px) {
	nav ul.main-nav li a:hover {
		border-bottom: none;
	}


	label.checkbtn {
		display: block;
	}

	nav label.logo {
		margin-left: 1.2em;
	}

	nav ul.cta-nav {
		float: right;
		margin-right: 0;
	}

	/** The box having the icons in it */
	.m-icon {
		display: inline;
	}

	.m-icon {
		border: 1px solid white;
		display: inline-block;
		height: 40px;
		width: 40px;
		font-size: 1.2rem;
		text-align: center;
		border-radius: 5px;
		margin-right: 0.4em;
	}

	/** Mobile Navigation */
	nav ul.main-nav {
		position: fixed;
		height: 100vh;
		width: 362px;
		background-color: #08090A;
		top: calc(var(--navbar-height));
		left: -100%;
		text-align: center;
		transition: all .1s;
		box-shadow: 0px 5px 2px 0  #b3b9b9;
		border-bottom-right-radius: 5px;
		border-bottom-left-radius: 5px;
		border-top: 4px inset var(--accent-color-2);
	}

	nav ul.main-nav li {
		display: block;
		line-height: 40px;
		margin:  0;
		text-align: left;
		width: 100%;
		padding: 20px 30px;
		cursor: pointer;
	}

	/** Do a slight rotation on hover */

	nav ul.main-nav li:hover {
		background: #474444;
	}

	nav ul.main-nav li a {
		font-size: 1.0rem;
		color: white;
	}

	nav ul.main-nav li a:hover {
		color: white;
	}

	/** Changes after the toggle has been clicked */
	#check:checked ~ ul.main-nav {
		left: calc((100% - var(--mobile-nav-width))/2);
	}

	#check:checked ~ label.checkbtn {
		color: red;
	}
}

/** breakpoint to change logo */
@media screen and (max-width: 460px){
	nav label.logo .mobile-logo {
		display: inline-block;
	}
	nav label.logo .desktop-logo {
		display: none;
	}
}

/** breakpoint for smaller screens  */
@media screen and (max-width: 362px){
	nav ul.cta-nav li.nav-cta-login-link {
		display: none;
	}

	nav ul.main-nav li.nav-cta-login-link {
		display: block;
	}

	nav ul.main-nav li.nav-cta-login-link a {
		color: black;
		padding: 0.6em;
		font-size: 1.3em;
	}

	nav ul.main-nav {
	
		width: var(--mobile-nav-width);
	}

	nav ul.main-nav li:nth-last-child(1):hover {
		background: none;
		cursor: default;
	}
}

</style>
