**Example 1: 查询资产打标值**

查询资产打标值

Input: 

```
tccli wedata ListTagsByAsset --cli-unfold-argument  \
    --QueryItems.0.PropertyType catalog \
    --QueryItems.0.PropertyId 566
```

Output: 
```
{
    "Response": {
        "Data": {
            "Results": [
                {
                    "CreateTime": "2025-12-03T06:32:44.901Z",
                    "Creator": "",
                    "ModifiedTime": "2025-12-03T06:32:44.901Z",
                    "Modifier": "",
                    "OwnerAccount": "",
                    "PropertyId": "566",
                    "PropertyType": "catalog",
                    "Tags": [
                        {
                            "LabelId": "27",
                            "LabelName": "label1",
                            "LabelValue": "labelvalue1",
                            "LabelValueId": "53"
                        }
                    ]
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "a00c5b73-c372-4841-9040-5037b9b6dc8f"
    }
}
```

