**Example 1: 查询 EdgeKV 命名空间列表**

查询站点 zone-3j1xw7910arp 下的 EdgeKV 命名空间列表，从第 0 条开始，每页返回 10 条，按创建时间降序排列。

Input: 

```
tccli teo DescribeEdgeKVNamespaces --cli-unfold-argument  \
    --ZoneId zone-3j1xw7910arp \
    --Offset 0 \
    --Limit 10 \
    --SortBy created-on \
    --SortOrder desc
```

Output: 
```
{
    "Response": {
        "KVNamespaces": [
            {
                "Capacity": 1073741824,
                "CapacityUsed": 0,
                "CreatedOn": "2026-03-25T17:16:01+08:00",
                "ModifiedOn": "2026-03-25T17:16:01+08:00",
                "Namespace": "ns-011",
                "References": [],
                "Remark": "remark"
            }
        ],
        "TotalCount": 9,
        "RequestId": "ce0353db-f6f6-48ee-8275-50e1ebf990e8"
    }
}
```

