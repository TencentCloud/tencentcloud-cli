**Example 1: 删除子机的VXLAN信息。**

删除子机的VXLAN信息。

Input: 

```
tccli vpc DeleteVxlanInternal --cli-unfold-argument  \
    --VpcVxlanRequestSet.0.VpcId 80203 \
    --VpcVxlanRequestSet.0.Owner 251224754 \
    --VpcVxlanRequestSet.0.Ip 10.0.16.4
```

Output: 
```
{
    "Response": {
        "RequestId": "63f90488-d1c4-4697-b38a-114a8f5eae48",
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

