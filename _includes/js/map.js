window.conference.map = (() => {
    let config;
    let lang;

    let map;

    const setup = (elId) => {
        map = L.map(elId).setView([57.69438, 11.98510], 15);

        // L.tileLayer.provider(config.map_provider).addTo(map);
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap'
        }).addTo(map);

        // var marker = L.marker([57.69438, 11.98510]).addTo(map);

        var circle = L.circle([57.69438, 11.98510], {
            color: '#0f4c87',
            fillColor: '#0f4c87',
            fillOpacity: 0.5,
            radius: 75
        }).addTo(map);


        L.easyButton('far fa-star', () => {
            map.flyTo([57.69438, 11.98510], 15);
        }, lang.focus_conf).addTo(map);

        L.control.locate({
            flyTo: true,
            strings: {
                title: lang.focus_me
            }
        }).addTo(map);
    };

    const init = (c, l) => {
        config = c;
        lang = l;

        const elId = 'map';

        if (document.getElementById(elId)) {
            setup(elId);
        }
    };

    const getMap = () => {
        return map
    };

    return {
        init: init,
        getMap: getMap
    };
})();
