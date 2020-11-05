**Example 1: Modifying the HTTPS Listener Configuration**

Modify the HTTPS listener configuration.

Input: 

```
tccli gaap ModifyHTTPSListenerAttribute --cli-unfold-argument  \
    --InstanceId link-3d85gh\
    --ListenerId listener-o0f3at99\
    --ListenerName test-2\
    --ForwardProtocol HTTP
```

Output: 
```
{
    "Response": {
        "RequestId": "38fab584-8d14-4e2c-988c-4acdabbf2dff"
    }
}
```

