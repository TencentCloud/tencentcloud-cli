**Example 1: 示例1**



Input: 

```
tccli mna GetDevicePayMode --cli-unfold-argument  \
    --DeviceIdList mna-test1 mna-test2 mna-test3
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "DeviceId": "mna-test1",
                "PayMode": 1,
                "PayModeDesc": "50G流量包",
                "ResourceId": "56d11777-50f7-4c60-9c89-e7076c8529a9-0"
            },
            {
                "DeviceId": "mna-test2",
                "PayMode": 1,
                "PayModeDesc": "20G流量包",
                "ResourceId": "56d11777-50f7-4c60-9c89-e7076c8529a9-0"
            },
            {
                "DeviceId": "mna-test3",
                "PayMode": 0,
                "PayModeDesc": "按流量后付费"
            }
        ],
        "RequestId": "1206563f-f13f-4647-aaa8-37fa86954cc4-1"
    }
}
```

