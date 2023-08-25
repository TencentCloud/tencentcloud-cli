**Example 1: 获取模板更新提示信息**

获取模板更新提示信息

Input: 

```
tccli dsgc DescribeDSPAComplianceUpdateNotification --cli-unfold-argument  \
    --DspaId dspa-001 \
    --ComplianceId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "128009ac-7df4-0530-cc92-52f0d945e191",
        "IsUpdated": true,
        "TaskNameSet": [
            "aaa"
        ]
    }
}
```

