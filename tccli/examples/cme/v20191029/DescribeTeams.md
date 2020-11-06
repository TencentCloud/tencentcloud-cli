**Example 1: 获取团队信息**



Input: 

```
tccli cme DescribeTeams --cli-unfold-argument  \
    --Platform test \
    --TeamIds 1kdk882ddd88338ddd3k3 1kdk882ddd88338ddd3k4
```

Output: 
```
{
    "Response": {
        "TeamSet": [
            {
                "TeamId": "1kdk882ddd88338ddd3k3",
                "Name": "工作室1",
                "MemberCount": 30,
                "CreateTime": "",
                "UpdateTime": ""
            },
            {
                "TeamId": "1kdk882ddd88338ddd3k4",
                "Name": "工作室2",
                "MemberCount": 10,
                "CreateTime": "",
                "UpdateTime": ""
            }
        ],
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

