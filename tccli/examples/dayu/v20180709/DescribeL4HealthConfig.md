**Example 1: 导出四层健康检查配置**



Input: 

```
tccli dayu DescribeL4HealthConfig --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000xe \
    --RuleIdList rule-00000002
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "HealthConfig": [
            {
                "Protocol": "TCP",
                "VirtualPort": 666,
                "Enable": 1,
                "TimeOut": 30,
                "Interval": 300,
                "KickNum": 2,
                "AliveNum": 2,
                "KeepTime": 60
            }
        ]
    }
}
```

