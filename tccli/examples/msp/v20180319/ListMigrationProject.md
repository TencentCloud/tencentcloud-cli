**Example 1: 获取迁移项目名称列表**

获取迁移项目名称列表

Input: 

```
tccli msp ListMigrationProject --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "Projects": [
            {
                "ProjectId": 10013,
                "ProjectName": "test2"
            },
            {
                "ProjectId": 10012,
                "ProjectName": "test1"
            },
            {
                "ProjectId": 10007,
                "ProjectName": "test"
            }
        ],
        "RequestId": "1824f552-3027-458f-82e9-4603846e52c4"
    }
}
```

