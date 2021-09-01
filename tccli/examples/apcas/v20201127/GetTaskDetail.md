**Example 1: 查询画像洞察任务详情**



Input: 

```
tccli apcas GetTaskDetail --cli-unfold-argument  \
    --Id 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "TaskDetailDataList": [
            {
                "TagId": 1,
                "TagDesc": "xx",
                "LabelDetailDataList": [
                    {
                        "Value": {
                            "Tgi": 0.0,
                            "Proportion": 0.0,
                            "Market": 0.0
                        },
                        "Label": "xx"
                    }
                ]
            }
        ]
    }
}
```

