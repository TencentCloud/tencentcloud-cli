**Example 1: 查询策略列表**



Input: 

```
tccli fwm DescribeStrategies --cli-unfold-argument  \
    --Product cfw_edge_acl \
    --ExecArea pre
```

Output: 
```
{
    "Response": {
        "Strategies": [
            {
                "CreateBy": "700000363112",
                "CreateName": "cfw-test",
                "CreateTime": "2026-10-28 14:44:49",
                "ErrMsg": "",
                "ErrorType": "",
                "ExecArea": "pre",
                "GroupId": "fwmrg-bds51sjghb",
                "GroupName": "不影响云防测试rename",
                "Product": "cfw_edge_acl",
                "ReceiveAccount": [
                    {
                        "Nickname": "cfw计费测试",
                        "ReceiverType": 0,
                        "Uin": "100014712605"
                    }
                ],
                "RuleCount": 5,
                "RuleStatus": 4,
                "Sequence": 1,
                "StrategyId": "fwms-x8cvhqlj",
                "UpdateBy": "700000363112",
                "UpdateName": "cfw-test",
                "UpdateTime": "2026-10-28 15:38:01"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e994c8c1-78f3-4a63-b855-8c4b3dd3d963"
    }
}
```

