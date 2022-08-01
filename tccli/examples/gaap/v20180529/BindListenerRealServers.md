**Example 1: 监听器绑定源站**

监听器绑定源站

Input: 

```
tccli gaap BindListenerRealServers --cli-unfold-argument  \
    --RealServerBindSet.0.RealServerWeight 1 \
    --RealServerBindSet.0.RealServerId rs-04v3s12t \
    --RealServerBindSet.0.RealServerPort 80 \
    --RealServerBindSet.0.RealServerIP 119.28.69.101 \
    --RealServerBindSet.0.RealServerFailoverRole master \
    --ListenerId listener-pbsgn7ej
```

Output: 
```
{
    "Response": {
        "RequestId": "1f1e794d-a35e-41d2-8f40-fe32a2077329"
    }
}
```

