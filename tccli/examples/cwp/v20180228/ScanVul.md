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
        "RequestId": "c741a4fd-776f-499b-85a2-7bc70fd5b92s",
        "TaskId": 1
    }
}
```

