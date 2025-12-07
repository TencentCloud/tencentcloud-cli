**Example 1: 查询apm业务系统与其他产品的关联关系**

查询apm业务系统与其他产品的关联关系

Input: 

```
tccli apm DescribeApmAssociation --cli-unfold-argument  \
    --ProductName Prometheus \
    --InstanceId apm-059oXBfTL
```

Output: 
```
{
    "Response": {
        "ApmAssociation": {
            "PeerId": "",
            "Status": 2
        },
        "RequestId": "fac525bd-27a5-4411-b226-70e7d0a5529f"
    }
}
```

