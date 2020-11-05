**Example 1: Obtaining the list of migration project names**

This example shows you how to obtain the list of migration project names.

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
                "projectName": "test2",
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

