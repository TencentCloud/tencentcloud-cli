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
        "ApiCallStats": 10,
        "InputTokenUsage": 1120,
        "OutputTokenUsage": 101,
        "RequestId": "716109cc-ee93-423a-85f0-a21fb7afcc4f",
        "SearchUsage": 10,
        "TotalTokenUsage": 1221
    }
}
```

