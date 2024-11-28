**Example 1: 导出自由画布**

导出自由画布

Input: 

```
tccli bi ExportScreenPage --cli-unfold-argument  \
    --ProjectId 1907 \
    --PageId 39618 \
    --CanvasType FREE \
    --PicType url
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
            "PicType": "abc",
            "List": [
                {
                    "Content": "abc",
                    "WidgetId": "abc"
                }
            ],
            "TranId": "abc",
            "TranStatus": 0
        },
        "Msg": "abc",
        "RequestId": "abc"
    }
}
```

