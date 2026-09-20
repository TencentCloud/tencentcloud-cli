**Example 1: 查询 weather 相关 Record**



Input: 

```
tccli ags DescribeRegistryRecordList --cli-unfold-argument  \
    --RegistryId reg-0123abcd \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name search \
    --Filters.0.Values weather
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "RecordSet": [],
        "TotalCount": 0
    }
}
```

