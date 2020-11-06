**Example 1: 录音列表下载**



Input: 

```
tccli cr DownloadRecordList --cli-unfold-argument  \
    --Module Record \
    --Operation DownloadList \
    --InstId ins-abc123 \
    --BizDate 2019-09-16
```

Output: 
```
{
    "Response": {
        "RecordListUrl": "http://collection-robot.myqcloud.com/record-list.zip",
        "RequestId": "15d67679-7f71-4077-a7bd-c0ed27ae2461"
    }
}
```

