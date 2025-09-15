**Example 1: 重启智能体实例的值守任务**



Input: 

```
tccli tdai ContinueAgentWork --cli-unfold-argument  \
    --InstanceId agentins-efbt5y3h \
    --AgentTaskType sql_precheck
```

Output: 
```
{
    "Response": {
        "RequestId": "a070f1a2-7538-5318-c843-6b47607aa78c"
    }
}
```

