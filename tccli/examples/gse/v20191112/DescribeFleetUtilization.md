**Example 1: 查询服务器舰队的利用率信息**

查询服务器舰队的利用率信息

Input: 

```
tccli gse DescribeFleetUtilization --cli-unfold-argument  \
    --FleetIds fleet-qp3g3caa-nkeekxw6
```

Output: 
```
{
    "Response": {
        "FleetUtilization": [
            {
                "ActiveGameServerSessionCount": 0,
                "ActiveServerProcessCount": 49,
                "CurrentPlayerSessionCount": 0,
                "FleetId": "fleet-qp3g3caa-8yh5e7kg",
                "MaximumPlayerSessionCount": 0
            }
        ],
        "RequestId": "d485c777-e1f6-4bfd-9e03-c4968f097692",
        "TotalCount": 1
    }
}
```

