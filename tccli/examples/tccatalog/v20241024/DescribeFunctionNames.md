**Example 1: DescribeFunctionNames示例**



Input: 

```
tccli tccatalog DescribeFunctionNames --cli-unfold-argument  \
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
        "RequestId": "3d3f939c-1884-45b5-a8f6-4ca1bdbca0a3"
    }
}
```

