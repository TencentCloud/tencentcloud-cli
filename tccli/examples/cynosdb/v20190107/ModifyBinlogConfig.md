**Example 1: 修改binlog配置信息**

修改binlog配置信息

Input: 

```
tccli cynosdb ModifyBinlogConfig --cli-unfold-argument  \
    --ClusterId abc \
    --BinlogConfig.BinlogSaveDays 0 \
    --BinlogConfig.BinlogCrossRegionsEnable abc \
    --BinlogConfig.BinlogCrossRegions abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

