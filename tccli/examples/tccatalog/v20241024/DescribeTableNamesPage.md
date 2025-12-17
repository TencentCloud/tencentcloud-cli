**Example 1: DescribeTableNamesPage示例**



Input: 

```
tccli tccatalog DescribeTableNamesPage --cli-unfold-argument  \
    --CatalogName string \
    --SchemaName string
```

Output: 
```
{
    "Response": {
        "RequestId": "string",
        "TableNames": [
            "t1",
            "t2"
        ],
        "TotalCount": 2
    }
}
```

