**Example 1: 请求任务接口**



Input: 

```
tccli ms RequestLocalTask --cli-unfold-argument  \
    --ClientId 20230602_03702020-0a90-4f46-8f20-XXXXXXXXX
```

Output: 
```
{
    "Response": {
        "Sid": "uuid",
        "SrcFileMd5": "8c7ef86c259abad33f213405a35a13c2",
        "SrcFileSize": 0,
        "SrcFileUrl": "https://srcfile.url.com/srcfile",
        "SrcFileType": "release",
        "SrcFileVersion": "enterprise",
        "EncryptParam": "release",
        "EncryptState": 0,
        "RequestId": "abc"
    }
}
```

