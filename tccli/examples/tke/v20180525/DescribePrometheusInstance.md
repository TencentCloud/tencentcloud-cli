**Example 1: 查看托管prometheus实例详情**



Input: 

```
tccli tke DescribePrometheusInstance --cli-unfold-argument  \
    --InstanceId prom-xxx
```

Output: 
```
{
    "Response": {
        "QueryAddress": "xx",
        "VpcId": "xx",
        "Name": "xx",
        "InstanceId": "xx",
        "COSBucket": "xx",
        "AlertManagerUrl": "xx",
        "Grafana": {
            "Domain": "xx",
            "Internet": "xx",
            "Enabled": true,
            "AdminUser": "xx",
            "Address": "xx"
        },
        "RequestId": "xx",
        "SubnetId": "xx"
    }
}
```

