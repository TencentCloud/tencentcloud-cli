**Example 1: 修改实例网络**



Input: 

```
tccli sqlserver ModifyDBInstanceNetwork --cli-unfold-argument  \
    --InstanceId mssql-p2yli7gv \
    --NewVpcId vpc-ilki4qdp \
    --NewSubnetId subnet-lru6dhh8 \
    --OldIpRetainTime 12
```

Output: 
```
{
    "Response": {
        "RequestId": "20db6661-2a85-49d9-8a37-976b931649fb",
        "FlowId": 100125
    }
}
```

