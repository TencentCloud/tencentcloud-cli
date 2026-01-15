**Example 1: 创建监听器转发规则**



Input: 

```
tccli gaap CreateRule --cli-unfold-argument  \
    --ListenerId listener-9vub5ymx \
    --Domain www.baidu.com \
    --Path / \
    --RealServerType IP \
    --Scheduler lc \
    --HealthCheck 0 \
    --ForwardProtocol HTTP \
    --ForwardHost www.baidu.com
```

Output: 
```
{
    "Response": {
        "RuleId": "rule-f13hgptl",
        "RequestId": "ea3b7a5e-5d9a-4dbb-a95d-5e299ee98b67"
    }
}
```

