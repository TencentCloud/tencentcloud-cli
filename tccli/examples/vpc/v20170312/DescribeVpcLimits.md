**Example 1: 获取私有网络配额**

获取私有网络配额

Input: 

```
tccli vpc DescribeVpcLimits --cli-unfold-argument  \
    --LimitTypes appid-max-vpcs
```

Output: 
```
{
    "Response": {
        "VpcLimitSet": [
            {
                "LimitType": "appid-max-vpcs",
                "LimitValue": 5
            }
        ],
        "RequestId": "5cf1a813-d4f8-4e0c-8f90-c155a84a3ea1"
    }
}
```

