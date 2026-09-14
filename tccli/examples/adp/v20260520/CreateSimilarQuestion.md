**Example 1: 创建相似问生成任务**

创建相似问生成任务

Input: 

```
tccli adp CreateSimilarQuestion --cli-unfold-argument  \
    --KbId 2097333005876517504 \
    --Question 智阅Air14轻薄笔记本电脑的价格是多少？ \
    --Answer 智阅Air14轻薄笔记本电脑的价格为¥4123。
```

Output: 
```
{
    "Response": {
        "QuestionList": [
            "智阅Air14轻薄本多少钱"
        ],
        "RequestId": "9e5d32ed-ddc0-437e-85c1-3cc91389bb11"
    }
}
```

