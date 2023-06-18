**Example 1: 示例一**



Input: 

```
tccli dlc DescribeGovernEventRule --cli-unfold-argument  \
    --Name DataLakeCatalog.tes_db
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RuleThreshold": {
            "Id": 1,
            "Type": "iceberg",
            "AppId": "123456",
            "Name": "DataLakeCatalog.test_db",
            "Rule": {
                "AddDataFiles": 1000,
                "AddEqualityDeletes": 1000,
                "AddPositionDeletes": 1000,
                "AddDeleteFiles": 1000
            }
        }
    }
}
```

