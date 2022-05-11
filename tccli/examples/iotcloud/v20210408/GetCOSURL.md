**Example 1: 获取固件下载地址示例**



Input: 

```
tccli iotcloud GetCOSURL --cli-unfold-argument  \
    --ProductId ABCDE12345 \
    --FirmwareVersion 2.0.0
```

Output: 
```
{
    "Response": {
        "Url": "http://abc.com",
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

