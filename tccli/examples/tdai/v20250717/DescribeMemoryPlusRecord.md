**Example 1: 示例1**



Input: 

```
tccli tdai DescribeMemoryPlusRecord --cli-unfold-argument  \
    --SpaceId mem-1lpq**** \
    --Offset 0 \
    --Limit 10 \
    --RecordType conversation \
    --Filters.0.Name session_id \
    --Filters.0.Value barad-1779350361-131 \
    --OrderDirection ASC
```

Output: 
```
{
    "Response": {
        "Documents": [
            {
                "Fields": [
                    {
                        "Description": "时间戳",
                        "Name": "timestamp",
                        "Type": "json.Number",
                        "Value": "1779350361451"
                    }
                ],
                "Id": "msg-cb5bede3****"
            }
        ],
        "TotalCount": 20,
        "RequestId": "4dfebdaf-c04c-4bcf-9a62-0fbb48879987"
    }
}
```

