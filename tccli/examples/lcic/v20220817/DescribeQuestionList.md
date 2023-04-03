**Example 1: 示例**

获取房间问答提问列表

Input: 

```
tccli lcic DescribeQuestionList --cli-unfold-argument  \
    --RoomId 382651668 \
    --Page 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "QuestionInfo": [
            {
                "AnswerStats": [
                    {
                        "Answer": 1,
                        "Count": 0
                    },
                    {
                        "Answer": 2,
                        "Count": 1
                    },
                    {
                        "Answer": 4,
                        "Count": 0
                    },
                    {
                        "Answer": 8,
                        "Count": 1
                    },
                    {
                        "Answer": 16,
                        "Count": 0
                    }
                ],
                "CorrectAnswer": 8,
                "Duration": 0,
                "QuestionContent": "测试内容",
                "QuestionId": "7bd1e2cf-4291-447e-bd9d-123007abcf9a"
            }
        ],
        "RequestId": "2b0b1930-c032-4b8b-b4da-33a333da78d1",
        "Total": 2
    }
}
```

