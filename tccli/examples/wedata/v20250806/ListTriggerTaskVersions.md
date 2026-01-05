**Example 1: 成功**

查询调度任务版本列表成功

Input: 

```
tccli wedata ListTriggerTaskVersions --cli-unfold-argument  \
    --ProjectId 1470547050521227264 \
    --TaskId 20240703211658628
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-25 09:58:12",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250925095812224",
                    "VersionNum": "V16",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-25 09:56:23",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250925095622525",
                    "VersionNum": "V15",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-25 09:54:41",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250925095441384",
                    "VersionNum": "V14",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-25 09:54:24",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250925095423555",
                    "VersionNum": "V13",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-25 09:50:08",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250925095007521",
                    "VersionNum": "V12",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-24 09:48:09",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250924094809238",
                    "VersionNum": "V11",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-23 16:52:42",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250923165241990",
                    "VersionNum": "V10",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-23 16:39:41",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250923163941260",
                    "VersionNum": "V9",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-23 16:00:51",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250923160051416",
                    "VersionNum": "V8",
                    "VersionRemark": ""
                },
                {
                    "ApproveStatus": null,
                    "ApproveUserUin": null,
                    "CreateTime": "2025-09-23 15:59:34",
                    "CreateUserUin": "100043952936",
                    "Status": null,
                    "VersionId": "20240703211658628_20250923155933781",
                    "VersionNum": "V7",
                    "VersionRemark": ""
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 16,
            "TotalPageNumber": 2
        },
        "RequestId": "076835e9-8262-4476-aaee-ed3a081b068d"
    }
}
```

