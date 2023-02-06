**Example 1: 示例一**



Input: 

```
tccli dlc ModifyGovernEventRule --cli-unfold-argument  \
    --Name DataLakeCatalog.test_db \
    --Rule.AddDataFiles 1000 \
    --Rule.AddEqualityDeletes 1000 \
    --Rule.AddPositionDeletes 1000 \
    --Rule.AddDeleteFiles 1000
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

