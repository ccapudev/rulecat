new Vue({
    el: '#mainapp',
    data: {
        ruleta: []
    },
    methods: {
        rodar(){
            axios({
                url: '/',
                method: 'get',
                params: {
                    spin: 1
                }
            }).then(rsp => {
                this.ruleta =rsp.data
            })
        }
    }
})