**Example 1: 获取基础防护攻击状态**

无

Input: 

```
tccli antiddos DescribeBasicDeviceStatus --cli-unfold-argument  \
    --IpList 127.0.0.1
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
        "CLBData": [
            {
                "Key": "1.1.1.1",
                "Value": "1"
            }
        ],
        "RequestId": "8f7a9451-2372-4a88-a69d-9868b8991076"
    }
}
```

**Example 2: 获取基础防护状态**

获取基础防护状态

Input: 

```
tccli antiddos DescribeBasicDeviceStatus --cli-unfold-argument  \
    --IpList abc \
    --IdList abc \
    --FilterRegion 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "CLBData": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

