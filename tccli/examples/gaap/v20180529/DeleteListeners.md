**Example 1: 删除监听器**

删除监听器

Input: 

```
tccli gaap DeleteListeners --cli-unfold-argument  \
    --ProxyId link-3d85gh \
    --Force 1 \
    --ListenerIds listener-o0f3at99
```

Output: 
```
{
    "Response": {
        "OperationFailedListenerSet": [],
        "OperationSucceedListenerSet": [
            "listener-o0f3at99"
        ],
        "InvalidStatusListenerSet": [],
        "RequestId": "38fab584-8d14-4e2c-988c-4acdabbf2dff"
    }
}
```

