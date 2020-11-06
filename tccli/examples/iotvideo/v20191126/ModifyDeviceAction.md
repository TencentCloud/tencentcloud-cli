**Example 1: 修改设备物模型行为**



Input: 

```
tccli iotvideo ModifyDeviceAction --cli-unfold-argument  \
    --Tid xxx \
    --Wakeup true \
    --Branch Action.takePhoto.ctlVal \
    --Value 1 \
    --IsNum true
```

Output: 
```
{
    "Response": {
        "RequestId": "ae7e8d94-13c9-4b58-8d95-ffce1b06e666",
        "TaskId": "",
        "Data": "{\"error_code\":0}"
    }
}
```

