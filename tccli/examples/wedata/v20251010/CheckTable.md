**Example 1: TableNoteExists**



Input: 

```
tccli wedata CheckTable --cli-unfold-argument  \
    --CatalogName c4 \
    --SchemaName default \
    --TableName tableA \
    --WorkspaceId 17697667906247629
```

Output: 
```
{
    "Response": {
        "Data": {
            "Exists": false
        },
        "RequestId": "f0bd2597-6ef6-4f3e-8886-72e26e6a2fa4"
    }
}
```

