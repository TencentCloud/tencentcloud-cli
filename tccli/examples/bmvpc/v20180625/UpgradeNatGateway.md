**Example 1: 升级NAT网关**



Input: 

```
tccli bmvpc UpgradeNatGateway --cli-unfold-argument  \
    --NatId nat-1tw1oc0t \
    --VpcId vpc-mi51u7gs \
    --MaxConcurrent 3000000
```

Output: 
```
{
    "Response": {
        "TaskId": 18411,
        "RequestId": "b38f56e9-4830-486f-a596-fb425f9e6e6b"
    }
}
```

