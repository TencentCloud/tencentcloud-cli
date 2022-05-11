**Example 1: 查询推送资源任务统计信息**



Input: 

```
tccli iotcloud DescribePushResourceTaskStatistics --cli-unfold-argument  \
    --ProductID O4CCMMZE3A \
    --Name 1.0
```

Output: 
```
{
    "Response": {
        "SuccessTotal": 1,
        "FailureTotal": 0,
        "UpgradingTotal": 1,
        "RequestId": "968ac21f-815f-4f32-852f-c0729c40e724"
    }
}
```

