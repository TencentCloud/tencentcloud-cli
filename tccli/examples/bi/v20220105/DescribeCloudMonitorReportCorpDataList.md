**Example 1: 上报免费试用馆信息**

上报免费试用馆信息

Input: 

```
tccli bi DescribeCloudMonitorReportCorpDataList --cli-unfold-argument  \
    --UinList abc \
    --Date abc
```

Output: 
```
{
    "Response": {
        "Extra": "abc",
        "Msg": "abc",
        "Data": {
            "CorpStatisticDataList": [
                {
                    "Date": "abc",
                    "Uin": "abc",
                    "DatasourceNum": 0,
                    "TableNum": 0,
                    "PageNum": 0,
                    "TotalNum": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

