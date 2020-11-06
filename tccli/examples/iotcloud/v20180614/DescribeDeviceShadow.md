**Example 1: 获取设备影子**



Input: 

```
tccli iotcloud DescribeDeviceShadow --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName abc
```

Output: 
```
{
    "Response": {
        "Data": "{\"payload\":{\"state\": {\"reported\": { \"color\": \"red\"}}, \"metadata\": {\"reported\": {\"color\": {\"timestamp\": 1509092895971}}}, \"timestamp\": 1509443636326, \"version\": 5},\"result\":0,\"timestamp\":1509440846582,\"type\":\"get\"}",
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

