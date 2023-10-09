**Example 1: 查询主机快照备份列表**

查询主机快照备份列表

Input: 

```
tccli cwp DescribeRansomDefenseBackupList --cli-unfold-argument  \
    --Order xx \
    --Limit 1 \
    --Quuid xx \
    --Filters.0.Values xx \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch True \
    --Offset 1 \
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

