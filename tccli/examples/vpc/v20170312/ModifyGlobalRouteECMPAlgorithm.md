**Example 1: 修改IPv4全局路由ECMP的HASH算法**

修改IPv4全局路由ECMP的HASH算法

Input: 

```
tccli vpc ModifyGlobalRouteECMPAlgorithm --cli-unfold-argument  \
    --VpcId vpc-mcqaoy0f \
    --DestinationCidrBlock 192.168.0.0/20 \
    --SubnetRouteAlgorithm ECMP_DESTINATION_IP_HASH
```

Output: 
```
{
    "Response": {
        "RequestId": "78adae2b-1200-4f78-9cc6-f88f452510d3"
    }
}
```

