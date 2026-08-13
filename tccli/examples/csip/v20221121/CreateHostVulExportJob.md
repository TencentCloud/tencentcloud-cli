**Example 1: 创建扫描导出任务**

创建扫描导出任务

Input: 

```
tccli csip CreateHostVulExportJob --cli-unfold-argument  \
    --BusinessAction RelateHostList \
    --MemberId mem-tencent-6f5795752f66e429 \
    --Filters.0.Name KbID \
    --Filters.0.Values 791 \
    --Filters.0.ExactMatch 1
```

Output: 
```
{
    "Response": {
        "JobID": "921621a1-3f26-43f8-80c0-e5de3221d8db",
        "RequestId": "50afc204-6d84-4bec-a9e4-006cac5d8358"
    }
}
```

