**Example 1: 创建 Grafana 实例**

创建Grafana实例

Input: 

```
tccli monitor CreateGrafanaInstance --cli-unfold-argument  \
    --SubnetIds subnet-123 \
    --VpcId vpc-123 \
    --InstanceName my-instance \
    --GrafanaInitPassword sfduyxoewqx \
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

**Example 2: 创建 Grafana 实例无支付权限**

子用户没有支付权限时，调用接口会报错 CamNoAuth

Input: 

```
tccli monitor CreateGrafanaInstance --cli-unfold-argument  \
    --SubnetIds subnet-123 \
    --VpcId vpc-123 \
    --InstanceName my-instance \
    --GrafanaInitPassword sfduyxoewqx \
    --EnableInternet True
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "UnauthorizedOperation.CamNoAuth",
            "Message": "uin: no pay auth for ownerUin:"
        },
        "RequestId": "fpllngzieyoh54e1244ols7k2hh3gdny"
    }
}
```

