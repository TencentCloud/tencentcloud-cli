**Example 1: 下载报告**

下载报告

Input: 

```
tccli advisor DownloadReportFileAsync --cli-unfold-argument  \
    --Id 0 \
    --Type Group \
    --TaskId a0b7cfdd-83e6-49c5-b156-37272bada0da \
    --Env public \
    --TaskType allTaskType \
    --TopicType 0 \
    --CloudMapUuid arch-rm9u9s8g
```

Output: 
```
{
    "Response": {
        "ResultId": "-1#Group#0f7c2fac-20ee-4da9-8e71-944577bf7616",
        "ReportAuthorized": true,
        "RequestId": "eb710d64-cd7d-4b22-975b-1edf1a6330c8"
    }
}
```

