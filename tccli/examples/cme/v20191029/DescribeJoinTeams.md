**Example 1: 获取用户所加入的团队列表**



Input: 

```
tccli cme DescribeJoinTeams --cli-unfold-argument  \
    --Platform test \
    --MemberId 1993939392iidkei8ei
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "TeamSet": [
            {
                "TeamId": "1kdk882ddd88338ddd3k3",
                "Name": "工作室1",
                "MemberCount": 30,
                "Role": "Admin"
            },
            {
                "TeamId": "1kdk882ddd88338ddd3k4",
                "Name": "工作室2",
                "MemberCount": 10,
                "Role": "Member"
            }
        ],
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

