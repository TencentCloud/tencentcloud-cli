**Example 1: 查询binlog配置信息**

查询binlog配置信息

Input: 

```
tccli cynosdb DescribeBinlogConfig --cli-unfold-argument  \
    --ClusterId DescribeBinlogConffv
```

Output: 
```
{
    "Response": {
        "BinlogConfig": {
            "BinlogCrossRegions": [
                "ap-guangzhou"
            ],
            "BinlogCrossRegionsEnable": "ON",
            "BinlogSaveDays": 7
        },
        "BinlogCrossRegionsConfigUpdateTime": "2024-12-23 19:27:09",
        "RequestId": "e01e2fd6-10bc-45a0-b715-0d29a5fb317d"
    }
}
```

