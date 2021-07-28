**Example 1: 获取基础防护攻击状态**



Input: 

```
tccli antiddos DescribeBasicDeviceStatus --cli-unfold-argument  \
    --IpList ‘1.1.1.1’
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "1.1.1.1",
                "Value": "1"
            }
        ],
        "RequestId": "8f7a9451-2372-4a88-a69d-9868b8991076"
    }
}
```

