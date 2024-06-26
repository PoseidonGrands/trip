## 景点列表接口

### 请求地址
/sight/sight_list

### 请求方式
GET

### 请求参数
<table>
<thead>
    <tr>
        <th>字段</th>
        <th>类型</th>
        <th>是否必填</th>
        <th>说明</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>page_index</td>
        <td>int</td>
        <td>false</td>
        <td>第几页数据（默认第一页数据）</td>
    </tr>
    <tr>
        <td>is_valid</td>
        <td>int</td>
        <td>false</td>
        <td>是否查询有效的数据（默认为true</td>
    </tr>
    <tr>
        <td>is_hot</td>
        <td>int</td>
        <td>false</td>
        <td>是否查询热门景点的信息（默认为false，全部查询</td>
    </tr>
    <tr>
        <td>is_top</td>
        <td>int</td>
        <td>false</td>
        <td>是否查询精选景点的信息（默认为false，全部查询</td>
    </tr>
</tbody>
</table>

### 响应格式
```
{
    "meta": {
        "total_count": 3,
        "page_count": 2,
        "current_page": 1
    },
    "objects": [
        {
            "id": 1,
            "name": "1",
            "banner_img": "http://localhost:5173/1",
            "score": "1.0",
            "province": "1",
            "city": "1",
            "comment_count": 0
        },
        {
            "id": 2,
            "name": "2",
            "banner_img": "http://localhost:5173/2",
            "score": "2.0",
            "province": "2",
            "city": "2",
            "comment_count": 0
        }
    ]
}
```

### 响应参数说明
<table>
    <thead>
        <tr>
            <th>字段名</th>
            <th>类型</th>
            <th>说明</th>
        </tr>
    </thead>
        <tbody>
        <tr>
            <td>meta</td>
            <td></td>
            <td>元数据</td>
        </tr>
        <tr>
            <td>objects</td>
            <td></td>
            <td>轮播图对象，解释如下</td>
        </tr>
        <tr>
            <td>id</td>
            <td>int</td>
            <td>编号</td>
        </tr>
        <tr>
            <td>name</td>
            <td>String</td>
            <td>名称</td>
        </tr>
        <tr>
            <td>img</td>
            <td>String</td>
            <td>图片地址</td>
        </tr>
        <tr>
            <td>banner_img</td>
            <td>String</td>
            <td>大图地址地址</td>
        </tr>
        <tr>
            <td>score</td>
            <td>Float</td>
            <td>景点评分</td>
        </tr>
    <!-- TODO... -->
</table>