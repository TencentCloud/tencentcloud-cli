**Example 1: 查询冲突问列表**

查询冲突问列表

Input: 

```
tccli adp DescribeConflictQASummaryList --cli-unfold-argument  \
    --FilterList.0.Name status \
    --FilterList.0.ValueList 1 \
    --KbId 2095766521673516736 \
    --PageNumber 0 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "ConflictQaList": [
            {
                "ConflictGroupId": "2096809118072442560"
            }
        ],
        "TotalCount": 3,
        "RequestId": "ca71b9e2-5def-41c0-bdfc-46fd60cc1717"
    }
}
```

