**Example 1: 获取告警短信配额**



Input: 

```
tccli monitor DescribeAlarmSmsQuota --cli-unfold-argument  \
    --Module monitor
```

Output: 
```
{
    "Response": {
        "QuotaList": [
            {
                "FreeLeft": 1000,
                "Name": "基础告警",
                "PurchaseLeft": 0,
                "Type": "basic",
                "Used": 0
            },
            {
                "FreeLeft": 1000,
                "Name": "云拨测告警",
                "PurchaseLeft": 0,
                "Type": "cloud_test",
                "Used": 0
            },
            {
                "FreeLeft": 1000,
                "Name": "自定义监控告警",
                "PurchaseLeft": 0,
                "Type": "custom",
                "Used": 0
            },
            {
                "FreeLeft": 1000,
                "Name": "自定义消息",
                "PurchaseLeft": 0,
                "Type": "custom_msg",
                "Used": 0
            }
        ],
        "RequestId": "4f0be406-3993-4249-8b3f-373c8d8a76d7",
        "Total": 1000,
        "Used": 0
    }
}
```

