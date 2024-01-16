**Example 1: 获取共享单元成员列表**



Input: 

```
tccli organization DescribeShareUnitMembers --cli-unfold-argument  \
    --UnitId shareUnit-xhre**ra2p \
    --Area ap-guangzhou \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-03-06 17:08:38",
                "ShareMemberUin": 333333333333
            }
        ],
        "RequestId": "dd22e981-ad22-4676-865b-2d2184bf879b",
        "Total": 1
    }
}
```

