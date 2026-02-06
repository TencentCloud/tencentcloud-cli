**Example 1: 成功示例**



Input: 

```
tccli wedata ListTaskVersions --cli-unfold-argument  \
    --TaskId 20250723102549746 \
    --ProjectId 1464962169590902784 \
    --TaskVersionType SUBMIT
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "ApproveStatus": "u65e0u9700u5ba1u6279",
                    "ApproveUserUin": null,
                    "CreateTime": "2025-08-27 14:48:32",
                    "CreateUserUin": "100028579606",
                    "Status": "Y",
                    "VersionId": "20250723102549746_20250827144832136",
                    "VersionNum": "V41",
                    "VersionRemark": "11"
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 14,
            "TotalPageNumber": 2
        },
        "RequestId": "8babe7ee-868b-4e7b-a82f-825835e6482a"
    }
}
```

