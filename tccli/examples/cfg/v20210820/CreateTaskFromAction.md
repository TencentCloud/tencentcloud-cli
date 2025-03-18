**Example 1: 根据动作创建演练**

根据动作创建演练示例

Input: 

```
tccli cfg CreateTaskFromAction --cli-unfold-argument  \
    --TaskActionId 12 \
    --TaskInstances ins-jjphrwng \
    --TaskTitle CVM服务器空操作 \
    --TaskDescription 创建演练测试
```

Output: 
```
{
    "Response": {
        "RequestId": "a3875789-7d89-4bf1-8763-e9b46c6459d7",
        "TaskId": 10959
    }
}
```

