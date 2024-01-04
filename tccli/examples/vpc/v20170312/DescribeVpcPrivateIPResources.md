**Example 1: 查询内网IP地址对应的实例ID**

查询内网IP地址对应的实例ID

Input: 

```
tccli vpc DescribeVpcPrivateIPResources --cli-unfold-argument  \
    --Filters.0.Name private-ip-address \
    --Filters.0.Values 10.0.5.251
```

Output: 
```
{
    "Response": {
        "VpcPrivateIPResourceSet": [
            {
                "PrivateIPAddress": "10.0.5.251",
                "ResourceId": "",
                "Region": "ap-qingyuan",
                "ResourceType": "Unknown"
            }
        ],
        "RequestId": "9088eb5b-53f1-4178-b510-83f6a071d26e",
        "TotalCount": 1
    }
}
```

