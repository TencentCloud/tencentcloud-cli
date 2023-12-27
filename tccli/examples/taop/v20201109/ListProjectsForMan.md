**Example 1: 示例**



Input: 

```
tccli taop ListProjectsForMan --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "ProjectList": [
            {
                "AIEngine": "",
                "Auth": [
                    "UPDATE_PROJECT",
                    "GET_PROJECT",
                    "INVITE_USER",
                    "AI_TRAIN",
                    "UPLOAD_DATA",
                    "MARK",
                    "AUDIT",
                    "DOWNLOAD",
                    "CREATE_PROJECT",
                    "DEL_PROJECT",
                    "DEL_USER",
                    "CONF_AUTH",
                    "SHARE"
                ],
                "Bucket": "",
                "CamPolicyId": 0,
                "Cover": "",
                "CreateTime": "2021-06-23 21:10:18",
                "CreateUserId": "0",
                "CreateUserInfo": {
                    "CreateTime": "",
                    "Department": "传染科",
                    "Id": 123445,
                    "Mobile": "1xxxxxxx",
                    "Name": "sanzhang",
                    "PlatName": "张三",
                    "Position": "医生",
                    "Role": 4,
                    "SubAccountUin": "200000122000"
                },
                "Description": "",
                "HasModifyAuth": false,
                "ProjectId": "100700",
                "ProjectName": "主账户创建的项目",
                "ProjectPath": "这里是描述",
                "ProjectType": 0,
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UseAi": 0,
                "UserCount": 0
            }
        ],
        "RequestId": "9be731a4-a7ec-4ac3-934e-21d7a3a68025"
    }
}
```

