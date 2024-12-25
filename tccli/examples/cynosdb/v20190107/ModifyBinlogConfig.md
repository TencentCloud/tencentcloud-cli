**Example 1: 修改binlog配置信息**

修改binlog配置信息

Input: 

```
tccli cynosdb ModifyBinlogConfig --cli-unfold-argument  \
    --ClusterId cynosdbmysql-grhvkwff \
    --BinlogConfig.BinlogSaveDays 0 \
    --BinlogConfig.BinlogCrossRegionsEnable yes \
    --BinlogConfig.BinlogCrossRegions ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "51169b54-61d4-4604-a07e-e519a5527923"
    }
}
```

