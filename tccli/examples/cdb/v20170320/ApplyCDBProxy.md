**Example 1: 创建数据库代理**



Input: 

```
tccli cdb ApplyCDBProxy --cli-unfold-argument  \
    --UniqVpcId xx \
    --InstanceId xx \
    --SecurityGroup xx \
    --Mem 1 \
    --UniqSubnetId xx \
    --Desc xx \
    --Cpu 1 \
    --ProxyCount 1
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "dd803e8b-02543d6b-0b6ec9c4-8c1e133c",
        "RequestId": "6236a2ad-0557-48c3-b983-247d2870e0a1"
    }
}
```

