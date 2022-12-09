**Example 1: 列出 Grafana 白名单**

列出 Grafana 白名单

Input: 

```
tccli monitor DescribeGrafanaWhiteList --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny",
        "WhiteList": []
    }
}
```

