**Example 1: 导出按终端查看软件统计列表**



Input: 

```
tccli ioa ExportSoftwareCensusListByDevice --cli-unfold-argument  \
    --OsType 0 \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b9657bd5-a848-43a9-8849-d278f6cd5207",
        "Data": {
            "DownloadURL": "https://ioa-dev-1-1258344699.cos-internal.ap-guangzhou.tencentcos.cn/software-open-api/software/dIofzJMYuG-%E8%BD%AF%E4%BB%B6%E7%BB%9F%E8%AE%A1-%E6%8C%89%E7%BB%88%E7%AB%AF%E6%9F%A5%E7%9C%8B-2022-11-10%2018%3A20%3A58.csv?q-sign-algorithm=sha1&q-ak=AKIDf9PPAfv0qQs8BzXsxnNincCWbQzJNDo9&q-sign-time=1668075658%3B1668079258&q-key-time=1668075658%3B1668079258&q-header-list=host&q-url-param-list=&q-signature=0b9ae200de58c1be7c6bffbad9038246de43201e"
        }
    }
}
```

