**Example 1: 查询安全组关联的实例统计**

查询安全组关联的实例统计

Input: 

```
tccli vpc DescribeSecurityGroupAssociationStatistics --cli-unfold-argument  \
    --SecurityGroupIds sg-2quou3gv sg-ohuuioma
```

Output: 
```
{
    "Response": {
        "RequestId": "f23d1450-ed00-4442-98d4-be409e625e6c",
        "SecurityGroupAssociationStatisticsSet": [
            {
                "InstanceStatistics": [
                    {
                        "InstanceCount": 1,
                        "InstanceType": "CVM"
                    }
                ],
                "CDB": 1,
                "ENI": 1,
                "SecurityGroupId": "sg-ohuuioma",
                "CLB": 1,
                "TotalCount": 1,
                "CVM": 1,
                "SG": 1
            },
            {
                "InstanceStatistics": [
                    {
                        "InstanceCount": 1,
                        "InstanceType": "CVM"
                    }
                ],
                "CDB": 1,
                "ENI": 1,
                "SecurityGroupId": "sg-2quou3gv",
                "CLB": 1,
                "TotalCount": 1,
                "CVM": 1,
                "SG": 1
            }
        ]
    }
}
```

