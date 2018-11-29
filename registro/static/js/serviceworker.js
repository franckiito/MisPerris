var CACHE_NAME = 'my-site-cache-v1';

var urlsToCache = [
    '../',
    '/static/css/bootstrap.css',
    '/static/css/all.css',
    '/static/css/estilo.css',
    '/media/fotos/Apolo.jpg',
    '/media/fotos/Duque.jpg',
    '/media/fotos/Tom.jpg',
    '/static/js/jquery-3.3.1.js',
    '/static/js/popper.js',
    '/static/js/bootstrap.js',
    '/static/js/jquery.validate.js',
    '/static/js/jquery.Rut.js',
    '/static/js/app.js',
];


self.addEventListener('install', function(event) {
// Perform install steps
	event.waitUntil(
		caches.open(CACHE_NAME)
			.then(function(cache) {
				console.log('Cache Abierto!');
				return cache.addAll(urlsToCache);
			})
	);
});

self.addEventListener('activate', function(event) {
  console.log('Finally active. Ready to start serving content!');  
});


self.addEventListener('fetch', function(event) {
event.respondWith(
      caches.match(event.request)
    .then(function(response) {
        // Cache hit - return response
      if (response) {
                  return response;
      }
      return fetch(event.request);
    })
);
});

/*
var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        '/base_layout'
      ]);
    })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/base_layout'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});

*/