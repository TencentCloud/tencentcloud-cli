**Example 1: 示例**

示例

Input: 

```
tccli mqtt ModifyDeviceIdentity --cli-unfold-argument  \
    --InstanceId mqtt-qzgaq8bk \
    --DeviceId device-1 \
    --PropagatingProperties.0.Key key1 \
    --PropagatingProperties.0.Value value1
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "dbe406c9-8d46-4b54-b12f-b58be26d0e96"
    }
}
```

