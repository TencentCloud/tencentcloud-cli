**Example 1: 获取固件下载地址**



Input: 

```
tccli iotvideo GetFirmwareURL --cli-unfold-argument  \
    --ProductID product \
    --FirmwareVersion 1.0.0
```

Output: 
```
{
    "Response": {
        "Url": "http://test.com/firmware",
        "RequestId": "id"
    }
}
```

