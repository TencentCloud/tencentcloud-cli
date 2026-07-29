**Example 1: 下载巡检报告**

下载巡检报告

Input: 

```
tccli dbbrain CreateDBDiagReportUrls --cli-unfold-argument  \
    --Product mysql \
    --AsyncRequestIds 68974526
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AsyncRequestId": 68974526,
                "ExpireTime": null,
                "ReportUrl": null
            }
        ],
        "TotalCount": 1,
        "RequestId": "e3bbadae-6e2f-45d5-89cc-cc57b3681dbe"
    }
}
```

