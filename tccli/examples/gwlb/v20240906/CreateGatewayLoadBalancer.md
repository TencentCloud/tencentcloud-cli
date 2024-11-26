**Example 1: 创建一个网关负载均衡实例**

在私有网络中创建一个网关负载均衡

Input: 

```
tccli gwlb CreateGatewayLoadBalancer --cli-unfold-argument  \
    --VpcId vpc-30xq**** \
    --SubnetId subnet-**** \
    --LoadBalancerName the_name_of_gwlb
```

Output: 
```
{
    "Response": {
        "LoadBalancerIds": [
            "gwlb-kmfr****"
        ],
        "DealName": "20211230660009761735781",
        "RequestId": "7ffa6830-cd1b-4bc4-8e24-1688885f594a"
    }
}
```

