**Example 1: 示例**



Input: 

```
tccli mqtt DescribeDeviceIdentityBackupHistory --cli-unfold-argument  \
    --InstanceId mqtt-mzj7aqxk \
    --Destination mqtt-******** \
    --DeviceId device-1 \
    --ModificationTimeStart 1782199046395 \
    --ModificationTimeEnd 1782199086395 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [],
        "RequestId": "19fd4d06-8370-4687-a5c4-ff109c9de86e"
    }
}
```

