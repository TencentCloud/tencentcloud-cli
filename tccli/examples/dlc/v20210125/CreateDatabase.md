**Example 1: 生成建库SQL语句**



Input: 

```
tccli dlc CreateDatabase --cli-unfold-argument  \
    --DatabaseInfo.Comment xx \
    --DatabaseInfo.Properties.0.Value xx \
    --DatabaseInfo.Properties.0.Key xx \
    --DatabaseInfo.DatabaseName xx
```

Output: 
```
{
    "Response": {
        "Execution": {
            "SQL": "xx"
        },
        "RequestId": "xx"
    }
}
```

