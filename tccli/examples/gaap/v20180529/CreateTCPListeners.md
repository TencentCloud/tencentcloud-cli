**Example 1: 创建TCP监听器**

创建TCP监听器

Input: 

```
tccli gaap CreateTCPListeners --cli-unfold-argument  \
    --RealServerType IP \
    --ConnectTimeout 20 \
    --ProxyId link-bjkpdum1 \
    --HealthCheck 1 \
    --ListenerName test1 \
    --Scheduler rr \
    --Ports 90 \
    --DelayLoop 20
```

Output: 
```
{
    "Response": {
        "RequestId": "9aeda369-17c7-429f-be39-745c1e92fc71",
        "ListenerIds": [
            "listener-o0f3at99"
        ]
    }
}
```

