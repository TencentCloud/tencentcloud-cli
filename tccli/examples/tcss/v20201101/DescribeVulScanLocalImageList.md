**Example 1: 查询漏洞扫描任务的本地镜像列表**



Input: 

```
tccli tcss DescribeVulScanLocalImageList --cli-unfold-argument  \
    --TaskID 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "MediumLevelVulCount": 0,
                "ScanStatus": "SCANNING",
                "ScanEndTime": "2006-01-02 15:04:05",
                "ScanStartTime": "2006-01-02 15:04:05",
                "ErrorStatus": "0",
                "ImageID": "sha256:80beff5ff34259ceb7fbe9cd10b2d94912618f5b5595f234349c5bb0cd4f9211",
                "ImageName": "ImageName",
                "CriticalLevelVulCount": 0,
                "TaskID": 0,
                "ScanDuration": 0.0,
                "HighLevelVulCount": 0,
                "LowLevelVulCount": 0,
                "Size": 0.0
            }
        ],
        "RequestId": "d1b9dbe2-f78d-491a-b514-f0aa19d8ae4b"
    }
}
```

