**Example 1: 拉取账户所拥有的项目**



Input: 

```
tccli dcdb DescribeProjects --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Projects": [
            {
                "AppId": 0,
                "CreateTime": "0000-00-00 00:00:00",
                "CreatorUin": 0,
                "Info": "默认项目",
                "IsDefault": 1,
                "Name": "默认项目",
                "OwnerUin": 0,
                "ProjectId": 0,
                "SrcAppId": 0,
                "SrcPlat": "qcloud",
                "Status": 3
            },
            {
                "AppId": 1251966477,
                "CreateTime": "2019-09-17 15:47:05",
                "CreatorUin": 3374998458,
                "Info": "",
                "IsDefault": 0,
                "Name": "ryanforredis",
                "OwnerUin": 3374998458,
                "ProjectId": 1159121,
                "SrcAppId": 0,
                "SrcPlat": "qcloud",
                "Status": 0
            }
        ],
        "RequestId": "31666e3c-f5bf-4862-8876-68f81131eef1"
    }
}
```

