**Example 1: 查询受漏洞影响的镜像统计**



Input: 

```
tccli tcss DescribeVulImageSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllAuthorizedImageCount": 5703,
        "EmergencyVulCount": 38,
        "RequestId": "e06df6e9-3f54-41d0-9857-41ed365623a2",
        "ScannedImageCount": 2,
        "SeriousVulImageCount": 2,
        "SupportVulTotalCount": 70678,
        "SysTemVulCount": 634,
        "VulLibraryUpdateTime": "2024-10-29 19:42:56",
        "VulTotalCount": 2086,
        "WebVulCount": 1442
    }
}
```

