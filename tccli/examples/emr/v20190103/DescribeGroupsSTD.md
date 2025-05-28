**Example 1: 查询用户组信息**



Input: 

```
tccli emr DescribeGroupsSTD --cli-unfold-argument  \
    --InstanceId emr-mzkssfla
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": "2025-05-14 21:46:04",
                "GroupName": "test2",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": []
            },
            {
                "CreateTime": "2025-05-14 21:46:04",
                "GroupName": "group2",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": []
            },
            {
                "CreateTime": "2025-05-14 15:39:50",
                "GroupName": "jianpan-1",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a3"
                ]
            },
            {
                "CreateTime": "2025-05-14 15:39:50",
                "GroupName": "jianpan-test",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a4",
                    "a1"
                ]
            },
            {
                "CreateTime": "2025-05-14 13:59:11",
                "GroupName": "user4",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a3",
                    "a4"
                ]
            },
            {
                "CreateTime": "2025-05-14 13:59:11",
                "GroupName": "user3",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a3"
                ]
            },
            {
                "CreateTime": "2025-05-14 13:59:11",
                "GroupName": "user2",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a3"
                ]
            },
            {
                "CreateTime": "2025-05-14 13:58:47",
                "GroupName": "odinlli1",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": [
                    "a1"
                ]
            },
            {
                "CreateTime": "2025-05-14 13:58:47",
                "GroupName": "odinlli4",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": []
            },
            {
                "CreateTime": "2025-05-14 13:58:47",
                "GroupName": "odinlli3",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": []
            },
            {
                "CreateTime": "2025-05-14 13:58:47",
                "GroupName": "odinlli2",
                "GroupType": 2,
                "GroupTypeDesc": "NormalUserGroup",
                "Users": []
            }
        ],
        "RequestId": "a7d952a8-7fe6-461c-b59c-9ae3d7d427d0",
        "TotalCount": 11
    }
}
```

