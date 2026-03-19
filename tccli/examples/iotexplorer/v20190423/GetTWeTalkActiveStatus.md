**Example 1: 获取设备Talk激活状态**



Input: 

```
tccli iotexplorer GetTWeTalkActiveStatus --cli-unfold-argument  \
    --DeviceIds RNSEEMTZB0_dev
```

Output: 
```
{
    "Response": {
        "TalkActivationRecords": [
            {
                "DeviceId": "RNSEEMTZB0_dev",
                "ExpireTime": 11270477496,
                "ServiceType": 1
            }
        ],
        "RequestId": "882fdadf-e56a-465a-8a6d-2ecea4137f3c"
    }
}
```

