**Example 1: 查询本地网关**

查询本地网关

Input: 

```
tccli vpc DescribeLocalGateway --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LocalGatewaySet": [
            {
                "CdcId": "cluster-1234dert",
                "VpcId": "vpc-m0c2kcun",
                "UniqLocalGwId": "lgw-1234edfr",
                "LocalGatewayName": "TEST",
                "LocalGwIp": "10.0.0.0",
                "CreateTime": "2021-03-24 15:31:56"
            }
        ],
        "TotalCount": 1,
        "RequestId": "74883e1b-5901-46de-ae1e-d6e2cf591c5b"
    }
}
```

