**Example 1: 查询主机资产自动同步结果**

查询主机资产自动同步结果

Input: 

```
tccli dasb DescribeAssetSyncStatus --cli-unfold-argument  \
    --Category 1
```

Output: 
```
{
    "Response": {
        "RequestId": "79b7b771-368d-44b7-b954-f0cceda748e2",
        "Status": {
            "LastStatus": 1,
            "LastTime": "2021-09-22T15:04:05+08:00",
            "InProcess": true
        }
    }
}
```

