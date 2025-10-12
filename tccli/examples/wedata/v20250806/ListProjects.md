**Example 1: 正常调用**



Input: 

```
tccli wedata ListProjects --cli-unfold-argument  \
    --ProjectName jian_pro1 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "CreateTime": "2025-08-28T17:23:10+08:00",
                    "CreatorUin": "100028579606",
                    "Description": "default",
                    "DisplayName": "jian_pro1",
                    "ProjectId": "2916098084817846272",
                    "ProjectModel": "SIMPLE",
                    "ProjectName": "jian_pro1",
                    "ProjectOwnerUin": null,
                    "Status": 1
                }
            ],
            "PageNumber": 1,
            "PageSize": 10,
            "TotalCount": 1,
            "TotalPageNumber": 1
        },
        "RequestId": "6abbd6f0-20ce-4f38-84f3-bb2c6d615f62"
    }
}
```

