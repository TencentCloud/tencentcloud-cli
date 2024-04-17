**Example 1: GetIntegrationNodeColumnSchema**



Input: 

```
tccli wedata GetIntegrationNodeColumnSchema --cli-unfold-argument  \
    --ColumnContent {  "id": 1699859100000,  "name": "This seems to be a string", "len": 0,  "a1": "This seems to be a string"} \
    --DatasourceType MYSQL
```

Output: 
```
{
    "Response": {
        "Schemas": [
            {
                "Alias": null,
                "Comment": "",
                "Id": "",
                "Name": "id",
                "Properties": null,
                "Type": "bigint",
                "Value": null
            },
            {
                "Alias": null,
                "Comment": "",
                "Id": "",
                "Name": "name",
                "Properties": null,
                "Type": "string",
                "Value": null
            },
            {
                "Alias": null,
                "Comment": "",
                "Id": "",
                "Name": "len",
                "Properties": null,
                "Type": "int",
                "Value": null
            },
            {
                "Alias": null,
                "Comment": "",
                "Id": "",
                "Name": "a1",
                "Properties": null,
                "Type": "string",
                "Value": null
            }
        ],
        "RequestId": "b86188b4-93e4-4b90-a5ed-2f7346af921f"
    }
}
```

