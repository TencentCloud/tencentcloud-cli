**Example 1: 提交工作流调度任务至生产**

提交工作流调度任务至生产

Input: 

```
tccli wedata SubmitTriggerTask --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20251121163138956 \
    --VersionRemark submit_1125
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true,
            "VersionId": "20251121163138956_20251125104113487"
        },
        "RequestId": "21cf5fae-69ea-4028-a3fc-157f66f5a30e"
    }
}
```

