**Example 1: 修改实例公网配置**

修改实例公网配置

Input: 

```
tccli trocket ModifyInstanceEndpoint --cli-unfold-argument  \
    --InstanceId rmq-cdrgxq94om \
    --Type PUBLIC \
    --Bandwidth 2 \
    --IpRules.0.Ip 1.2.3.4 \
    --IpRules.0.Allow True \
    --IpRules.0.Remark test remark
```

Output: 
```
{
    "Response": {
        "RequestId": "999bc587-90d9-4ec2-97e3-3ef170e1da96"
    }
}
```

