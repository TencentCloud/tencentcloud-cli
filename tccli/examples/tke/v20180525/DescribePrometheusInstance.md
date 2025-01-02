**Example 1: 查看托管prometheus实例详情**

查看托管prometheus实例详情

Input: 

```
tccli tke DescribePrometheusInstance --cli-unfold-argument  \
    --InstanceId prom-e55paxnt
```

Output: 
```
{
    "Response": {
        "QueryAddress": "http://10.0.0.1:9090",
        "VpcId": "vpc-e55paxnt",
        "Name": "tps-test",
        "InstanceId": "prom-e55paxnt",
        "COSBucket": "prometheus-prom-e55paxnt-data-qbc3zefo",
        "AlertManagerUrl": "",
        "Grafana": {
            "Domain": "",
            "Internet": "close",
            "Enabled": true,
            "AdminUser": "admin",
            "Address": "http://10.0.0.2"
        },
        "RequestId": "55054791-f4ff-4c33-afd2-dsahdjahdahada",
        "SubnetId": "subnet-dsadsada"
    }
}
```

