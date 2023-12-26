**Example 1: 分页查询示例1**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2
```

Output: 
```
{
    "Response": {
        "Count": 6,
        "ProjectList": [
            {
                "AIEngine": "无",
                "Bucket": "100097-251006271",
                "Cover": "",
                "CreateUserId": "264334425865150000",
                "Description": "描述说明",
                "HasModifyAuth": true,
                "ProjectId": "100097",
                "ProjectName": "demo测试01",
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UserCount": 1
            },
            {
                "AIEngine": "无",
                "Bucket": "100096-251006271",
                "Cover": "",
                "CreateUserId": "264334425865150000",
                "Description": "描述说明",
                "HasModifyAuth": true,
                "ProjectId": "100096",
                "ProjectName": "demo测试02",
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UserCount": 1
            }
        ],
        "RequestId": "3de3cacf-1bd4-4460-837f-fb71448e2d66"
    }
}
```

**Example 2: 增加 projectType**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 1 \
    --ProjectType 1 \
    --PageSize 30
```

Output: 
```
{
    "Response": {
        "Count": 3,
        "ProjectList": [
            {
                "AIEngine": "0",
                "Auth": [
                    "DEL_USER",
                    "MARK",
                    "DOWNLOAD",
                    "AI_TRAIN",
                    "CREATE_PROJECT",
                    "UPDATE_PROJECT",
                    "GET_PROJECT",
                    "UPLOAD_DATA",
                    "AUDIT",
                    "SHARE",
                    "DEL_PROJECT",
                    "INVITE_USER",
                    "CONF_AUTH"
                ],
                "Bucket": "taop-1300054071-251010749",
                "CamPolicyId": 0,
                "Cover": "",
                "CreateTime": "",
                "CreateUserId": "0",
                "CreateUserInfo": {
                    "CreateTime": "",
                    "Department": "",
                    "Id": "",
                    "Mobile": "",
                    "Name": "",
                    "PlatName": "",
                    "Position": "",
                    "Role": 0,
                    "SubAccountUin": ""
                },
                "Description": "开发环境自测涛",
                "HasModifyAuth": false,
                "ProjectId": "100824",
                "ProjectName": "开发环境自测涛876339",
                "ProjectPath": "100824/",
                "ProjectType": 0,
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UseAi": 0,
                "UserCount": 0
            },
            {
                "AIEngine": "0",
                "Auth": [
                    "AI_TRAIN",
                    "CREATE_PROJECT",
                    "UPDATE_PROJECT",
                    "GET_PROJECT",
                    "DEL_USER",
                    "MARK",
                    "DOWNLOAD",
                    "DEL_PROJECT",
                    "INVITE_USER",
                    "CONF_AUTH",
                    "UPLOAD_DATA",
                    "AUDIT",
                    "SHARE"
                ],
                "Bucket": "taop-1300054071-251010749",
                "CamPolicyId": 0,
                "Cover": "",
                "CreateTime": "",
                "CreateUserId": "0",
                "CreateUserInfo": {
                    "CreateTime": "",
                    "Department": "",
                    "Id": "",
                    "Mobile": "",
                    "Name": "",
                    "PlatName": "",
                    "Position": "",
                    "Role": 0,
                    "SubAccountUin": ""
                },
                "Description": "开发环境自测涛",
                "HasModifyAuth": false,
                "ProjectId": "100823",
                "ProjectName": "开发环境自测涛23339",
                "ProjectPath": "100823/",
                "ProjectType": 0,
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UseAi": 0,
                "UserCount": 0
            },
            {
                "AIEngine": "0",
                "Auth": [
                    "UPDATE_PROJECT",
                    "GET_PROJECT",
                    "DEL_USER",
                    "MARK",
                    "DOWNLOAD",
                    "AI_TRAIN",
                    "CREATE_PROJECT",
                    "INVITE_USER",
                    "CONF_AUTH",
                    "UPLOAD_DATA",
                    "AUDIT",
                    "SHARE",
                    "DEL_PROJECT"
                ],
                "Bucket": "taop-1300054071-251010749",
                "CamPolicyId": 0,
                "Cover": "",
                "CreateTime": "",
                "CreateUserId": "0",
                "CreateUserInfo": {
                    "CreateTime": "",
                    "Department": "",
                    "Id": "",
                    "Mobile": "",
                    "Name": "",
                    "PlatName": "",
                    "Position": "",
                    "Role": 0,
                    "SubAccountUin": ""
                },
                "Description": "开发环境自测涛",
                "HasModifyAuth": false,
                "ProjectId": "100818",
                "ProjectName": "开发环境自测涛",
                "ProjectPath": "100818/",
                "ProjectType": 0,
                "SimpleImageUrl": "",
                "StudyCount": 0,
                "UseAi": 0,
                "UserCount": 0
            }
        ],
        "RequestId": "b74354b8-c0b1-412f-856d-ef76b8565977"
    }
}
```

**Example 3: 项目列表搜索**



Input: 

```
tccli taop ListProjects --cli-unfold-argument  \
    --PageNumber 4 \
    --ProjectType 0 \
    --PageSize 20 \
    --StudyCountOper -1
```

Output: 
```
{
    "Response": {
        "Count": 59,
        "ProjectList": [],
        "RequestId": "fcf1002e-dee5-4f80-bf79-74ab7171590b"
    }
}
```

