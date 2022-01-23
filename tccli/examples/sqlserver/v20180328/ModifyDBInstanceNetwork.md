**Example 1: 修改实例网络**



Input: 

```
tccli sqlserver ModifyDBInstanceNetwork --cli-unfold-argument  \
    --InstanceId mssql-p2yli7gv \
    --NewVpcId vpc-ilki4qdp \
    --NewSubnetId subnet-lru6dhh8 \
    --Vip 127.0.0.1 \
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

**Example 2: 转网**



Input: 

```
tccli sqlserver ModifyDBInstanceNetwork --cli-unfold-argument  \
    --InstanceId mssql-e720ieef \
    --NewVpcId vpc-kw88teud \
    --NewSubnetId subnet-8z5n8tcg \
    --OldIpRetainTime 0
```

Output: 
```
{
    "Response": {
        "FlowId": 1011581,
        "RequestId": "bdac237c-b9b7-4050-9284-97898cca5883"
    }
}
```

