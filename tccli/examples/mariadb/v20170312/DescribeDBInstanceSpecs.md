**Example 1: 查询云数据库可售卖规格**



Input: 

```
tccli mariadb DescribeDBInstanceSpecs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "694b99aa-d45e-485e-821b-e84ae16479c2",
        "Specs": [
            {
                "Machine": "TS85",
                "SpecInfos": [
                    {
                        "SuitInfo": "日独立用户数上百万人的中型应用",
                        "Pid": 10820,
                        "Machine": "TS85",
                        "MaxStorage": 3000,
                        "Memory": 64,
                        "Cpu": 1,
                        "NodeCount": 3,
                        "Qps": 33000,
                        "MinStorage": 10
                    }
                ]
            }
        ]
    }
}
```

