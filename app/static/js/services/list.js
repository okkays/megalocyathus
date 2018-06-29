services.list = function(controller) {

  var service = {};

  service.add_route = function(obj) {
    route = `/${controller}/${obj.id}`
    return $.extend({'route': route}, obj);
  }

  // Users of this service should override this.
  service.populate = function(list_data) {
    console.log(list_data);
  }

  service.init = function() {
    var list_promise = api(controller)();
    $('document').ready(function() {
      // Populate the list.
      list_promise.then(function(data) {
        var processed = data.map(service.add_route);
        console.log(`Loaded ${controller}: `, processed);
        service.populate(processed);
      });
    });
  }

  return service;
}
