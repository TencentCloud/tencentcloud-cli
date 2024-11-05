**Example 1: 获取素材列表**

获取素材列表

Input: 

```
tccli lowcode DescribeMaterialInfoList --cli-unfold-argument  \
    --Name abc \
    --Tags abc \
    --EnvId abc \
    --MediaType abc \
    --PageSize 1 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "List": {
            "Name": "abc",
            "DownloadUrl": "abc",
            "IsPublic": true,
            "UpdateTime": "2020-09-22 00:00:00",
            "Tags": "abc",
            "MediaType": "abc",
            "Size": "abc",
            "ExpireTime": "2020-09-22 00:00:00",
            "Id": 1,
            "CreateTime": "2020-09-22 00:00:00",
            "Owner": "abc"
        },
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

