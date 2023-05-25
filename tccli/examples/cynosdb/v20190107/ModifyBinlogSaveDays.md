**Example 1: 修改集群Binlog保留天数**



Input: 

```
tccli cynosdb ModifyBinlogSaveDays --cli-unfold-argument  \
    --ClusterId cynosdb-xxxxxxxx \
    --BinlogSaveDays 10
```

Output: 
```
{
    "Response": {
        "RequestId": "9e56617c-c7cc-44e1-a967-6beb418ad5e7"
    }
}
```

