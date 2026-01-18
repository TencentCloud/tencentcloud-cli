**Example 1: 监听器绑定源站**

监听器绑定源站

Input: 

```
tccli gaap BindListenerRealServers --cli-unfold-argument  \
    --ListenerId listener-a8lsmk4b \
    --RealServerBindSet.0.RealServerId rs-1008nt4p \
    --RealServerBindSet.0.RealServerPort 880 \
    --RealServerBindSet.0.RealServerIP 44.4.4.4
```

Output: 
```
{
    "Response": {
        "RequestId": "cea0b55a-6bcc-436a-9acf-a80a7f7c2bd6"
    }
}
```

