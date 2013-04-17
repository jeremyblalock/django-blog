define([
  'jquery',
  'underscore',
  'backbone',
], function($, _, Backbone) {
  var PostModel = Backbone.Model.extend({
    defaults: {
      title: 'Loading...',
      body: '',
      slug: ''
    },
    url: '/api/posts'
  });

  return PostModel;
});
