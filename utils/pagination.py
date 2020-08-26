__author__ = 'Administrator'
from django.utils.safestring import mark_safe


class Pagination(object):
    """
    current_page:当前的页面
    data_count:需要做分页处理的总条数
    per_page_count：每页显示条数
    pager_num:最多显示页码
    可以参考day58的项目
    """
    def __init__(self, current_page, data_count, per_page_count=1, pager_num=7):
        try:
            self.current_page = int(current_page)
        except Exception as e:
            self.current_page = 1
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.pager_num = pager_num

    @property
    def start(self):
        """
        开始页面数
        :return:
        """
        return (self.current_page - 1) * self.per_page_count

    @property
    def end(self):
        """
        结束页面数
        :return:
        """
        return self.current_page * self.per_page_count

    @property
    def total_count(self):
        """
        返回分页数
        :return:
        """
        v, y = divmod(self.data_count, self.per_page_count)
        if y:
            v += 1
        return v

    def page_str(self, base_url):
        """
        分页属性返回
        :param base_url:
        :return:
        """
        page_list = []

        if self.total_count < self.pager_num:
            start_index = 1
            end_index = self.total_count + 1
        else:
            if self.current_page <= (self.pager_num + 1) / 2:
                start_index = 1
                end_index = self.pager_num + 1
            else:
                start_index = self.current_page - (self.pager_num - 1) / 2
                end_index = self.current_page + (self.pager_num + 1) / 2
                if (self.current_page + (self.pager_num - 1) / 2) > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.pager_num + 1

        if self.current_page == 1:
            prev = '<li><a class="page" href="javascript:void(0);">上一页</a></li>'
        else:
            prev = '<li><a class="page" href="%s?p=%s">上一页</a></li>' % (base_url, self.current_page - 1,)
        page_list.append(prev)

        for i in range(int(start_index), int(end_index)):
            if i == self.current_page:
                temp = '<li class="active"><a class="page active" href="%s?p=%s">%s</a></li>' % (base_url, i, i)
            else:
                temp = '<li><a class="page" href="%s?p=%s">%s</a></li>' % (base_url, i, i)
            page_list.append(temp)

        if self.current_page == self.total_count:
            nex = '<li><a class="page" href="javascript:void(0);">下一页</a></li>'
        else:
            nex = '<li><a class="page" href="%s?p=%s">下一页</a></li>' % (base_url, self.current_page + 1,)
        page_list.append(nex)

        # jump = """
        # <input type='text'  /><a onclick='jumpTo(this, "%s?p=");'>GO</a>
        # <script>
        #     function jumpTo(ths,base){
        #         var val = ths.previousSibling.value;
        #         location.href = base + val;
        #     }
        # </script>
        # """ % (base_url,)
        #
        # page_list.append(jump)

        page_str = mark_safe("".join(page_list))

        return page_str