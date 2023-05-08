**Example 1: GetIntegrationNodeColumnSchema**



Input: 

```
tccli wedata GetIntegrationNodeColumnSchema --cli-unfold-argument  \
    --ColumnContent {"a":1,"b":"0","c":0} \
    --DatasourceType KAFKA
```

Output: 
```
{
    "Response": {
        "Schemas": [
            {
                "Name": "a",
                "Value": "int"
            },
            {
                "Name": "b",
                "Value": "string"
            },
            {
                "Name": "c",
                "Value": "int"
            }
        ],
        "RequestId": "xx"
    }
}
```

