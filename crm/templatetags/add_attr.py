from django.template import Library
from django.urls import reverse
from django.http import QueryDict

register = Library()

@register.filter(is_safe=True)
def label_with_classes(value, arg):
    """
    为模板form表单增加class属性
    :param value:
    :param arg:
    :return:
    """
    return value.label_tag(attrs={'class': arg})

@register.filter(is_safe=True)
def label_with_style(value, arg):
    """
    为模板form表单增加style属性
    :param value:
    :param arg:
    :return:
    """
    return value.label_tag(attrs={'style': arg})

@register.filter()
def widget_with_classes(value, arg):
    return value.as_widget(attrs={'class': arg})
# @register.simple_tag
# def memory_url(request, name, *args, **kwargs):
#     """
#     生成URL（含条件）
#     :return:
#     """
#     # /crm/depart/edit/45/?_filter=page=5&age=1
#     base_url = reverse(name, args=args, kwargs=kwargs)
#     if not request.GET:
#         return base_url
#     new_query_dict = QueryDict(mutable=True)
#     new_query_dict['_filter'] = request.GET.urlencode()  # _filter=pagesdf5sdfagesdfsdf1
#     url = "%s?%s" % (base_url, new_query_dict.urlencode(),)
#     return url
