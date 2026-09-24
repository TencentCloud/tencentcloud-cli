**Example 1: 示例1**



Input: 

```
tccli dlc DescribeCatalogTableNames --cli-unfold-argument  \
    --CatalogName chenfan_test_1 \
    --SchemaName default
```

Output: 
```
{
    "Response": {
        "TableNames": [
            {
                "Name": "sdfsdf",
                "Namespace": [
                    "chenfan_test_1"
                ]
            }
        ],
        "RequestId": "12e53385-1ed0-4ef3-be44-640bf69d9eb9"
    }
}
```

