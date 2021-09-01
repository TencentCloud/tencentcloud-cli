**Example 1: 创建任务**

创建任务

Input: 

```
tccli tsf CreateTask --cli-unfold-argument  \
    --TaskName test \
    --TaskContent com.example.task.simpleTask \
    --TaskArgument taskArgumentTest \
    --ExecuteType UNICAST \
    --TaskType JAVA \
    --TaskRule.RuleType Cron \
    --TaskRule.RepeatInterval 0 \
    --TaskRule.Expression 00/1****? \
    --TimeOut 30000 \
    --GroupId group-12345678
```

Output: 
```
{
    "Response": {
        "RequestId": "6281ddf9-1914-420b-afb8-93735ac3270a",
        "Result": "task-12345678"
    }
}
```

