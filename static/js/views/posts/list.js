define([
  'jquery',
  'underscore',
  'backbone',
  'collections/posts',
  'views/posts/item'
], function($, _, Backbone, PostCollection, PostItemView) {
  var PostListView = Backbone.View.extend({
    el: $('#main'),

    initialize: function() {
      var self = this;
      this.collection = new PostCollection();
      this.collection.fetch({
        success: function() {
          self.render();
        }
      });
    },
    render: function() {
      console.log("RENDERING");
      var self = this;
      console.log(this.collection, this.collection.models);
      _.each(this.collection.models, function(model) {        
        console.log("POST:", model);
        var postItemView = new PostItemView({model: model});
        self.$el.append(postItemView.render());
      });
    }
  });
  return PostListView;
});
