**Example 1: 1**



Input: 

```
tccli wedata CreateModelVersion --cli-unfold-argument  \
    --CatalogName model \
    --SchemaName schema \
    --ModelName testaaa \
    --Uri http://130.1.1.1 \
    --Comment aaabbb
```

Output: 
```
{
    "Response": {
        "Data": {
            "Created": true
        },
        "RequestId": "abab2560-c9d1-4461-9acb-3d355e20eda0"
    }
}
```

