**Example 1: 速算题目批改**

传入速算图像url，返回批改结果

Input: 

```
tccli hcm Evaluation --cli-unfold-argument  \
    --SessionId s_1596611058609_2868392 \
    --Url xxx
```

Output: 
```
{
    "Response": {
        "SessionId": "s_1596611058609_2868392",
        "Items": [
            {
                "Item": "YES",
                "ItemString": "600*5=6*500",
                "ItemConf": 0,
                "ItemCoord": {
                    "Height": 130,
                    "Width": 531,
                    "X": 1135,
                    "Y": 953
                },
                "Answer": "",
                "ExpressionType": "1",
                "QuestionId": ""
            },
            {
                "Item": "YES",
                "ItemString": "4厘米=(40)毫米",
                "ItemConf": 0,
                "ItemCoord": {
                    "Height": 125,
                    "Width": 579,
                    "X": 1489,
                    "Y": 800
                },
                "Answer": "",
                "ExpressionType": "7",
                "QuestionId": ""
            }
        ],
        "RequestId": "17c1a0ba-0b66-4b28-892f-f248dcc5f548"
    }
}
```

