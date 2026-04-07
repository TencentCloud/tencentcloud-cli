**Example 1: 查询调度器参数信息**



Input: 

```
tccli tke DescribeClusterSchedulerPolicy --cli-unfold-argument  \
    --ClusterId cls-ncmx45jw
```

Output: 
```
{
    "Response": {
        "ClientConnection": {
            "Burst": 100,
            "QPS": 50
        },
        "HighPerformance": true,
        "Policy": "",
        "SchedulerPolicyConfig": [
            {
                "PluginConfigs": [
                    {
                        "Args": "eyJraW5kIjoiTm9kZVJlc291cmNlc0ZpdEFyZ3MiLCJhcGlWZXJzaW9uIjoia3ViZXNjaGVkdWxlci5jb25maWcuazhzLmlvL3YxIiwic2NvcmluZ1N0cmF0ZWd5Ijp7InR5cGUiOiJMZWFzdEFsbG9jYXRlZCIsInJlc291cmNlcyI6W3sibmFtZSI6ImNwdSIsIndlaWdodCI6MX0seyJuYW1lIjoibWVtb3J5Iiwid2VpZ2h0IjoxfV19fQ==",
                        "Name": "NodeResourcesFit"
                    }
                ],
                "PluginSet": {
                    "Disabled": [
                        {
                            "Name": "qGPU"
                        }
                    ],
                    "Enabled": [
                        {
                            "Name": "NodeResourcesFit",
                            "Weight": 1
                        }
                    ]
                },
                "SchedulerName": "default-scheduler"
            }
        ],
        "RequestId": "ba8878e9-05c5-450a-af5f-aff1a2ff4a44"
    }
}
```

