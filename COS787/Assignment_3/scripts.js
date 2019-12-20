// loading spatial data
mongoimport <path to restaurants.json> -c restaurants
mongoimport <path to neighborhoods.json> -c neighborhood
// indexing
db.restaurants.createIndex({ location: "2dsphere" })
// Loading spatial data
// Indexing
// Basic selections
// Finding features in a given bounding box
// Intersections
// Selecting features based on their distance from another feature
// Any additional queries possible or JavaScript libraries