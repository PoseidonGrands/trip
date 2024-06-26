## 轮播图接口

### 请求地址
/system/slide_list

### 请求方式
GET

### 请求参数
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
            <td>type</td>
            <td>int</td>
            <td>true</td>
            <td>轮播图所属模块（10：首页）</td>
        </tr>
    </tbody>
</table>

### 响应格式
```
{
    "meta": {},
    "objects": [
        {
            "id": 1,
            "name": "1",
            "img_url": "/static/home/banner/banner1.jpg",
            "target_url": "#"
        },
        {
            "id": 2,
            "name": "2",
            "img_url": "/static/home/banner/banner2.jpg",
            "target_url": "#"
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
            <td>img_url</td>
            <td>String</td>
            <td>图片地址</td>
        </tr>
        <tr>
            <td>target_url</td>
            <td>String</td>
            <td>目标地址</td>
        </tr>
    </tbody>
</table>