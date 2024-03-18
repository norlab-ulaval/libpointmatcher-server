<template>
    <div>
        <h3>CSV Reader</h3>
        <br />
        <input type="file" id="csvFile" name="csvFile" @change="onLoadFile" />
    </div>
</template>

<script>
export default {
    name: 'CSVReader',
    methods: {
        onLoadFile(event) {
            let files = event.target.files || e.dataTransfer.files;
            this.$papa.parse(files[0], {
                header: true,
                complete: this.onComplete,
                skipEmptyLines: true,
            });
        },
        onComplete(results, file) {
            console.log("Parsed data:", results.data);
            this.$emit('csv-data', results.data);
        },
    }
};
</script>