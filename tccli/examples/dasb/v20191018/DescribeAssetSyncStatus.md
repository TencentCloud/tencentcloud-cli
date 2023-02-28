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
        "RequestId": "xxxxxxxxx",
        "Status": {
            "LastStatus": 1,
            "LastTime": "2021-09-22T15:04:05Z07:00",
            "InProcess": true
        }
    }
}
```

