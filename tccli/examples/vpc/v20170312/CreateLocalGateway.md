**Example 1: 创建本地网关**

创建本地网关

Input: 

```
tccli vpc CreateLocalGateway --cli-unfold-argument  \
    --CdcId cluster-1234dert \
    --VpcId vpc-m0c2kcun \
    --LocalGatewayName TEST
```

Output: 
```
{
    "Response": {
        "LocalGateway": {
            "CdcId": "cluster-1234dert",
            "VpcId": "vpc-m0c2kcun",
            "UniqLocalGwId": "lgw-1234edfr",
            "LocalGatewayName": "TEST",
            "LocalGwIp": "10.0.0.0",
            "CreateTime": "2021-03-24 15:31:56"
        },
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

