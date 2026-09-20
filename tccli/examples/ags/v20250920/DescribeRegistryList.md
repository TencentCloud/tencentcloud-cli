**Example 1: 模糊搜索 `example` 关键字**

未命中任何 Registry 时 RegistrySet 为空数组，TotalCount 为 0。

Input: 

```
tccli ags DescribeRegistryList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name search \
    --Filters.0.Values example
```

Output: 
```
{
    "Response": {
        "RequestId": "req-example",
        "RegistrySet": [],
        "TotalCount": 0
    }
}
```

