**Example 1: Binlog保留天数查询**



Input: 

```
tccli cynosdb DescribeBinlogSaveDays --cli-unfold-argument  \
    --ClusterId cynosdbmysql-rtqj0kp5
```

Output: 
```
{
    "Response": {
        "BinlogSaveDays": 7,
        "RequestId": "9bea88d4-9549-4101-b1b9-8d7ceb0581a2"
    }
}
```

