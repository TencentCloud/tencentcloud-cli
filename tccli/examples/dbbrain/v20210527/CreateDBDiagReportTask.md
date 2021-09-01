**Example 1: 创建健康报告, 发送邮件(可选)**



Input: 

```
tccli dbbrain CreateDBDiagReportTask --cli-unfold-argument  \
    --InstanceId test \
    --StartTime 2019-01-01T00:00:00+08:00 \
    --EndTime 2019-01-02T00:00:00+08:00 \
    --SendMailFlag 1 \
    --ContactPerson 1 \
    --ContactGroup 1
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": 129632,
        "RequestId": "77db16d7-bbe8-48a7-868b-ed776a96f1ab"
    }
}
```

