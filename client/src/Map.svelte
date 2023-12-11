<script>
	import L from 'leaflet';
    let map;
    let files;

    // Build the map
    function createMap(container) {
        // Initialize the map
        map = L.map(container, {preferCanvas: true }).setView([51.505, -0.09], 13);
        // Add default tile layer
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        return map;
    }

    // Load data file
    function loadData(e) {
        // Process input file
        const fr = new FileReader();
        fr.onload = () => addLayer(fr.result)
        fr.onerror = () => console.log("Data failed")
        fr.readAsText(e['target']['files'][0]);
        console.log("Process initiated")
    }

    // Add loaded data to map
    function addLayer(data) {
        console.log("Data loaded")
        L.geoJSON(JSON.parse(data)).addTo(map)
    }

</script>

<div>
    <div class="map" use:createMap />
    <input type="file" on:input={(e) => loadData(e)} bind:files accept=".json,.geojson">
    {#if files && files[0]}
        <p>
            {files[0].name}
        </p>
    {/if}
</div>

<style>
	div {
		width: 100%;
		height: 400px;
	}
</style>