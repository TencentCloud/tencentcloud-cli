**Example 1: 查询RDMA地址池网段**

查询RDMA地址池网段

Input: 

```
tccli ihn DescribeRdmaIpPoolSubnet --cli-unfold-argument  \
    --ModuleId 818181 \
    --Offset 0 \
    --Limit 9
```

Output: 
```
{
    "Response": {
        "RdmaIpPoolSubnets": [
            {
                "CreateTime": "2025-02-21 17:37:36",
                "IntMask": 16,
                "ModuleId": 818181,
                "Subnet": "91.91.0.0"
            }
        ],
        "TotalCount": 1,
        "RequestId": "41f57646-729b-4130-8a42-fe9d85dd0950"
    }
}
```

