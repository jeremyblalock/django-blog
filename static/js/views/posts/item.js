define([
  'jquery',
  'underscore',
  'backbone',
], function($, _, Backbone) {

  var PostItemView = Backbone.View.extend({
    render: function() {
      template = _.template($('#postDetailTemplate').html());
      this.$el.html(template({post: this.model.toJSON()}));
      return this.$el;
    }
  });

  return PostItemView;

});
