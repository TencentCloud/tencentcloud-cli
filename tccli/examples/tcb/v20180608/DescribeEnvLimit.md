**Example 1: 查询环境个数上限接口**



Input: 

```
tccli tcb DescribeEnvLimit --cli-unfold-argument  \
    --Source sss
```

Output: 
```
{
    "Response": {
        "CurrentFreeEnvNum": 0,
        "ChangePayTotal": 0,
        "CurrentChangePayMonthly": 0,
        "MaxDeleteMonthly": 0,
        "MaxEnvNum": 0,
        "ChangePayMonthly": 0,
        "CurrentChangePayTotal": 0,
        "MaxDeleteTotal": 0,
        "CurrentEnvNum": 0,
        "CurrentDeleteMonthly": 0,
        "CurrentDeleteTotal": 0,
        "CurrentFreeTrialNum": 0,
        "MaxFreeTrialNum": 0,
        "MaxFreeEnvNum": 0,
        "RequestId": "xx"
    }
}
```

