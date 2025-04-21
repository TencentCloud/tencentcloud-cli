**Example 1: 导出基于软件分类的软件列表**



Input: 

```
tccli ioa ExportSoftListBySoftCategory --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "3b916d06-c775-417f-a393-af61a08eff5f",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/software-open-api/software/%E8%BD%AF%E4%BB%B6%E7%BB%9F%E8%AE%A1-%E6%8C%89%E8%BD%AF%E4%BB%B6%E6%9F%A5%E7%9C%8B2022-11-10%2015%3A49%3A43.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1668066583%3B1668070183&q-key-time=1668066583%3B1668070183&q-header-list=host&q-url-param-list=&q-signature=ebcb8737aa1be56060c08f5e5cfb0d94e479c2ba"
        }
    }
}
```

