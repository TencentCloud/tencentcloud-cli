**Example 1: 获取诊断事件列表**



Input: 

```
tccli dbbrain DescribeDBDiagEvents --cli-unfold-argument  \
    --StartTime 2021-05-27T00:00:00+00:00 \
    --EndTime 2021-05-27T01:00:00+00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "7a9a6ba0-5893-11ec-8ad2-ff04c623cbd9",
        "TotalCount": 1,
        "Items": [
            {
                "InstanceId": "cdb-test",
                "EventId": 330858512,
                "StartTime": "2021-05-27 00:01:10",
                "EndTime": "2021-05-27 00:01:20",
                "DiagItem": "事务未提交",
                "DiagType": "事务未提交",
                "Severity": 1,
                "Outline": "存在未提交事务",
                "Metric": "",
                "Region": "ap-guangzhou"
            }
        ]
    }
}
```

