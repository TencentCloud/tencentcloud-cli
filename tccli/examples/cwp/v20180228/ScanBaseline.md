**Example 1: 基线检测接口**

进行基线检测或重新检测的接口

Input: 

```
tccli cwp ScanBaseline --cli-unfold-argument  \
    --StrategyIdList 1 2 3 \
    --CategoryIdList 0 1 2 \
    --RuleIdList 1 2 3 \
    --QuuidList "aaa" "bbb"
```

Output: 
```
{
    "Response": {
        "RequestId": "req-566234234",
        "ScanningQuuids": [
            "Quuid1",
            "Quuid2"
        ],
        "TaskId": 120
    }
}
```

