**Example 1: 成功示例**



Input: 

```
tccli wedata ListTaskVersions --cli-unfold-argument  \
    --ProjectId 3107313458352103424 \
    --TaskId 20260109115445849
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
                    "CreateTime": "2026-01-09 11:56:30",
                    "CreateUserUin": "700001893691",
                    "Status": null,
                    "UsedVersion": null,
                    "VersionId": "20260109115445849_20260109115630120",
                    "VersionNum": "V3",
                    "VersionRemark": ""
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 3,
            "TotalPageNumber": 1
        },
        "RequestId": "11c54132-3b1c-4f5f-abd6-039214193ec7"
    }
}
```

