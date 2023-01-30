**Example 1: 列出 Grafana 环境变量**

列出 Grafana 环境变量

Input: 

```
tccli monitor DescribeGrafanaEnvironments --cli-unfold-argument  \
    --InstanceId grafana-abcdefgh
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Envs": "{}"
    }
}
```

