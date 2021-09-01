**Example 1: 查看当前漏洞总计数量**

查询用户网站的漏洞总计数量

Input: 

```
tccli cws DescribeVulsNumber --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ImpactSiteNumber": 1,
        "PageCount": 33,
        "RequestId": "de766e0c-963f-4984-b145-f1085ff165a0",
        "SiteNumber": 8,
        "VulsHighNumber": 8,
        "VulsLowNumber": 0,
        "VulsMiddleNumber": 2,
        "VulsNoticeNumber": 0
    }
}
```

