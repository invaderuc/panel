$(function(){
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(getCoords, getError);
	}else{
		initialize(13.30272, -87,194107);
	}
	function getCoords(position)
	{
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat, lng);
	}

	function getError(err)
	{
		initialize(13.30272, -87,194107);
	}
	      function initialize() {
        var mapOptions = {
          center: new google.maps.LatLng(-34.397, 150.644),
          zoom: 8,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById("map_canvas"),
            mapOptions);
      }
});