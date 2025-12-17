**Example 1: DescribeSchemaNamesPage**



Input: 

```
tccli tccatalog DescribeSchemaNamesPage --cli-unfold-argument  \
    --CatalogName system_catalog \
    --SchemaNamePattern information_*
```

Output: 
```
{
    "Response": {
        "SchemaNames": [
            {
                "Name": "information_schema",
                "Namespace": [
                    "system_catalog"
                ]
            }
        ],
        "SnapshotId": "",
        "TotalCount": 1,
        "RequestId": "f03d972f-b831-47c8-abd4-70ec9a5826ef"
    }
}
```

