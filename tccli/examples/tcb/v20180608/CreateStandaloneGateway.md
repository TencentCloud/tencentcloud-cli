**Example 1: 创建独立网关**



Input: 

```
tccli tcb CreateStandaloneGateway --cli-unfold-argument  \
    --EnvId env-test-xxx \
    --GatewayAlias StandaloneGateway \
    --VpcId vpc-nzmimmod \
    --SubnetIds subnet-hpddq58c \
    --GatewayDesc gateway \
    --PackageVersion starter
```

Output: 
```
{
    "Response": {
        "GatewayName": "x-tcb-cbr-gateway-9eba9lc1daaf2e",
        "RequestId": "51a33e48-a808-4fe7-8c02-4e7be5245351"
    }
}
```

