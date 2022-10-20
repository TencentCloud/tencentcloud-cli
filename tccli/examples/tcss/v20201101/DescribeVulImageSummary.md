**Example 1: 查询受漏洞影响的镜像统计**



Input: 

```
tccli tcss DescribeVulImageSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllAuthorizedImageCount": 0,
        "VulLibraryUpdateTime": "xx",
        "WebVulCount": 0,
        "SupportVulTotalCount": 0,
        "ScannedImageCount": 0,
        "VulTotalCount": 0,
        "EmergencyVulCount": 0,
        "RequestId": "xx",
        "SysTemVulCount": 0,
        "SeriousVulImageCount": 0
    }
}
```

