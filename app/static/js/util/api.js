/**
 * Use as:
 * api('services')('get')
 * api('services')('post', params={'key': 'value'}).then()
 */
function api(token, params={}, route='/__/api') {
  var allowed = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
  if (!token) return api('GET', params, route)
  if (allowed.includes(token.toUpperCase())) {
    let options = $.extend({'method': token}, params);
    return $.ajax(route, options);
  }
  return function(newToken, moreParams={}) {
    return api(newToken, $.extend({}, params, moreParams), route + '/' + token);
  }
}
