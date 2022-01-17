**Example 1: 查询本地binlog保留策略**



Input: 

```
tccli cdb DescribeLocalBinlogConfig --cli-unfold-argument  \
    --InstanceId cdb-c1nl9rpv
```

Output: 
```
{
    "Response": {
        "LocalBinlogConfig": {
            "MaxUsage": 30,
            "SaveHours": 120
        },
        "LocalBinlogConfigDefault": {
            "MaxUsage": 30,
            "SaveHours": 120
        },
        "RequestId": "a8cce05c-3975-1243-1087-17e2851d3486"
    }
}
```

