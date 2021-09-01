**Example 1: 获取图像任务统计信息示例**

获取图像任务统计信息示例

Input: 

```
tccli tci DescribeImageTaskStatistic --cli-unfold-argument  \
    --JobId 336
```

Output: 
```
{
    "Response": {
        "RequestId": "fd59a73c-9ba3-4f7a-966c-68f20eaddeac",
        "JobId": 336,
        "Statistic": {
            "FaceIdentify": null,
            "FaceExpression": null,
            "FaceDetect": null,
            "Handtracking": null,
            "Gesture": null,
            "TeacherMovement": null,
            "StudentMovement": null,
            "Light": {
                "LightLevelRatio": null,
                "LightDistribution": [
                    {
                        "Time": 0,
                        "Value": 131
                    },
                    {
                        "Time": 0,
                        "Value": 131
                    },
                    {
                        "Time": 0,
                        "Value": 130
                    },
                    {
                        "Time": 0,
                        "Value": 130
                    },
                    {
                        "Time": 0,
                        "Value": 128
                    },
                    {
                        "Time": 0,
                        "Value": 130
                    },
                    {
                        "Time": 0,
                        "Value": 124
                    },
                    {
                        "Time": 0,
                        "Value": 132
                    },
                    {
                        "Time": 0,
                        "Value": 133
                    },
                    {
                        "Time": 0,
                        "Value": 134
                    }
                ]
            }
        }
    }
}
```

