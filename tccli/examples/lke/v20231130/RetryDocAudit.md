**Example 1: 文档审核重试**

文档审核重试

Input: 

```
tccli lke RetryDocAudit --cli-unfold-argument  \
    --LoginUin abc \
    --LoginSubAccountUin abc \
    --BotBizId abc \
    --DocBizId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

