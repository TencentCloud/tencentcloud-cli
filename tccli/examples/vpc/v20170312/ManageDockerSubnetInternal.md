**Example 1: Docker子网管理**



Input: 

```
tccli vpc ManageDockerSubnetInternal --cli-unfold-argument  \
    --VpcId vpc-ewdc1236 \
    --Subnet 10.0.0.1 \
    --IntMask 16 \
    --ManageType CREATE
```

Output: 
```
{
    "Response": {
        "RequestId": "404428db-f850-40c2-803d-0aae49aba43a"
    }
}
```

