**Example 1: 创建基线主任务导出任务示例**

创建基线主任务导出任务，返回导出任务ID

Input: 

```
tccli csip CreateBaselineMainTaskExportJob --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29
```

Output: 
```
{
    "Response": {
        "JobId": "0001a001-0000-0000-0000-000000000001",
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

