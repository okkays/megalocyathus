(function() { // Hide from global scope.
  var services_list = services.list('services');

  function build_list_item(service) {
    var element = `<li>
      <p class="title">
        <a href="${service.route}">${service.name}</a>
      </p>
      <p class="description">${service.description}</p>
    </li>`
    return $(element)
  }

  services_list.populate = function(services) {
    $('ul#main').append(services.map(build_list_item));
  }

  services_list.init();
})()
