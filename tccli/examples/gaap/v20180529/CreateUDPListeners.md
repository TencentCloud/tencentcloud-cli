**Example 1: Creating an UDP Listener**

Create an UDP listener.

Input: 

```
tccli gaap CreateUDPListeners --cli-unfold-argument  \
    --ProxyId link-bjkpdum1 \
    --ListenerName test1 \
    --RealServerType IP \
    --Scheduler rr \
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

