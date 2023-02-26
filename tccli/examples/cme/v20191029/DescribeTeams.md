**Example 1: 获取指定团队信息**



Input: 

```
tccli cme DescribeTeams --cli-unfold-argument  \
    --TeamIds 1kdk882ddd88338ddd3k4 1kdk882ddd88338ddd3k3 \
    --Platform test
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
                "CreateTime": "2020-03-09T02:35:21Z",
                "UpdateTime": "2020-07-06T04:55:21Z"
            },
            {
                "TeamId": "1kdk882ddd88338ddd3k4",
                "Name": "工作室2",
                "MemberCount": 10,
                "CreateTime": "2020-04-03T09:25:21Z",
                "UpdateTime": "2020-06-06T03:16:21Z"
            }
        ],
        "RequestId": "99004d9f-aeec-4817-bbe2-d3499f95a2bf"
    }
}
```

**Example 2: 分布获取团队信息**



Input: 

```
tccli cme DescribeTeams --cli-unfold-argument  \
    --Platform test \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TeamSet": [
            {
                "TeamId": "1kdk882ddd88338ddd3k3",
                "Name": "工作室1",
                "MemberCount": 30,
                "CreateTime": "2020-03-09T02:35:21Z",
                "UpdateTime": "2020-07-06T04:55:21Z"
            }
        ],
        "RequestId": "98534d9f-aeec-4817-bbe2-d3499f95a2af"
    }
}
```

