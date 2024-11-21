**Example 1: 策略列表**



Input: 

```
tccli cwp DescribeBaselinePolicyList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "PolicyName": "专业版主机弱口令+旗舰版",
                "DetectInterval": 1,
                "DetectTime": "00:00:00",
                "IsEnabled": 1,
                "AssetType": 1,
                "RuleIds": [
                    50
                ],
                "HostIds": [
                    "044889f8-d6a2-4fc3-a8a8-c114b6f5266b",
                    "a0770b41-9697-4a1d-8150-b8fa247b6189",
                    "cc0e8a25-7169-4b5c-a929-2b4cccbfce10"
                ],
                "HostIps": [
                    "1.1.1.1"
                ],
                "PolicyId": 172,
                "RuleCount": 1,
                "ItemCount": 1,
                "HostCount": 3,
                "IsDefault": 0
            }
        ],
        "RequestId": "5c340825-dbc9-4410-a47f-75eab15769d7",
        "Total": 19
    }
}
```

