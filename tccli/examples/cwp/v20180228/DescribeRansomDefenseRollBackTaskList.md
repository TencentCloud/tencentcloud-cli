**Example 1: 查询回滚任务列表**

查询回滚任务列表

Input: 

```
tccli cwp DescribeRansomDefenseRollBackTaskList --cli-unfold-argument  \
    --Order xx \
    --Limit 1 \
    --By xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1
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

