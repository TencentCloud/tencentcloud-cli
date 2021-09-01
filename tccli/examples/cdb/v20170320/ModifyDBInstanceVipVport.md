**Example 1: 修改云数据库实例的IP和端口号**



Input: 

```
tccli cdb ModifyDBInstanceVipVport --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj \
    --DstIp 10.0.1.1 \
    --DstPort 1025 \
    --UniqVpcId 11357 \
    --UniqSubnetId 23789 \
    --ReleaseDuration 12
```

Output: 
```
{
    "Response": {
        "RequestId": "6EF60BEC-0242-43AF-BB20-270359FB54A7",
        "AsyncRequestId": "d2baf2fb-cbae62df-7dd0d736-9cbd3e31"
    }
}
```

