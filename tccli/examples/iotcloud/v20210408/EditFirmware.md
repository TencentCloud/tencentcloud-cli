**Example 1: 编辑固件信息**



Input: 

```
tccli iotcloud EditFirmware --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --FirmwareVersion 1.0.0 \
    --FirmwareName name \
    --FirmwareDescription desc
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

