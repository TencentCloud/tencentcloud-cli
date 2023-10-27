**Example 1: UploadFile**



Input: 

```
tccli cpp UploadFile --cli-unfold-argument  \
    --Base64 abc \
    --OriginFileName abc \
    --KeepActive True \
    --OriginalProxy abc \
    --Watermark True
```

Output: 
```
{
    "Response": {
        "FileId": "abc",
        "Filename": "abc",
        "OriginName": "abc",
        "Type": "abc",
        "Size": 0,
        "Context": "abc",
        "ContextKey": "abc",
        "Path": "abc",
        "Watermark": "abc",
        "OriginalProxy": "abc",
        "Ext": "abc",
        "ReadableSize": "abc",
        "Location": "abc",
        "Md5": "abc",
        "Sha1": "abc",
        "Algorithm": "abc",
        "State": "abc",
        "KeepActive": true,
        "ActiveExpireTime": "abc",
        "InactiveTime": "abc",
        "Metadata": "abc",
        "RequestId": "abc"
    }
}
```

