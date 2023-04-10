**Example 1: 删除健康报告生成任务**

健康报告任务删除成功

Input: 

```
tccli dbbrain DeleteDBDiagReportTasks --cli-unfold-argument  \
    --InstanceId cdb-inste123 \
    --Product mysql \
    --AsyncRequestIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5fdab910-5c9e-11eb-a610-8717ee1b1000",
        "Status": 0
    }
}
```

