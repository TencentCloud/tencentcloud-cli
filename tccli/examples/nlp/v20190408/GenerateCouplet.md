**Example 1: 智能春联调用示例**



Input: 

```
tccli nlp GenerateCouplet --cli-unfold-argument  \
    --Text 小鸡 \
    --TargetType 0
```

Output: 
```
{
    "Response": {
        "TopScroll": "满园春色",
        "Content": [
            "小龙昂首开新局",
            "鸡犬登楼展宏图"
        ],
        "RandomCause": "",
        "RequestId": "9a7a1615-3e09-4db2-8032-5c6f497f7e6a"
    }
}
```

