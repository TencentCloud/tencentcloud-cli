**Example 1: 儿童闲聊示例**



Input: 

```
tccli nlp ChatBot --cli-unfold-argument  \
    --Flag 1\
    --OpenId no23391003\
    --Query 给我讲个故事可以
```

Output: 
```
{
    "Response": {
        "Reply": "宝贝，最近好多小朋友都在听下面这些故事呢",
        "Confidence": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 通用闲聊示例**



Input: 

```
tccli nlp ChatBot --cli-unfold-argument  \
    --Flag 0\
    --Query 我要买股票
```

Output: 
```
{
    "Response": {
        "Reply": "股市有风险，入市须谨慎",
        "Confidence": 0.8,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

