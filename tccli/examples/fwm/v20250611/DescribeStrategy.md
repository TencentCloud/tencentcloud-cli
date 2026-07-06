**Example 1: 查询策略详情**



Input: 

```
tccli fwm DescribeStrategy --cli-unfold-argument  \
    --StrategyId fwms-kmbf8avt
```

Output: 
```
{
    "Response": {
        "RequestId": "209ce0d3-c47f-49b9-936c-c35aa2966910",
        "Strategy": {
            "CreateBy": "100011616646",
            "CreateName": "天空之蓝",
            "CreateTime": "2026-02-27 19:22:44",
            "ErrMsg": "",
            "ErrorType": "",
            "ExecArea": "pre",
            "GroupId": "fwmrg-5gxybcnr",
            "GroupName": "gl测试构造风险",
            "ReceiveAccount": [
                {
                    "Nickname": "天空之蓝",
                    "Uin": "100011616646"
                }
            ],
            "RuleCount": 11,
            "RuleStatus": 1,
            "Sequence": 1,
            "StrategyId": "fwms-kmbf8avt",
            "UpdateBy": "100011616646",
            "UpdateName": "天空之蓝",
            "UpdateTime": "2026-02-27 19:52:50"
        }
    }
}
```

