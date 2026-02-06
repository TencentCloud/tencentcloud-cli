**Example 1: 创建HTTP监听器**



Input: 

```
tccli gaap CreateHTTPListener --cli-unfold-argument  \
    --ListenerName listener-name \
    --Port 8091 \
    --ProxyId link-p9888rix
```

Output: 
```
{
    "Response": {
        "ListenerId": "listener-9vub5ymx",
        "RequestId": "788e2374-283f-4aaa-ab74-49042e84383e"
    }
}
```

