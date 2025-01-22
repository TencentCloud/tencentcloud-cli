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
            "ErrorTip": "",
            "ErrorMessage": "接口错误",
            "ErrorLevel": "ERROR",
            "DocLink": "",
            "FAQ": "",
            "ReservedField": ""
        },
        "Extra": "",
        "Data": {
            "PicType": "PNG",
            "List": [
                {
                    "Content": "",
                    "WidgetId": "saia192"
                }
            ],
            "TranId": "qwq211221",
            "TranStatus": 0
        },
        "Msg": "失败",
        "RequestId": "ddsds122321-fdsd12"
    }
}
```

