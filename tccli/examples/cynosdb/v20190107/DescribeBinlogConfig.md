**Example 1: 查询binlog配置信息**

查询binlog配置信息

Input: 

```
tccli cynosdb DescribeBinlogConfig --cli-unfold-argument  \
    --ClusterId cynosdbmysql-xxx
```

Output: 
```
{
    "Response": {
        "BinlogCrossRegionsConfigUpdateTime": "abc",
        "BinlogConfig": {
            "BinlogSaveDays": 0,
            "BinlogCrossRegionsEnable": "abc",
            "BinlogCrossRegions": "abc"
        },
        "RequestId": "abc"
    }
}
```

