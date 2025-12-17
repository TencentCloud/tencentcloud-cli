**Example 1: DescribeFunctionNamesPage示例**



Input: 

```
tccli tccatalog DescribeFunctionNamesPage --cli-unfold-argument  \
    --CatalogName layyu_lakehouse \
    --SchemaName s1
```

Output: 
```
{
    "Response": {
        "FunctionNames": [
            {
                "Name": "f2",
                "Namespace": [
                    "layyu_lakehouse"
                ]
            }
        ],
        "SnapshotId": "",
        "TotalCount": 1,
        "RequestId": "0207a84a-d1fd-426e-83d0-5053a75f3737"
    }
}
```

