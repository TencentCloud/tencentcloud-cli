**Example 1: 获取素材上传链接**



Input: 

```
tccli lowcode DescribeMaterialUploadUrl --cli-unfold-argument  \
    --ExpireDay 1 \
    --EnvId xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "DownloadUrl": "xx",
        "Id": "xx",
        "RequestId": "xx",
        "UploadUrl": "xx"
    }
}
```

