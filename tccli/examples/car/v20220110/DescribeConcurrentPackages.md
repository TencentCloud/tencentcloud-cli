**Example 1: 获取云应用并发包列表示例**



Input: 

```
tccli car DescribeConcurrentPackages --cli-unfold-argument  \
    --Limit 0 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Total": 0,
        "ConcurrentPackages": []
    }
}
```

