**Example 1: 查询项目列表**

查询项目列表

Input: 

```
tccli pts DescribeProjects --cli-unfold-argument  \
    --ProjectIds project-xx
```

Output: 
```
{
    "Response": {
        "ProjectSet": [
            {
                "AppId": 123,
                "Uin": "456",
                "SubAccountUin": "789",
                "CreatedAt": "2021-08-23T20:59:07+08:00",
                "UpdatedAt": "2021-08-23T20:59:07+08:00",
                "ProjectId": "project-ks8lr6m2",
                "Name": "MyProject",
                "Description": "Test project",
                "Tags": [
                    {
                        "TagKey": "owner",
                        "TagValue": "lyla"
                    }
                ],
                "Status": 1
            }
        ],
        "RequestId": "abc",
        "Total": 1
    }
}
```

