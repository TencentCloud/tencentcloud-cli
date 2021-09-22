**Example 1: 查询策略详情接口**

根据策略id查询该策略的详情

Input: 

```
tccli cwp DescribeBaselineStrategyDetail --cli-unfold-argument  \
    --StrategyId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "PassRate": 50,
        "StrategyName": "等保一级策略",
        "ScanCycle": 1,
        "ScanAt": "00:00:00",
        "IsGlobal": 1,
        "IfScanned": 1,
        "MachineType": "cvm",
        "Region": "ap-bj",
        "Quuids": [
            "2001",
            "2002",
            "2003"
        ],
        "CategoryIds": [
            1,
            2,
            3
        ]
    }
}
```

