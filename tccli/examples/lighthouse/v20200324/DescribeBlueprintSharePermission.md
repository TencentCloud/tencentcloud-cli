**Example 1: 查询自定义镜像共享信息**



Input: 

```
tccli lighthouse DescribeBlueprintSharePermission --cli-unfold-argument  \
    --BlueprintId lhbp-fypya4jw
```

Output: 
```
{
    "Response": {
        "SharePermissionSet": [
            {
                "CreatedTime": "2021-07-27T03:44:15Z",
                "ImageId": "img-jxk9gnz6"
            }
        ],
        "RequestId": "9842d6d6-8f8d-42cf-a9ad-846a47a28456"
    }
}
```

