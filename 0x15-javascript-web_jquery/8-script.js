$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, status) {
	if (status === 'success') {
	  for (let m in data.results) {
	    $('UL#list_movies').append('<li>' + data.results[m].title + '</li>');
	  }
	}
});
