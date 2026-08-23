**Example 1: 查询镜像关联资产数**



Input: 

```
tccli csip DescribeImageAssociatedAssetCount --cli-unfold-argument  \
    --MemberId mem-12e1se11 \
    --Id 3390 \
    --PreviewId 1000
```

Output: 
```
{
    "Response": {
        "ImageCountList": [
            {
                "ContainerCount": 0,
                "HostCount": 2,
                "Id": 3390,
                "OwnerAccountName": "***-管理*",
                "OwnerAppId": 260000000,
                "OwnerUin": "70000*******"
            }
        ],
        "RequestId": "facd87e4-82e2-43e9-b231-0f042b89732c"
    }
}
```

