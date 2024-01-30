**Example 1: 批量更新固件示例**



Input: 

```
tccli iotcloud BatchUpdateFirmware --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --FirmwareVersion 2.0.0 \
    --FirmwareOriVersion 1.0.0 \
    --Type 7
```

Output: 
```
{
    "Response": {
        "TaskId": 123456,
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

