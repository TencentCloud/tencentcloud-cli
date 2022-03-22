**Example 1: 创建数据导出任务**



Input: 

```
tccli dlc CreateExportTask --cli-unfold-argument  \
    --InputType taskResult \
    --InputConf.0.Key taskId \
    --InputConf.0.Value b99e07e08a3811ec8e8f525400afd9d2 \
    --OutputType cos \
    --OutputConf.0.Key path \
    --OutputConf.0.Value cosn://@dlcda57--0205-4299-82a3/
```

Output: 
```
{
    "Response": {
        "TaskId": "xxxx-xxx",
        "RequestId": "123-abc"
    }
}
```

