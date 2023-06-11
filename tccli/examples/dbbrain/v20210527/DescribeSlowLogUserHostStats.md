**Example 1: 获取慢日志来源地址统计分布图**

获取慢日志来源地址统计分布图。

Input: 

```
tccli dbbrain DescribeSlowLogUserHostStats --cli-unfold-argument  \
    --Product mysql \
    --InstanceId cdb-c1nl9rpv \
    --StartTime 2020-09-21T00:00:00+00:00 \
    --EndTime 2020-09-22T00:00:00+00:00
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "UserTotalCount": 1,
        "RequestId": "e2a51350-8c9f-11eb-bc0f-c9f5ab88d057",
        "Items": [
            {
                "UserHost": "10.3.1.1",
                "Ratio": 50,
                "Count": 29
            },
            {
                "UserHost": "10.3.1.2",
                "Ratio": 50,
                "Count": 29
            }
        ],
        "UserNameItems": [
            {
                "UserName": "root",
                "Ratio": 100,
                "Count": 58
            }
        ]
    }
}
```

