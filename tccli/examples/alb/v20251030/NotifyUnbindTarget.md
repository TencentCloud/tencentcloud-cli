**Example 1: 通知负载均衡解绑后端服务**



Input: 

```
tccli alb NotifyUnbindTarget --cli-unfold-argument  \
    --Ips 192.168.0.1 \
    --NumericVpcId 143563231
```

Output: 
```
{
    "Response": {
        "RequestId": "3b848733-70e5-4558-ae39-4b9938eb7609"
    }
}
```

