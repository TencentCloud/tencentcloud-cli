**Example 1: 查询安全组关联的实例统计**



Input: 

```
tccli ecm DescribeSecurityGroupAssociationStatistics --cli-unfold-argument  \
    --SecurityGroupIds esg-ohuuioma esg-2quou3gv
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SecurityGroupAssociationStatisticsSet": [
            {
                "SecurityGroupId": "esg-ohuuioma",
                "ECM": 0,
                "Module": 1,
                "ENI": 0,
                "SG": 1,
                "CLB": 0,
                "TotalCount": 1
            },
            {
                "SecurityGroupId": "esg-2quou3gv",
                "ECM": 1,
                "Module": 1,
                "ENI": 0,
                "SG": 1,
                "CLB": 0,
                "TotalCount": 2
            }
        ]
    }
}
```

