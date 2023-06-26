**Example 1: 对联生成调用示例**

对联生成。

Input: 

```
tccli nlp ComposeCouplet --cli-unfold-argument  \
    --Text 阳光 \
    --TargetType 0
```

Output: 
```
{
    "Response": {
        "Content": [
            "阳春白雪江山秀",
            "光彩红梅岁月长"
        ],
        "RandomCause": "",
        "RequestId": "e9cc9a63-e2e9-4f92-a419-0fd8bf25cdf6",
        "TopScroll": "盛世新春"
    }
}
```

