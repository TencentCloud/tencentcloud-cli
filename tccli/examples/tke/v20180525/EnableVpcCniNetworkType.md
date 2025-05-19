**Example 1: 启用vpc-cni网络**

TKE 集群启用 vpc-cni 网络

Input: 

```
tccli tke EnableVpcCniNetworkType --cli-unfold-argument  \
    --ClusterId cls-e55paxnt \
    --EnableStaticIp False \
    --VpcCniType tke-route-eni \
    --Subnets subnet-e55paxnt subnet-e55paxnt
```

Output: 
```
{
    "Response": {
        "RequestId": "defc0237-d413-4079-9faa-7f3ff928d224"
    }
}
```

