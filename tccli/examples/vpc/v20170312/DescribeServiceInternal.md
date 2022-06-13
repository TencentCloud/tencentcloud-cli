**Example 1: 查询接口**



Input: 

```
tccli vpc DescribeServiceInternal --cli-unfold-argument  \
    --Offset 0 \
    --Limit 2 \
    --Filters.0.Name vpc-id \
    --Filters.0.Values vpc-e3t30r8t
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

