**Example 1: 接收上传到控制台的固件版本信息**



Input: 

```
tccli iotvideo UploadOtaVersion --cli-unfold-argument  \
    --ProductId 461708984329 \
    --OtaVersion 0.9.1 \
    --VersionUrl http://xx.xx.xx.xx \
    --FileSize 3456 \
    --Md5 c4ca4238a0b923820dcc509a6f75849 \
    --Operator test
```

Output: 
```
{
    "Response": {
        "RequestId": "9396ceb0-4abd-4b8a-b991-abff1131c334"
    }
}
```

