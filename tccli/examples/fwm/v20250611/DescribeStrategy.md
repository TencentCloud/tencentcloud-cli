**Example 1: 查询策略详情**



Input: 

```
tccli fwm DescribeStrategy --cli-unfold-argument  \
    --StrategyId fwms-x8cvhqlj
```

Output: 
```
{
    "Response": {
        "Strategy": {
            "CreateBy": "700000363112",
            "CreateName": "cfw-test",
            "CreateTime": "2026-10-28 14:44:49",
            "ErrMsg": "",
            "ErrorType": "",
            "ExecArea": "pre",
            "GroupId": "fwmrg-bds51sjghb",
            "GroupName": "不影响云防测试rename",
            "Product": "cfw_edge_acl",
            "ReceiveAccount": [],
            "RuleCount": 5,
            "RuleStatus": 4,
            "Sequence": 1,
            "StrategyId": "fwms-x8cvhqlj",
            "UpdateBy": "700000363112",
            "UpdateName": "cfw-test",
            "UpdateTime": "2026-10-28 15:38:01"
        },
        "RequestId": "9cc25e15-e146-46d5-b860-df7828aae7c0"
    }
}
```

