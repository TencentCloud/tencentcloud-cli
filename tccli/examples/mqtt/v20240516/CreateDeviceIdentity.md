**Example 1: 示例**

示例

Input: 

```
tccli mqtt CreateDeviceIdentity --cli-unfold-argument  \
    --InstanceId mqtt-qzgaq8bk \
    --DeviceId device-2 \
    --Status 1 \
    --PrimaryKey pk1 \
    --SecondaryKey sk1 \
    --PropagatingProperties.0.Key key-1 \
    --PropagatingProperties.0.Value key-b
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "30a1df4f-1a90-4241-8f77-9e568f5d0149"
    }
}
```

