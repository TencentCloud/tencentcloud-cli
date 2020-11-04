**Example 1: 创建TCP监听器**

创建TCP监听器

Input: 

```
tccli gaap CreateTCPListeners --cli-unfold-argument  \
    --ProxyId link-bjkpdum1\
    --ListenerName test1\
    --RealServerType IP\
    --Scheduler rr\
    --DelayLoop 20\
    --ConnectTimeout 20\
    --HealthCheck 1\
    --Ports 90
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

