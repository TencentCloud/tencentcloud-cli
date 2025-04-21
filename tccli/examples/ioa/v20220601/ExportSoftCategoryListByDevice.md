**Example 1: 导出基于设备分组的软件分类列表**



Input: 

```
tccli ioa ExportSoftCategoryListByDevice --cli-unfold-argument  \
    --OsType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0d8287c1-8c27-439a-a4b7-df6a03d7e75c",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/software-open-api/software/%E8%BD%AF%E4%BB%B6%E7%BB%9F%E8%AE%A1-%E6%8C%89%E8%BD%AF%E4%BB%B6%E5%88%86%E7%B1%BB%E6%9F%A5%E7%9C%8B2022-11-10%2018%3A02%3A20.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1668074540%3B1668078140&q-key-time=1668074540%3B1668078140&q-header-list=host&q-url-param-list=&q-signature=293a0aa2b99c93bbe41cec1b2db5d65ed48993ee"
        }
    }
}
```

