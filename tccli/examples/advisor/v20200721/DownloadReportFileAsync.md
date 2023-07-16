**Example 1: 下载报告**

下载报告

Input: 

```
tccli advisor DownloadReportFileAsync --cli-unfold-argument  \
    --Id 0 \
    --Type abc \
    --TaskId abc \
    --Env abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValues abc \
    --TaskType abc \
    --TopicType 0 \
    --CloudMapUuid abc
```

Output: 
```
{
    "Response": {
        "ResultId": "abc",
        "ReportAuthorized": true,
        "RequestId": "abc"
    }
}
```

