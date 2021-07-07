**Example 1: 定期扫描漏洞设置**

定期扫描漏洞设置

Input: 

```
tccli cwp ScanVulSetting --cli-unfold-argument  \
    --VulCategories 1 \
    --VulLevels 1 \
    --TimerInterval 3 \
    --TimerTime 02:10:50 \
    --VulEmergency 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234"
    }
}
```

