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
            "ErrorTip": "",
            "ErrorMessage": "",
            "ErrorLevel": "INFO",
            "DocLink": "",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Data": {
            "CorpId": "110112",
            "ProjectId": "1101",
            "PageId": "1",
            "WidgetList": [
                {
                    "WidgetId": "dsjdsk",
                    "WidgetName": "表格"
                }
            ]
        },
        "Msg": "成功",
        "RequestId": "sadadadfdkfdl212313dsds"
    }
}
```

