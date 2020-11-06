**Example 1: 更新设备影子**



Input: 

```
tccli iotcloud UpdateDeviceShadow --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceName abc \
    --State {"desired":{"color":"red"}} \
    --ShadowVersion 1
```

Output: 
```
{
    "Response": {
        "Data": "{\"payload\":{\"state\": {\"desired\": { \"color\": \"red\"}}, \"metadata\": {\"desired\": {\"color\": {\"timestamp\": 1509092895971}}}, \"timestamp\": 1509443636326, \"version\": 5},\"result\":0,\"timestamp\":1509440846582,\"type\":\"update\"}",
        "RequestId": "9e574269-093f-4a7f-bf90-24ef80b6528a"
    }
}
```

