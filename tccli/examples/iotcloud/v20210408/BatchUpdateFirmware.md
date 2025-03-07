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
        "TaskId": 11236,
        "RequestId": "0b77fcf9-d157-4b60-9a3d-541916b48c24"
    }
}
```

