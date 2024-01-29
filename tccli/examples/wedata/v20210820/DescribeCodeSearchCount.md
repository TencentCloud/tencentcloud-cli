**Example 1: 搜索结果统计示例**



Input: 

```
tccli wedata DescribeCodeSearchCount --cli-unfold-argument  \
    --Status dev \
    --ProjectId 1 \
    --Keyword hive \
    --SearchScopes orchrestrationSpace developmentSpace recycle
```

Output: 
```
{
    "Response": {
        "RequestId": "e57c6471-1780-4e85-8fc0-7f01ed7529ac",
        "Data": {
            "DevCount": 0,
            "ScheduleCount": 4,
            "RecycleCount": 0
        }
    }
}
```

