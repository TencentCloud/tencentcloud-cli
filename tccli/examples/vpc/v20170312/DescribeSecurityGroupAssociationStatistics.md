**Example 1: 查询安全组关联的实例统计**



Input: 

```
tccli vpc DescribeSecurityGroupAssociationStatistics --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupIds sg-ohuuioma sg-2quou3gv
```

Output: 
```
{
    "Response": {
        "SecurityGroupAssociationStatisticsSet": [
            {
                "SecurityGroupId": "sg-2quou3gv",
                "CDB": 0,
                "CVM": 0,
                "ENI": 0,
                "SG": 0,
                "CLB": 0,
                "TotalCount": 0
            },
            {
                "SecurityGroupId": "sg-05bb4upy",
                "CDB": 0,
                "CVM": 1,
                "ENI": 1,
                "SG": 2,
                "CLB": 1,
                "TotalCount": 3
            }
        ]
    }
}
```

