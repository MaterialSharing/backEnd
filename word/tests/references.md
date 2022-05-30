resolve()¶
The resolve() function can be used for resolving URL paths to the corresponding view functions. It has the following signature:

resolve(path, urlconf=None)¶
path is the URL path you want to resolve. As with reverse(), you don’t need to worry about the urlconf parameter. The function returns a ResolverMatch object that allows you to access various metadata about the resolved URL.

If the URL does not resolve, the function raises a Resolver404 exception (a subclass of Http404) .

class ResolverMatch¶
func¶
The view function that would be used to serve the URL

args¶
The arguments that would be passed to the view function, as parsed from the URL.

kwargs¶
The keyword arguments that would be passed to the view function, as parsed from the URL.

url_name¶
The name of the URL pattern that matches the URL.

route¶
The route of the matching URL pattern.

For example, if path('users/<id>/', ...) is the matching pattern, route will contain 'users/<id>/'.

tried¶
New in Django 3.2.
The list of URL patterns tried before the URL either matched one or exhausted available patterns.

app_name¶
The application namespace for the URL pattern that matches the URL.

app_names¶
The list of individual namespace components in the full application namespace for the URL pattern that matches the URL. For example, if the app_name is 'foo:bar', then app_names will be ['foo', 'bar'].

namespace¶
The instance namespace for the URL pattern that matches the URL.

namespaces¶
The list of individual namespace components in the full instance namespace for the URL pattern that matches the URL. i.e., if the namespace is foo:bar, then namespaces will be ['foo', 'bar'].

view_name¶
The name of the view that matches the URL, including the namespace if there is one.