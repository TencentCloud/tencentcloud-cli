**Example 1: 上传固件信息示例**



Input: 

```
tccli iotcloud UploadFirmware --cli-unfold-argument  \
    --ProductID ABCDE12345 \
    --FirmwareVersion 1.0.0 \
    --Md5sum hfshfspodkoiwuidoiwjcuie \
    --FileSize 1024
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxxxxxxxxxxxxxxxxx"
    }
}
```

