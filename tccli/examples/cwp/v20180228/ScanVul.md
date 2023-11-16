**Example 1: 漏洞一键检测**



Input: 

```
tccli cwp ScanVul --cli-unfold-argument  \
    --VulCategories 1,2 \
    --VulLevels 1,2,3,4 \
    --HostType 1 \
    --QuuidList 69796250-2a3a-40ef-b418-676e677019a4 \
    --VulEmergency 1 \
    --TimeoutPeriod 3600 \
    --VulIds 1
```

Output: 
```
{
    "Response": {
        "TaskId": 1,
        "RequestId": "69796250-2a3a-40ef-b418-676e677019a4"
    }
}
```

