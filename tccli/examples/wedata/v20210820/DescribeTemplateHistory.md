**Example 1: 查询规则模版操作记录**

查询规则模版操作记录

Input: 

```
tccli wedata DescribeTemplateHistory --cli-unfold-argument  \
    --ProjectId 1 \
    --PageNumber 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "UserName": "xx",
                    "AlterContent": "xx",
                    "AlterType": 1,
                    "UserId": 1,
                    "Version": 1,
                    "TemplateId": 1
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

