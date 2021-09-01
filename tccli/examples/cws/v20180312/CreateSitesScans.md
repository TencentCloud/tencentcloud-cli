**Example 1: 新增站点扫描任务**

新增一个或多个站点的单次扫描任务

Input: 

```
tccli cws CreateSitesScans --cli-unfold-argument  \
    --SiteIds 1 2 \
    --ScannerType normal \
    --RateLimit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

