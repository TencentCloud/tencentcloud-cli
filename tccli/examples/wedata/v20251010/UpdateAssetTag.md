**Example 1: 修改资产打标值**

修改资产打标值

Input: 

```
tccli wedata UpdateAssetTag --cli-unfold-argument  \
    --PropertyType catalog \
    --PropertyId 599 \
    --Tags.0.LabelId 1 \
    --Tags.0.LabelName 11 \
    --Tags.0.LabelValueId 2 \
    --Tags.0.LabelValue 22
```

Output: 
```
{
    "Response": {
        "Data": {
            "Message": "修改成功",
            "Success": true,
            "UpdatedResult": {
                "CreateTime": "2025-12-03T07:34:25.703Z",
                "Creator": "",
                "ModifiedTime": "2025-12-03T07:34:25.703Z",
                "Modifier": "",
                "OwnerAccount": "",
                "PropertyId": "599",
                "PropertyType": "catalog",
                "Tags": [
                    {
                        "LabelId": "1",
                        "LabelName": "11",
                        "LabelValue": "22",
                        "LabelValueId": "2"
                    }
                ]
            }
        },
        "RequestId": "a00770b7-6a05-49c3-b655-8fdbb7e06a07"
    }
}
```

