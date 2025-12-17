**Example 1: DropFunction示例**



Input: 

```
tccli tccatalog DropFunction --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --FunctionName f1
```

Output: 
```
{
    "Response": {
        "Dropped": true,
        "RequestId": "290b0018-05d6-4132-b31f-65bb93539bf7"
    }
}
```

