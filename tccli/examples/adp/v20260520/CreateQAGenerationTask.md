**Example 1: 创建 QA 生成任务**

创建 QA 生成任务

Input: 

```
tccli adp CreateQAGenerationTask --cli-unfold-argument  \
    --DocIdList 2095352703294256640 \
    --KbId 2095346479588688512
```

Output: 
```
{
    "Response": {
        "TaskIdList": [
            "2097960333379110400"
        ],
        "RequestId": "b5ab552e-b852-44c7-b74b-80ca0a47cdc6"
    }
}
```

