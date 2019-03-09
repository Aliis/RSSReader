<template>
    <div>
        <v-container grid-list-lg>
            <v-layout row wrap>
                <v-flex xs12 v-if="errorMsg">
                    <v-card color="blue-grey darken-2">
                        <v-card-text  class="text">
                            <p>{{ errorMsg }}</p>
                        </v-card-text>
                        <v-card-actions class="buttons">
                            <div class="button-wrapper"><v-btn @click="getFeed" flat color="orange">Lae uuesti</v-btn></div>
                        </v-card-actions>
                    </v-card>
                </v-flex>
                <v-flex xs12 v-else v-for="value in feedItems.slice(0, feedCounter)">
                    <v-card color="blue-grey darken-2">
                        <v-card-title class="text">
                            <div class="headline">{{ value.title }}</div>
                        </v-card-title>
                        <v-card-text  class="text">
                            <p>{{ value.description }}</p>
                            {{ value.published_date}}
                        </v-card-text>
                        <v-card-actions class="buttons">
                            <div class="button-wrapper"><a :href="value.link" target="_blank"><v-btn
                                    flat color="orange">Vaata uudist täismahus</v-btn></a></div>
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data() {
            return {
                feedItems: [],
                feedCounter: 10,
                errorMsg: ''
            }
        },
        methods: {
            getFeed() {
                axios.get('http://localhost:5000/')
                    .then((res) => {
                        if (res.data === 500) {
                            this.errorMsg = 'Lehe laadimine ebaõnnestus. RSS-i server on hetkel maas.'
                        }
                        else {
                            this.errorMsg = ''
                            this.feedItems = res.data;
                        }
                    })
                    .catch((error) => {
                        this.errorMsg = 'Lehe laadimine ebaõnnestus. ' + error
                });
            },
            addFeed() {
                this.feedCounter += 10
            },
            infiniteScroll() {
                window.onscroll = () => {
                    let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;

                    if (bottomOfWindow) {
                        this.addFeed()
                    }
                };
            }
    },
    created() {
        this.getFeed();
    },
    mounted() {
        this.infiniteScroll();
    }
};
</script>
<style>
    .text {
        color: #ddd;
    }
    .button-wrapper {
        text-align: right;
        width: 100%;
    }
    .buttons {
        background: #455A70;
    }
</style>
