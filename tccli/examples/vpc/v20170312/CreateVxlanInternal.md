**Example 1: 添加子机的VXLAN信息。**

添加子机的VXLAN信息。

Input: 

```
tccli vpc CreateVxlanInternal --cli-unfold-argument  \
    --VpcVxlanRequestSet.0.VpcId 80203 \
    --VpcVxlanRequestSet.0.Owner 251224754 \
    --VpcVxlanRequestSet.0.Ip 10.0.16.4
```

Output: 
```
{
    "Response": {
        "RequestId": "6d0ccf2a-a8cf-406e-8dfa-9cbb73b74803",
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

