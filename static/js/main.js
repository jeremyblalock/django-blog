require.config({
  paths: {
    underscore: 'lib/underscore-min',
    backbone: 'lib/backbone-min'
  },
  shim: {
    'backbone': {
        //These script dependencies should be loaded before loading
        //backbone.js
        deps: ['underscore', 'jquery'],
        //Once loaded, use the global 'Backbone' as the
        //module value.
        exports: 'Backbone'
    },
    'underscore': {
        exports: '_'
    }
  }
});

require([
  'app'
], function(App) {
  App.initialize();
});
