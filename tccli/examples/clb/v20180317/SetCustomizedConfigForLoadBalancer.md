**Example 1: 创建负载均衡维度的个性化配置**



Input: 

```
tccli clb SetCustomizedConfigForLoadBalancer --cli-unfold-argument  \
    --OperationType ADD \
    --ConfigContent 'client_max_body_size 222M;' \
    --ConfigName config_test
```

Output: 
```
{
    "Response": {
        "ConfigId": "pz-1234abcd",
        "RequestId": "83129908-a282-4f9f-8ab-131a3025ba22"
    }
}
```

