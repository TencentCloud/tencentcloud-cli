**Example 1: Deleting a Listener**

Delete a listener.

Input: 

```
tccli gaap DeleteListeners --cli-unfold-argument  \
    --ProxyId link-3d85gh \
    --ListenerIds listener-o0f3at99 \
    --Force 1
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

