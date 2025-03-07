**Example 1: 编辑固件信息**



Input: 

```
tccli iotcloud EditFirmware --cli-unfold-argument  \
    --ProductId EQPOKD5111 \
    --FirmwareVersion 1.0.0 \
    --FirmwareName name1 \
    --FirmwareDescription desc \
    --FirmwareUserDefined '{\"key1\":\"value1\", \"key2\":\"支持中文\"}'
```

Output: 
```
{
    "Response": {
        "RequestId": "ebea2fd8-0b8f-44b3-99ab-1b04fcfb6cbc"
    }
}
```

