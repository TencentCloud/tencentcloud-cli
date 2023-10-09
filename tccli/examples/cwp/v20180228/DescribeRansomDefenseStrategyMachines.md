**Example 1: 查询防勒索策略绑定机器列表**

查询防勒索策略绑定机器列表

Input: 

```
tccli cwp DescribeRansomDefenseStrategyMachines --cli-unfold-argument  \
    --Id 1 \
    --Limit 1 \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
    --Order xx \
    --By xx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {}
        ],
        "RequestId": "xx"
    }
}
```

