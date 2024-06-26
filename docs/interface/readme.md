## trip接口文档
RESTful风格
* 200 请求成功
* 201 提交成功
* 400 参数错误
* 401 未登录
* 403 没有权限
* 404 页面未找到
* 500 服务器正忙

### 接口请求地址
1. 测试环境
http://...
2. 生产环境

### 请求头

<!-- TODO -->

### 错误代码及提示
```
{
    'error_code': '400',
    'error_msg': '该字段不能为空',
    'error_list': [
        'password': [
            '该字段不能为空'
        ]
    ]
}
```

### 分页
#### 分页请求参数
<table>
    <thead>
        <tr>
            <th>字段</th>
            <th>类型</th>
            <th>是否必选</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>page_index</td>
            <td>int</td>
            <td>false</td>
            <td>当前页（默认为第一页）</td>
        </tr>
    </tbody>
</table>

#### 分页响应参数
<table>
    <thead>
        <tr>
            <th>字段</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>meta</td>
            <td></td>
            <td>分页元数据，解释如下</td>
        </tr>
        <tr>
            <td>total_count</td>
            <td>int</td>
            <td>总共有多少数据</td>
        </tr>
        <tr>
            <td>page_count</td>
            <td>int</td>
            <td>总共有几页</td>
        </tr>
        <tr>
            <td>current_page</td>
            <td>int</td>
            <td>当前是第几页</td>
        </tr>
        <tr>
            <td>objects</td>
            <td></td>
            <td>分页对象</td>
        </tr>
    </tbody>
</table> 

## 接口列表
### 1.系统模块
* [1.1 轮播图接口](./system/slider_list.md)

### 2.景点模块
* [2.1 景点列表接口](./sight/sight_list.md)