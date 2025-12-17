**Example 1: DescribeViewNames示例**



Input: 

```
tccli tccatalog DescribeViewNames --cli-unfold-argument  \
    --CatalogName c1 \
    --SchemaName s1
```

Output: 
```
{
    "Response": {
        "ViewNames": [
            {
                "Name": "v1",
                "Namespace": [
                    "default"
                ]
            }
        ],
        "RequestId": "bf74b3c1-5088-4721-b5e5-d6d558ca32ab"
    }
}
```

