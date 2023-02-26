**Example 1: 分页拉取团队成员信息**



Input: 

```
tccli cme DescribeTeamMembers --cli-unfold-argument  \
    --Platform test \
    --TeamId 1kdk882ddd88338ddd3k3 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "MemberSet": [
            {
                "MemberId": "299addf39392iidkei38",
                "Remark": "主编辑李四",
                "Role": "Owner"
            },
            {
                "MemberId": "39a39a9b92iidkei9ab",
                "Remark": "主编辑李四",
                "Role": "Admin"
            },
            {
                "MemberId": "i9dlld9393d2iidkei89i0",
                "Remark": "主编辑李四",
                "Role": "Members"
            }
        ],
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

**Example 2: 拉取指定成员的信息**



Input: 

```
tccli cme DescribeTeamMembers --cli-unfold-argument  \
    --Platform test \
    --TeamId 1kdk882ddd88338ddd3k3 \
    --MemberIds 1993939392iidkei8ei
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MemberSet": [
            {
                "MemberId": "1993939392iidkei8ei",
                "Remark": "主编辑李四",
                "Role": "Members"
            }
        ],
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

