**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeDeviceIdentity --cli-unfold-argument  \
    --InstanceId mqtt-25zezo7b \
    --DeviceId device-1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "CreatedTime": 1741708800000,
        "DeviceId": "device-1",
        "InstanceId": "mqtt-25zezo7b",
        "PrimaryKey": "bcc0d6cae2a51e79723ce5e88547e214",
        "RequestId": "c6a780ce-7850-41de-8be6-41e073cc6668",
        "SecondaryKey": "sk1",
        "Status": 1
    }
}
```

