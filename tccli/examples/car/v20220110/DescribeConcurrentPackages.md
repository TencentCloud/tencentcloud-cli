**Example 1: 获取云应用并发包列表示例**



Input: 

```
tccli car DescribeConcurrentPackages --cli-unfold-argument  \
    --Limit 0 \
    --Filters.0.Values cac-j6x242r6 \
    --Filters.0.Name ConcurrentId \
    --Offset 0 \
    --ConcurrentCategory DESKTOP
```

Output: 
```
{
    "Response": {
        "RequestId": "25b6f399-bd7c-4e5e-99a3-9a6f4b11e1b7",
        "Total": 0,
        "ConcurrentPackages": []
    }
}
```

