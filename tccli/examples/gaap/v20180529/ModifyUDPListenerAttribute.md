**Example 1: 修改UDP监听器配置**

修改UDP监听器配置

Input: 

```
tccli gaap ModifyUDPListenerAttribute --cli-unfold-argument  \
    --ProxyId link-bjkpdum1 \
    --ListenerId listener-o0f3at99 \
    --Scheduler rr \
    --ListenerName test10
```

Output: 
```
{
    "Response": {
        "RequestId": "3919ba30-85c4-4cb4-81bf-ff243b50f3dc"
    }
}
```

