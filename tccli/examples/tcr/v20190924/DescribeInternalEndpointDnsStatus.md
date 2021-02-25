**Example 1: 查询私有域名解析状态**



Input: 

```
tccli tcr DescribeInternalEndpointDnsStatus --cli-unfold-argument  \
    --VpcSet.0.InstanceId tcr-xxx \
    --VpcSet.0.VpcId vpc-xxx \
    --VpcSet.0.EniLBIp 1.1.1.1 \
    --VpcSet.0.UsePublicDomain true
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "VpcSet": [
            {
                "Region": "ap-guangzhou",
                "VpcId": "vpc-xxx",
                "Status": "ENABLED"
            }
        ]
    }
}
```

