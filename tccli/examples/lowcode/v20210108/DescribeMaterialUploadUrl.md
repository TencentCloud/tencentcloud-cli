**Example 1: 获取素材上传链接**



Input: 

```
tccli lowcode DescribeMaterialUploadUrl --cli-unfold-argument  \
    --EnvId abc \
    --Name abc \
    --ExpireDay 1
```

Output: 
```
{
    "Response": {
        "UploadUrl": "abc",
        "DownloadUrl": "abc",
        "Id": "abc",
        "RequestId": "abc"
    }
}
```

