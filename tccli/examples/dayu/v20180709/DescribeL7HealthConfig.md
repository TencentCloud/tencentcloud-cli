**Example 1: Exporting layer-7 health check configuration**



Input: 

```
tccli dayu DescribeL7HealthConfig --cli-unfold-argument  \
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
                "Protocol": "http",
                "VirtualPort": 80,
                "Enable": 1,
                "Interval": 300,
                "KickNum": 2,
                "AliveNum": 2,
                "Method": "HEAD",
                "StatusCode": 15,
                "Url": "/index.php",
                "Status": 1
            }
        ]
    }
}
```

