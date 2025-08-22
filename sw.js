self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('fetch', (e) => {
  // Funciona offline (básico)
});
