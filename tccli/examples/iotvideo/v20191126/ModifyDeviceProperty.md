**Example 1: 修改设备物模型属性**



Input: 

```
tccli iotvideo ModifyDeviceProperty --cli-unfold-argument  \
    --Tid ******** \
    --Wakeup true \
    --Branch ProWritable.presetPosSetting.setVal.pos1.x \
    --Value 10 \
    --IsNum true
```

Output: 
```
{
    "Response": {
        "RequestId": "78f033ec-3c5a-4141-bc3c-679c91666035"
    }
}
```

