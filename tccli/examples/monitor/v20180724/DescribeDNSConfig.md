**Example 1: 列出实例的 DNS 配置**

列出实例的 DNS 配置

Input: 

```
tccli monitor DescribeDNSConfig --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny",
        "NameServers": [
            "114.114.114.114"
        ]
    }
}
```

