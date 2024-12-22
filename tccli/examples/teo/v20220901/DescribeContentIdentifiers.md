**Example 1: 查询内容标识符信息**

指定 ID 查询内容标识符

Input: 

```
tccli teo DescribeContentIdentifiers --cli-unfold-argument  \
    --Filters.0.Name content-id \
    --Filters.0.Values eocontent-27q0p0sali16 \
    --Filters.0.Fuzzy False
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "3c140219-cfe9-470e-b341-907877d6fb03",
        "ContentIdentifiers": [
            {
                "ContentId": "eocontent-27q0p0sali16",
                "Description": "content-test",
                "PlanId": "edgeone-2ycvs8ml4zpq",
                "ReferenceCount": 10,
                "Tags": [
                    {
                        "TagKey": "test",
                        "TagValue": "ct"
                    }
                ],
                "CreatedOn": "2023-10-05T15:30:45Z",
                "ModifiedOn": "2023-10-05T15:30:45Z",
                "DeletedOn": null,
                "Status": "active"
            }
        ]
    }
}
```

