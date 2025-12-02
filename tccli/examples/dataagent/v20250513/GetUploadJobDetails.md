**Example 1: 查询上传任务**

查询上传任务

Input: 

```
tccli dataagent GetUploadJobDetails --cli-unfold-argument  \
    --InstanceId dataagent-G5XTaxnz \
    --JobId job-9drpcx7eb7
```

Output: 
```
{
    "Response": {
        "Job": {
            "CreateTime": "2025-11-19T14:23:35.384323792+08:00",
            "Id": 0,
            "InstanceId": "dataagent-G5XTaxnz",
            "JobId": "job-9drpcx7eb7",
            "KnowledgeBaseId": "",
            "Message": "",
            "Status": "Success",
            "SubUin": "",
            "Uin": "",
            "UpdateTime": "2025-11-19T14:23:35.384323868+08:00"
        },
        "RequestId": "44545091-0bac-4260-adca-76dbd703614f"
    }
}
```

