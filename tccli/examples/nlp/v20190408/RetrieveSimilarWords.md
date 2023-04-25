**Example 1: 相似词召回调用示例**

相似词召回

Input: 

```
tccli nlp RetrieveSimilarWords --cli-unfold-argument  \
    --Text 林丹 \
    --Number 10
```

Output: 
```
{
    "Response": {
        "RequestId": "e246e84f-de88-46d0-b5dd-68ff94db40ad",
        "WordList": [
            "李宗伟",
            "桃田贤斗",
            "马龙",
            "纳达尔",
            "刘翔",
            "张本智和",
            "费德勒",
            "孙杨",
            "宁泽涛",
            "朱婷"
        ]
    }
}
```

