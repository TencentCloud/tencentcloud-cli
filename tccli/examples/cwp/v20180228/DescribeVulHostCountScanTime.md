**Example 1: 获取待处理漏洞数+影响主机数**

获取待处理漏洞数+影响主机数

Input: 

```
tccli cwp DescribeVulHostCountScanTime --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "ScanTime": "2020-01-01 00:00:00",
        "TotalVulCount": 38,
        "VulHostCount": 16,
        "IfFirstScan": true,
        "hadAutoFixVul": true,
        "LastFixTime": "xx",
        "TaskId": 1
    }
}
```

