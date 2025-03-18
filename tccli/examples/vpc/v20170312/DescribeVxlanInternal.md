**Example 1: 查询子机的VXLAN信息。**

查询子机的VXLAN信息。

Input: 

```
tccli vpc DescribeVxlanInternal --cli-unfold-argument  \
    --VpcId 80203 \
    --Owner 251224754 \
    --Ip 10.0.16.4
```

Output: 
```
{
    "Response": {
        "RequestId": "029ade9b-d9cc-4a1e-bd9c-a6d17e11e480",
        "Total": 1,
        "VpcVxlanSet": [
            {
                "CreateTime": "2024-12-23 17:30:49",
                "Ip": "10.0.16.4",
                "Owner": "251224754",
                "UniqueVpcId": "vpc-mcqaoy0f",
                "VpcId": 80203,
                "VpcVxlanId": 6
            }
        ]
    }
}
```

