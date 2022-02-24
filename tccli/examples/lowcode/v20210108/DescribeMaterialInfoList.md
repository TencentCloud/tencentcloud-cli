**Example 1: 获取素材列表**

获取素材列表

Input: 

```
tccli lowcode DescribeMaterialInfoList --cli-unfold-argument  \
    --EnvId xx \
    --PageNum 1 \
    --Name xx \
    --PageSize 1 \
    --Tags xx \
    --MediaType xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": {
            "ExpireTime": "2020-09-22 00:00:00",
            "UpdateTime": "2020-09-22 00:00:00",
            "Name": "xx",
            "Tags": "xx",
            "IsPublic": true,
            "MediaType": "xx",
            "CreateTime": "2020-09-22 00:00:00",
            "DownloadUrl": "xx",
            "Owner": "xx",
            "Id": 1,
            "Size": "xx"
        },
        "RequestId": "xx"
    }
}
```

