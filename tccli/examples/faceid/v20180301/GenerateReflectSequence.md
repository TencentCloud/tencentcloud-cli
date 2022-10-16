**Example 1: 获取光线序列**



Input: 

```
tccli faceid GenerateReflectSequence --cli-unfold-argument  \
    --DeviceDataUrl https://faceid-resource-sg-1254418846.cos.ap-singapore.myqcloud.com/faceid%2FApplyWebVerificationToken%2F1300268875%2F20b11b59-572d-406d-8d94-e6e05782134c \
    --DeviceDataMd5 d41d8cd98f00b204e9800998ecf8427e
```

Output: 
```
{
    "Response": {
        "ReflectSequenceUrl": "https://faceid-resource-sg-1254418846.cos.ap-singapore.myqcloud.com",
        "ReflectSequenceMd5": "d41d8cd98f00b204e9800998ecf8427e",
        "RequestId": "32-323233-323"
    }
}
```

