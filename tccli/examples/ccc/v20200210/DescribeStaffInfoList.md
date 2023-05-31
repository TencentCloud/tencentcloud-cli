**Example 1: 获取坐席列表示例**

获取坐席列表示例

Input: 

```
tccli ccc DescribeStaffInfoList --cli-unfold-argument  \
    --ModifiedTime 1590147606 \
    --PageSize 10 \
    --PageNumber 0 \
    --StaffMail “121223@qq.com” \
    --SdkAppId 1400000000
```

Output: 
```
{
    "Response": {
        "RequestId": "5ac74e13-ef15-41a6-9639-f1bc8c9896bd",
        "TotalCount": 602,
        "StaffList": [
            {
                "Name": "xiao",
                "Mail": "1000273@qq.com",
                "Phone": "008617636049517",
                "Nick": "测试3",
                "StaffNumber": "125",
                "SkillGroupList": [
                    {
                        "SkillGroupId": 53,
                        "SkillGroupName": "ALL-dingoding-测试",
                        "Priority": 3,
                        "Type": "ALL"
                    },
                    {
                        "SkillGroupId": 82,
                        "SkillGroupName": "uu",
                        "Priority": 1,
                        "Type": "IM"
                    }
                ],
                "LastModifyTimestamp": 1613988825
            }
        ]
    }
}
```

