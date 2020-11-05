**Example 1: Binding Forwarding Rules to the Origin Server**

Bind forwarding rules to an origin server.

Input: 

```
tccli gaap BindRuleRealServers --cli-unfold-argument  \
    --RuleId 0\
    --RealServerBindSet.0.RealServerId rs-i3658cdf\
    --RealServerBindSet.0.RealServerPort 80\
    --RealServerBindSet.0.RealServerIP 1.1.1.1\
    --RealServerBindSet.0.RealServerWeight 1
```

Output: 
```
{
    "Response": {
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

