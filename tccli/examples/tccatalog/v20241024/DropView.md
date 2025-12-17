**Example 1: DropView示例**



Input: 

```
tccli tccatalog DropView --cli-unfold-argument  \
    --CatalogName DataLakeCatalog \
    --SchemaName default \
    --ViewName jackietestview123
```

Output: 
```
{
    "Response": {
        "Dropped": true,
        "RequestId": "30eec33e-5170-42e0-bae2-503f39ee5ea6"
    }
}
```

