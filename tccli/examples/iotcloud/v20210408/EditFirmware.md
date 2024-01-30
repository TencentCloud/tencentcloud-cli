**Example 1: 编辑固件信息**



Input: 

```
tccli iotcloud EditFirmware --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --FirmwareVersion 1.0.0 \
    --FirmwareName name \
    --FirmwareDescription desc \
    --FirmwareUserDefined '{\"key1\":\"value1\", \"key2\":\"支持中文\"}'
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

