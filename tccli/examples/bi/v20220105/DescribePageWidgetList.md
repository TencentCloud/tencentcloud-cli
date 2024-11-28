**Example 1: 成功**



Input: 

```
tccli bi DescribePageWidgetList --cli-unfold-argument  \
    --ProjectId 662 \
    --PageId 6465
```

Output: 
```
{
    "Response": {
        "ErrorInfo": {
            "ErrorTip": "abc",
            "ErrorMessage": "abc",
            "ErrorLevel": "abc",
            "DocLink": "abc",
            "FAQ": "abc",
            "ReservedField": "abc"
        },
        "Extra": "abc",
        "Data": {
            "CorpId": "abc",
            "ProjectId": "abc",
            "PageId": "abc",
            "WidgetList": [
                {
                    "WidgetId": "abc",
                    "WidgetName": "abc"
                }
            ]
        },
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

