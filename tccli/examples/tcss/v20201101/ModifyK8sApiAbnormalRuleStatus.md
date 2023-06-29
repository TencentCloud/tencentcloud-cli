**Example 1: 修改k8sapi异常事件规则状态**



Input: 

```
tccli tcss ModifyK8sApiAbnormalRuleStatus --cli-unfold-argument  \
    --RuleID xxx \
    --Status True
```

Output: 
```
{
    "Response": {
        "RequestId": "522d7714-ef53-4940-b0ed-46d59a3cf0fd"
    }
}
```

