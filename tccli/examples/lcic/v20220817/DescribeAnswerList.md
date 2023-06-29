**Example 1: 示例**

示例

Input: 

```
tccli lcic DescribeAnswerList --cli-unfold-argument  \
    --QuestionId 69d2345d-0p80-7821-b3b7-cbfsdew \
    --Page 1 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "AnswerInfo": [
            {
                "Answer": 12,
                "CostTime": 10,
                "IsCorrect": 0,
                "Name": "zhangsan",
                "UserId": "2MANXmcVsYjgo9Bk00mvONkvekd"
            },
            {
                "Answer": 33,
                "CostTime": 6,
                "IsCorrect": 0,
                "Name": "lisi",
                "UserId": "2NP9SrTzakytuidv429i4rbNepD"
            }
        ],
        "RequestId": "8cc600da-b066-476a-a527-ee19c46f77f9",
        "Total": 2
    }
}
```

