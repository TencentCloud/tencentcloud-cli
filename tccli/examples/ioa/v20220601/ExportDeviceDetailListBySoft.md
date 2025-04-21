**Example 1: 导出基于软件查看终端详情列表查询**



Input: 

```
tccli ioa ExportDeviceDetailListBySoft --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6815e756-432e-4b72-8cd8-64f10d84fe63",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/software-open-api/software/%E7%BB%88%E7%AB%AF%E8%AF%A6%E6%83%852022-11-10%2018%3A06%3A37.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1668074798%3B1668078398&q-key-time=1668074798%3B1668078398&q-header-list=host&q-url-param-list=&q-signature=a0f8514a40d357b786f35860e3275726b694a522"
        }
    }
}
```

