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

**Example 2: 使用 MARKETPLACE 查询市场资产列表**

示例资源 ID 请替换；MARKETPLACE 为固定大写常量，市场响应只包含公开字段。

Input: 

```
tccli ags DescribeRegistryRecordList --cli-unfold-argument  \
    --RegistryId MARKETPLACE \
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

