**Example 1: 获取终端用户新增与登录信息**



Input: 

```
tccli tcb DescribeEndUserLoginStatistic --cli-unfold-argument  \
    --EnvId envid
```

Output: 
```
{
    "Response": {
        "LoginStatistics": [
            {
                "StatisticalType": "NEWUSER",
                "StatisticalCycle": "DAY",
                "Count": 9900,
                "UpdateTime": "2020-02-02 20:13:14"
            },
            {
                "StatisticalType": "LOGIN",
                "StatisticalCycle": "MONTH",
                "Count": 9900,
                "UpdateTime": "2020-02-02 20:13:14"
            }
        ],
        "RequestId": "046cacfd-af90-4355-ac92-f56954bd1831"
    }
}
```

