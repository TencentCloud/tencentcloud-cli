**Example 1: 修改TCP监听器配置**



Input: 

```
tccli gaap ModifyTCPListenerAttribute --cli-unfold-argument  \
    --ListenerId listener-a8oko9dl \
    --ProxyId link-p9888rix \
    --ConnectTimeout 5
```

Output: 
```
{
    "Response": {
        "RequestId": "334f0ea4-eee7-48df-b97b-185417e9a5b6"
    }
}
```

