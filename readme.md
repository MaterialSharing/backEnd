# 英语学习助手

## 后端框架比较
- django是一个流行且容易入门的后端框架,我们选择django+DRF来搭建后端
## DRF常用部分参考
- [Request parsing](https://www.django-rest-framework.org/api-guide/requests/#request-parsing)

  REST framework's Request objects provide flexible request parsing that allows you to treat requests with JSON data or other media types in the same way that you would normally deal with form data.

  [.data](https://www.django-rest-framework.org/api-guide/requests/#data)

  - `request.data` returns the parsed content of the request body. 

    - This is similar to the standard `request.POST` and `request.FILES` attributes except that:

      - It includes all parsed content, including *file and non-file* inputs.

      - It supports parsing the content of HTTP methods other than `POST`, meaning that you can access the content of `PUT` and `PATCH` requests.

      - It supports REST framework's flexible request parsing, rather than just supporting **form data**. 
      - For example you can handle incoming [JSON data](https://www.django-rest-framework.org/api-guide/parsers/#jsonparser) similarly to how you handle incoming [form data](https://www.django-rest-framework.org/api-guide/parsers/#formparser).

    - For more details see the [parsers documentation](https://www.django-rest-framework.org/api-guide/parsers/).

  - [.query_params](https://www.django-rest-framework.org/api-guide/requests/#query_params)

    - `request.query_params` is a **more correctly named synonym** for `request.GET`.

    - For clarity inside your code, we recommend using `request.query_params` **instead of the Django's** standard `request.GET`. 
    - Doing so will help keep your codebase more correct and obvious - any HTTP method type may include query parameters, not just `GET` requests.

  - [.parsers](https://www.django-rest-framework.org/api-guide/requests/#parsers)

    - The `APIView` class or `@api_view` decorator will **ensure that** this property is **automatically set to a list of `Parser` instances**, based on the `parser_classes` set on the **view** or based on the `DEFAULT_PARSER_CLASSES` setting.

    - <u>You won't typically need to access this property.</u>





























