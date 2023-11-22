**Example 1: 修改应用代理**

修改应用代理。

Input: 

```
tccli teo ModifyApplicationProxy --cli-unfold-argument  \
    --ZoneId zone-21xfqlh4qjee \
    --ProxyId proxy-537f5b41-162a-11ed-abaa-525400c5da15 \
    --ProxyName ssss \
    --ProxyType instance \
    --SessionPersistTime 3600 \
    --Ipv6.Switch on
```

Output: 
```
{
    "Response": {
        "RequestId": "b03fe5dd-be04-444c-a2e1-49f1bf2f399a"
    }
}
```

