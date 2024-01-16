**Example 1: 获取共享单元列表**



Input: 

```
tccli organization DescribeShareUnits --cli-unfold-argument  \
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
                "Area": "ap-guangzhou",
                "CreateTime": "2021-03-05 15:29:14",
                "Description": "share unit",
                "Name": "myShareUnit",
                "OwnerUin": 1111111111,
                "ShareMemberNum": 0,
                "ShareResourceNum": 0,
                "Uin": 2222222222,
                "UnitId": "shareUnit-xhre**ra2p"
            }
        ],
        "RequestId": "7e6a64bc-6522-4c33-b3c3-303570691d7b",
        "Total": 1
    }
}
```

