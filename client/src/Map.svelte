<!--
    Svelte component for mapping using leaflet and data I/O through a Flask-based application with data push, pull, load, save, and other endpoints.

    Created by Tariq Shihadah, 2023
-->
<script>
	import L from 'leaflet';
    let map;
    let files;
    let dataURL;

    // Build the map
    function createMap(container) {
        // Initialize the map
        map = L.map(container, {preferCanvas: true }).setView([40, -94], 4);
        // Add default tile layer
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        }).addTo(map);

        return map;
    }

    // Load data file
    function loadDataFile(e) {
        // Process input file
        const fr = new FileReader();
        fr.onload = () => {
            const data = fr.result
            const name = e['target']['files'][0].name
            addLayer(JSON.parse(data))
            pushData_GeoJSON(data, name)
        }
        fr.onerror = () => console.log("Data failed")
        fr.readAsText(e['target']['files'][0]);
    }

    // Load data URL
    async function loadDataURL(e) {
        // Fetch from URL
        const res = await fetch(
            dataURL
        )
        const data = await res.json()
        addLayer(data)
    }

    // Push data to server
    async function pushData_GeoJSON(data, name = none) {
        const res = await fetch(
            './data/push/' + name,
            {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            }
        )
    }

    // Pull data from server memory
    async function pullData_Loaded(name) {
        // Retrieve from server
        const res = await fetch(
            './data/pull/' + name,
            {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({name: name})
            }
        )
        const data = await res.json()
        addLayer(data)
    }

    // Add loaded data to map
    function addLayer(data) {
        console.log("Data loaded")
        L.geoJSON(data).addTo(map)
    }

</script>

<div>
    <div class="map" use:createMap />
    <button type="button" on:click={(e) => pullData_Loaded("us-states.json")} >Add US States</button>
    <input type="url" placeholder="Input data URL" bind:value={dataURL} >
    <button type="button" on:click={(e) => loadDataURL(e)} >Load data</button>
    <input type="file" on:input={(e) => loadDataFile(e)} bind:files accept=".json,.geojson" >
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