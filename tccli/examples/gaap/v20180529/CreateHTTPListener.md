**Example 1: 创建HTTP监听器**

创建HTTP监听器

Input: 

```
tccli gaap CreateHTTPListener --cli-unfold-argument  \
    --ProxyId link-cuxw2rm0 \
    --ListenerName listener-1 \
    --Port 443
```

Output: 
```
{
    "Response": {
        "RequestId": "9aeda369-17c7-429f-be39-745c1e92fc71",
        "ListenerId": "listener-o0f3at99"
    }
}
```

