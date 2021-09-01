**Example 1: 获取游戏实例日志URL**

获取游戏实例日志URL

Input: 

```
tccli gse GetGameServerInstanceLogUrl --cli-unfold-argument  \
    --FleetId fleet-qp3g3ffn-rwh0v05d \
    --InstanceId ins-93lqcfq0 \
    --ServerIp 21.3.65.11 \
    --Offset 0 \
    --Size 10
```

Output: 
```
{
    "Response": {
        "HasNext": true,
        "Total": 11,
        "PresignedUrls": [
            "http://test/url-001",
            "http://test/url-002",
            "http://test/url-003"
        ],
        "RequestId": "xx"
    }
}
```

