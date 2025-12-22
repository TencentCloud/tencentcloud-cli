**Example 1: 获取主机指标监控配置列表**



Input: 

```
tccli cls DescribeHostMetricConfigs --cli-unfold-argument  \
    --TopicId 46c21ba9-b6ea-45f1-8710-5ad92b978b7a \
    --Filters.0.Key name \
    --Filters.0.Values testxxx2
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "ConfigId": "b64d4365-0d37-4db0-a603-1412e8bb747c",
                "CreateTime": 1749800274,
                "HostMetricItems": [
                    {
                        "Type": "cpu"
                    },
                    {
                        "Type": "mem"
                    },
                    {
                        "Type": "net"
                    },
                    {
                        "Type": "disk"
                    },
                    {
                        "Type": "system"
                    }
                ],
                "Interval": 30000,
                "MachineGroupIds": [
                    "4ca1de67-785b-4a0e-96d9-9d12c5c3ad18"
                ],
                "Name": "testxxx2",
                "UpdateTime": 1749800274
            }
        ],
        "RequestId": "72ecd45e-a95a-4803-98c7-32217fd722db",
        "TotalCount": 1
    }
}
```

