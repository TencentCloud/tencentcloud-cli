**Example 1: 导出系统基线修复记录示例**

导出系统基线修复记录，返回导出任务ID

Input: 

```
tccli csip CreateBaselineFixRecordExportJob --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "JobId": "0001c003-0000-0000-0000-000000000003",
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

