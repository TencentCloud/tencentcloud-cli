**Example 1: 获取信息提取嵌入链接**



Input: 

```
tccli ess DescribeInformationExtractionWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3o2xYIKo7 \
    --TaskId yDwqxj1FlhYIKo7
```

Output: 
```
{
    "Response": {
        "RequestId": "s1757576271425719631",
        "Url": "https://embed.test.qian.tencent.cn/ai-contract-info-extract-embed?embed=1&code=xx&channel=TENCENTCLOUD&embedType=CONTRACT_EXTRACTION&shortKey=xx"
    }
}
```

