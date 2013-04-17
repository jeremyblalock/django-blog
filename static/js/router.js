define([
  'jquery',
  'underscore',
  'backbone',
  'views/posts/list',
  'views/posts/item'
], function($, _, Backbone, PostListView, PostItemView) {
  var AppRouter = Backbone.Router.extend({
    routes: {
      '': 'showPosts',
      'before/:id': 'showPosts',
      'posts/:slug': 'showSinglePost'
    }
  });

  var initialize = function() {
    var app_router = new AppRouter;
    app_router.on('route:showPosts', function() {
      var postListView = new PostListView();
    });

    app_router.on('route:showSinglePost', function(id) {
      alert("SINGLE POST, ID=" + id);
    });
    Backbone.history.start();
  }
  return {
    initialize: initialize
  }
});
