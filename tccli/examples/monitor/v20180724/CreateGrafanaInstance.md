**Example 1: 创建 Grafana 实例**

创建Grafana实例

Input: 

```
tccli monitor CreateGrafanaInstance --cli-unfold-argument  \
    --SubnetIds subnet-123 \
    --VpcId vpc-123 \
    --InstanceName test \
    --GrafanaInitPassword test \
    --EnableInternet True
```

Output: 
```
{
    "Response": {
        "InstanceId": "grafana-c1enzs01",
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny"
    }
}
```

