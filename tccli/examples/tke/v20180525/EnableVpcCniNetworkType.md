**Example 1: 启用vpc-cni网络**



Input: 

```
tccli tke EnableVpcCniNetworkType --cli-unfold-argument  \
    --ClusterId xx \
    --EnableStaticIp False \
    --VpcCniType tke-route-eni \
    --Subnets xxx yyy
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

