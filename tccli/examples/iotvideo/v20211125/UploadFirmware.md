**Example 1: 上传固件信息**



Input: 

```
tccli iotvideo UploadFirmware --cli-unfold-argument  \
    --Md5sum hfshfspodkoiwuidoiwjcuie \
    --FileSize 1024 \
    --FirmwareVersion 1.0.0 \
    --ProductID product
```

Output: 
```
{
    "Response": {
        "RequestId": "id"
    }
}
```

