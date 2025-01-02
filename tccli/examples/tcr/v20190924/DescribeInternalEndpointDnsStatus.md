**Example 1: 查询私有域名解析状态**



Input: 

```
tccli tcr DescribeInternalEndpointDnsStatus --cli-unfold-argument  \
    --VpcSet.0.InstanceId tcr-dg284imq \
    --VpcSet.0.VpcId vpc-9iazgkcl \
    --VpcSet.0.EniLBIp 192.168.23.69 \
    --VpcSet.0.UsePublicDomain True \
    --VpcSet.0.RegionName ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "56dac6c5-10a3-44c9-86cd-9e9be56bf4dd",
        "VpcSet": [
            {
                "Region": "ap-guangzhou",
                "Status": "ENABLED",
                "VpcId": "vpc-9iazgkcl"
            }
        ]
    }
}
```

