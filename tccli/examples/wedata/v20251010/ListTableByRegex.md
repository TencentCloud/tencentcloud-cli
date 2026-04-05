**Example 1: 实例1**



Input: 

```
tccli wedata ListTableByRegex --cli-unfold-argument  \
    --DatasourceId id1 \
    --DatabaseName di1 \
    --RegexTable id2 \
    --WorkspaceId di31
```

Output: 
```
{
    "Response": {
        "Data": {
            "TableNames": [
                "table01"
            ]
        },
        "RequestId": "9b004f20-3d39-4f25-bdaa-2af7a043b970"
    }
}
```

