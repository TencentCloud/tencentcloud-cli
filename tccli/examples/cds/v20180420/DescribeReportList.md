**Example 1: 查询报表列表**



Input: 

```
tccli cds DescribeReportList --cli-unfold-argument  \
    --Limit 0 \
    --Offset 0 \
    --Name ip-report \
    --StartTime 0 \
    --EndTime 0 \
    --ReportType 0 \
    --ReportStatus 0 \
    --TemplateId 0 \
    --Field ip \
    --Sort desc \
    --CntDay 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "List": [
            {
                "AddTime": 1730446418,
                "EndTime": 1730446418,
                "Id": 0,
                "InstanceId": 0,
                "IsDelete": 0,
                "Receivers": "bob",
                "Remark": "11 月会话分析",
                "ReportFile": "file.html",
                "ReportStatus": 0,
                "ReportTmpStatus": 0,
                "ReportType": 0,
                "SendResult": "success",
                "SendType": "site",
                "StartTime": 1730446418,
                "Title": "11 月会话分析",
                "TemplateId": 1,
                "AssetsList": [],
                "CntDay": 1
            }
        ],
        "RequestId": "a8aa8bbc-c255-42b1-88c4-04419f435a77"
    }
}
```

