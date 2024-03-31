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
                "Id": "abc",
                "Name": "abc",
                "Value": "abc",
                "Type": "abc",
                "Properties": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "Alias": "abc",
                "Comment": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

