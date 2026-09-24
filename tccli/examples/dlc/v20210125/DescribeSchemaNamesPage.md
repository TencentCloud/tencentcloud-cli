**Example 1: 示例1**



Input: 

```
tccli dlc DescribeSchemaNamesPage --cli-unfold-argument  \
    --CatalogName chenfan_test_1 \
    --Limit 1000
```

Output: 
```
{
    "Response": {
        "SchemaNames": [
            {
                "Name": "default",
                "Namespace": [
                    "chenfan_test_1"
                ]
            }
        ],
        "TotalCount": 3,
        "SnapshotId": "",
        "RequestId": "dca17bf4-111c-48aa-b995-8a210e180cea"
    }
}
```

