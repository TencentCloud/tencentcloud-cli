**Example 1: 查询灾备同步任务校验结果**



Input: 

```
tccli dts DescribeSyncCheckJob --cli-unfold-argument  \
    --JobId sync-blj8wnt1
```

Output: 
```
{
    "Response": {
        "Status": "finished",
        "ErrorCode": 0,
        "ErrorMessage": "灾备检查成功",
        "StepInfo": [
            {
                "StepNo": 1,
                "StepName": "检查参数",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 2,
                "StepName": "检查源实例",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 3,
                "StepName": "检查目标实例",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 4,
                "StepName": "检查实例状态",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 5,
                "StepName": "检查实例规格",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 6,
                "StepName": "检查实例版本",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 7,
                "StepName": "检查目标实例是否为空",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 8,
                "StepName": "检查是否开启加密",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 9,
                "StepName": "检查实例同步的库表信息",
                "StepCode": 0,
                "StepMessage": "校验成功"
            },
            {
                "StepNo": 10,
                "StepName": "检查实例冷备数据",
                "StepCode": 0,
                "StepMessage": "校验成功"
            }
        ],
        "CheckFlag": 1,
        "RequestId": "b3951c71-1da4-4b8f-9de5-ad71ab1e2917"
    }
}
```

