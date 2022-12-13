**Example 1: 更新 Grafana 的 DNS 配置**

更新 Grafana 的 DNS 配置

Input: 

```
tccli monitor UpdateDNSConfig --cli-unfold-argument  \
    --InstanceId grafana-12345678 \
    --NameServers xx
```

Output: 
```
{
    "Response": {
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny"
    }
}
```

