**Example 1: 漏洞管理 - 一键检测**

漏洞管理 - 一键检测

Input: 

```
tccli cwp ScanVul --cli-unfold-argument  \
    --VulCategories 1;2 \
    --VulLevels 1;2 \
    --HostType 1 \
    --VulEmergency 1
```

Output: 
```
{
    "Response": {
        "RequestId": "4234234",
        "TaskId": 1
    }
}
```

