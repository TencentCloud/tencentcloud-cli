**Example 1: 示例**

示例

Input: 

```
tccli mqtt DescribeDeviceIdentities --cli-unfold-argument  \
    --InstanceId mqtt-25zezo7b
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "Data": [
            {
                "CreatedTime": 1741708800000,
                "DeviceId": "device-1",
                "InstanceId": "mqtt-25zezo7b",
                "PrimaryKey": "pk2",
                "SecondaryKey": "sk2",
                "Status": 2
            },
            {
                "CreatedTime": 1741708800000,
                "DeviceId": "device-2",
                "InstanceId": "mqtt-25zezo7b",
                "PrimaryKey": "pk",
                "SecondaryKey": "sk",
                "Status": 2
            }
        ],
        "RequestId": "bc9241dd-5fd3-4636-aa07-06eda06661a8"
    }
}
```

