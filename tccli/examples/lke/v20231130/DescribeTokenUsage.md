**Example 1: 获取调用统计**

获取调用统计

Input: 

```
tccli lke DescribeTokenUsage --cli-unfold-argument  \
    --UinAccount 700001187441
```

Output: 
```
{
    "Response": {
        "ApiCallStats": 0,
        "InputTokenUsage": 0,
        "OutputTokenUsage": 0,
        "RequestId": "716109cc-ee93-423a-85f0-a21fb7afcc4f",
        "SearchUsage": 0,
        "TotalTokenUsage": 0
    }
}
```

