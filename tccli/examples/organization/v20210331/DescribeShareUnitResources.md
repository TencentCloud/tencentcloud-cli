**Example 1: 获取共享单元资源列表**



Input: 

```
tccli organization DescribeShareUnitResources --cli-unfold-argument  \
    --Offset 0 \
    --Area ap-guangzhou \
    --Limit 10 \
    --UnitId shareUnit-xhre**ra2p
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-03-06 17:11:30",
                "ResourceId": "shareUnit-12**erte",
                "ProductResourceId": "sec***002",
                "Type": "secret",
                "SharedMemberNum": 2,
                "SharedMemberUseNum": 0,
                "ShareManagerUin": 111111111111
            }
        ],
        "RequestId": "538e6bb8-704d-4594-b297-95bd2535ecc0",
        "Total": 1
    }
}
```

