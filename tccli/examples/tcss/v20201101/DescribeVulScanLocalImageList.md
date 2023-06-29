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
                "ScanStatus": "xx",
                "ScanEndTime": "xx",
                "ScanStartTime": "xx",
                "ErrorStatus": "xx",
                "ImageID": "xx",
                "ImageName": "xx",
                "CriticalLevelVulCount": 0,
                "TaskID": 0,
                "ScanDuration": 0.0,
                "HighLevelVulCount": 0,
                "LowLevelVulCount": 0,
                "Size": 0.0
            }
        ],
        "RequestId": "xx"
    }
}
```

