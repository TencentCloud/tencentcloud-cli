**Example 1: 查询规则模版操作记录**

查询规则模版操作记录

Input: 

```
tccli wedata DescribeTemplateHistory --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "TotalCount": 1,
            "Items": [
                {
                    "UserName": "abc",
                    "AlterContent": "abc",
                    "AlterType": 1,
                    "UserId": 1,
                    "Version": 1,
                    "TemplateId": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

