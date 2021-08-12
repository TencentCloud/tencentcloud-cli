**Example 1: 获取访问日志导出列表**



Input: 

```
tccli waf DescribeAccessExports --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226
```

Output: 
```
{
    "Response": {
        "Exports": [
            {
                "ExportId": "export-61daca5c-f341-4796-aeb3-4f2f598a06c7",
                "Query": "*",
                "FileName": "log_100005604621_1ae37c76-df99-4e2b-998c-20f39eba6226_20210713_export-61daca5c-f341-4796-aeb3-4f2f598a06c7_1626174454.tar.gz",
                "FileSize": 279519,
                "Order": "desc",
                "Format": "json",
                "Count": 6221,
                "Status": "Completed",
                "From": 1625395948532,
                "To": 1626000748532,
                "CosPath": "https://export-cd-1254077820.cos.ap-chengdu.myqcloud.com/%2Fexport%2F20210713%2Flog_100005604621_1ae37c76-df99-4e2b-998c-20f39eba6226_20210713_export-61daca5c-f341-4796-aeb3-4f2f598a06c7_1626174454.tar.gz?q-sign-algorithm=sha1&q-ak=xxx&q-sign-time=1626175178%3B1626178778&q-key-time=1626175178%3B1626178778&q-header-list=host&q-url-param-list=&q-signature=ebb37d76834b5be4ff0c8bfa263d88d1adf5685d",
                "CreateTime": "2021-07-13 19:07:15"
            }
        ],
        "TotalCount": 1,
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

