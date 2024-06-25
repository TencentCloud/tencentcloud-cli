**Example 1: 成功示例**



Input: 

```
tccli iotexplorer DescribeFirmwareUpdateStatus --cli-unfold-argument  \
    --ProductId PR******ID \
    --DeviceName de***01
```

Output: 
```
{
    "Response": {
        "DstVersion": "1.0",
        "OriVersion": "1.4",
        "Percent": 100,
        "RequestId": "adcfghb",
        "Status": 6
    }
}
```

