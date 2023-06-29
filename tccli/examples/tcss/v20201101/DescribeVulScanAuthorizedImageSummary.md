**Example 1: 统计漏洞扫描页已授权和未扫描镜像数**



Input: 

```
tccli tcss DescribeVulScanAuthorizedImageSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AllAuthorizedImageCount": 0,
        "RequestId": "xx",
        "UnScanAuthorizedImageCount": 0
    }
}
```

