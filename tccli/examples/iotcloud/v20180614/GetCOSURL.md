**Example 1: 获取固件下载地址示例**



Input: 

```
tccli iotcloud GetCOSURL --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --FirmwareVersion 2.0.0 \
    --Filesize 1000
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

