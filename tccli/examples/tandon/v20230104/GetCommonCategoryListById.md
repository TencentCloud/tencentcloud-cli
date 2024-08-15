**Example 1: 示例**



Input: 

```
tccli tandon GetCommonCategoryListById --cli-unfold-argument  \
    --Level2Id 1107
```

Output: 
```
{
    "Response": {
        "Data": {
            "Level1Name": "abc",
            "Level2Name": "abc",
            "Categories": [
                {
                    "Id": 1,
                    "Cell": {
                        "Name": "abc",
                        "Description": "abc",
                        "Weights": 1,
                        "Queue": 1,
                        "ServiceSceneCode": 1,
                        "Support": 1,
                        "EnableTicketAssistantAnswer": 1,
                        "Visible": 0
                    },
                    "CustomFields": [
                        {
                            "FieldId": 1,
                            "Name": "abc",
                            "Type": "abc",
                            "Copywriter": "abc",
                            "Remark": "abc",
                            "Required": 0,
                            "Options": "abc",
                            "Weights": 1,
                            "ApplyChannel": "abc",
                            "ParentFieldId": 1
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

