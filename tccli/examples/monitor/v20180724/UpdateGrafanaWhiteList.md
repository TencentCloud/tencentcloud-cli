**Example 1: 更新 Grafana 白名单**

更新 Grafana 白名单

Input: 

```
tccli monitor UpdateGrafanaWhiteList --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh \
    --Whitelist 127.0.0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny"
    }
}
```

