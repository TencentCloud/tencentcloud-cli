**Example 1: 调用成功**

基于账号成功查询到到相关的任务信息列表

Input: 

```
tccli msp DescribeSurveyTasks --cli-unfold-argument  \
    --Account divewang
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CompleteTime": "",
                "JobSrc": "在线调研",
                "JobStatus": "调研完成",
                "PlanID": "plan-lhgqFY2z",
                "PlanName": "dive-dev-0408-1",
                "StartTime": "2024-04-08 11:40:28"
            }
        ],
        "RequestId": "316d5b44-a445-45be-b91e-d9bc1939f27c",
        "Total": 1
    }
}
```

**Example 2: 无匹配信息**

无匹配信息总数返回0

Input: 

```
tccli msp DescribeSurveyTasks --cli-unfold-argument  \
    --Account janicejzhu
```

Output: 
```
{
    "Response": {
        "Data": null,
        "RequestId": "66049915-6cce-4405-84ec-fc1e47b4c7cc",
        "Total": 0
    }
}
```

