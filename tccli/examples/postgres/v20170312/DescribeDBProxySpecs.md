**Example 1: 查询代理可售规格**

查询代理可售规格

Input: 

```
tccli postgres DescribeDBProxySpecs --cli-unfold-argument  \
    --DBInstanceId postgres-ronvpb2l
```

Output: 
```
{
    "Response": {
        "AvailableZones": [
            "ap-guangzhou-3"
        ],
        "SpecSet": [
            {
                "Cpu": 2,
                "MaxNodeNum": 4,
                "Memory": 4000,
                "MinNodeNum": 1
            }
        ],
        "SupportProxy": true,
        "RequestId": "b3ab22e5-de57-47ec-b98a-f55a76cf6d76"
    }
}
```

