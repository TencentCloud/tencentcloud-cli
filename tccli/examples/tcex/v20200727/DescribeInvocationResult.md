**Example 1: 查询服务调用结果接口示例**



Input: 

```
tccli tcex DescribeInvocationResult --cli-unfold-argument  \
    --InvokeId e3163011-7b90-4971-b46b-2c8a5ebd9a21
```

Output: 
```
{
    "Response": {
        "RequestId": "e3163b11-7b90-4971-b46b-2c8a5ebd9a6g",
        "Status": 2,
        "Results": [
            {
                "AlgoId": "2",
                "AlgoName": "OCR手写体识别",
                "AlgoType": 3,
                "Error": "",
                "Result": "裙子和紧身衣，由于气候、风和太阳的影响，因而产生出最微妙的色调。假加穿上贵妇人的衣服，就会失去她特有的魅力。一个在地里穿着粗布衣服的农民,比他在礼拜天穿着节日盛装到教堂去更为真实。我以为，把一幅农民画画成老套光活的样子,同样是错误的。如果能在农画上闻到熏腊肉的烟味、煮士豆的蒸气味,那就好了,这不是不正常;只要闻到马棚里的味，很好，那正是一个马棚;如果用野上有一种成熟了的庄稼或土豆味，鱼肥或人造肥料的气味，那就是正常的，对城里人来说更是这样。"
            },
            {
                "AlgoId": "4",
                "AlgoName": "文本分类",
                "AlgoType": 3,
                "Error": "",
                "Result": "[{\"Class\":\"女性\",\"Confidence\":0.21}]"
            },
            {
                "AlgoId": "6",
                "AlgoName": "情感分析",
                "AlgoType": 3,
                "Error": "",
                "Result": "{\"Negative\":0.07756602,\"Neutral\":0,\"Positive\":0.922434}"
            }
        ]
    }
}
```

