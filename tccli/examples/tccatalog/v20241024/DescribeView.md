**Example 1: DescribeView示例**



Input: 

```
tccli tccatalog DescribeView --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1 \
    --ViewName v1
```

Output: 
```
{
    "Response": {
        "View": {
            "EngineType": "",
            "Name": "",
            "ViewDefinition": "",
            "ViewType": ""
        },
        "RequestId": "30a12e80-2a5c-4516-8d7f-2a1fae67057c"
    }
}
```

