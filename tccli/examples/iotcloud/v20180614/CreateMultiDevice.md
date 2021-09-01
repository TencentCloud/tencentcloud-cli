**Example 1: 创建多个设备**



Input: 

```
tccli iotcloud CreateMultiDevice --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --DeviceNames aaa bbb ccc
```

Output: 
```
{
    "Response": {
        "TaskId": "abcdedf123456789",
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

