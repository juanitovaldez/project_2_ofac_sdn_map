window.onload = function() {
    L.mapquest.key = 'lYrP4vF3Uk5zgTiGGuEzQGwGIVDGuy24';
    var baseLayer = L.mapquest.tileLayer('hybrid');
    

    var map = L.mapquest.map('map', {
      center: L.latLng(0, 0),
      layers: baseLayer,
      zoom: 2
    });



var markers = L.markerClusterGroup();

    for (var i = 0; i < addressPoints.rows.length; i++) {
      var popup = '<b>Entity ID: </b>' + addressPoints.rows[i][0] +
              '<br/><b>Name: </b>' + addressPoints.rows[i][1] +
              '<br/><b>Type: </b>' + addressPoints.rows[i][2] +
              '<br/><b>Program: </b>' + addressPoints.rows[i][3] +
              '<br/><b>Latitude: </b>' + addressPoints.rows[i][4] +
              '<br/><b>Longitude: </b> ' + addressPoints.rows[i][5];              

      var addressPoint = addressPoints.rows[i];
      var title = addressPoint[0] + ': ' + addressPoint[1];
      var lat = addressPoint[4];
      var lng = addressPoint[5];
      //console.log(lat, lng, title);
      var marker = L.marker(new L.LatLng(lat, lng) , {
        title: title,
        icon: L.mapquest.icons.marker()
      
      });
      
      marker.bindPopup(popup);
      markers.addLayer(marker);

    };
    markers.addTo(map);

      var heatArray = [];

      for (var i = 0; i < addressPoints.rows.length; i++) {
        var location = addressPoints.rows[i];
    
        if (location) {
          heatArray.push([location[4], location[5]]);
        }
      }
    
     var heat = L.heatLayer(heatArray, {
        minOpacity: .75,
        maxZoom: 11,
        radius: 42,
        blur: 69
      }).addTo(map);

    };