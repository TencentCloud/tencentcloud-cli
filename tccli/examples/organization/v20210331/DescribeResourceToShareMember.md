**Example 1: 获取与我共享的资源列表**



Input: 

```
tccli organization DescribeResourceToShareMember --cli-unfold-argument  \
    --Area guangzhou \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-03-06 17:11:30",
                "ProductResourceId": "sec***002",
                "Type": "secret",
                "UnitId": "shareUnit-xh***a2p",
                "UnitName": "my-shareunit",
                "ShareManagerUin": "1000001"
            }
        ],
        "RequestId": "34b1919e-ab09-4cc0-8f4b-b35f371c7c58",
        "Total": 1
    }
}
```

