**Example 1: Creating an HTTP Listener**

Create an HTTP listener.

Input: 

```
tccli gaap CreateHTTPListener --cli-unfold-argument  \
    --ProxyId link-cuxw2rm0\
    --ListenerName listener-1\
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

