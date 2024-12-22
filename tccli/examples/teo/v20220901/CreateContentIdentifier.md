**Example 1: 创建内容标识符**

创建内容标识符，同时绑定标签。

Input: 

```
tccli teo CreateContentIdentifier --cli-unfold-argument  \
    --Tags.0.TagKey test \
    --Tags.0.TagValue abc \
    --PlanId edgeone-37q0w7qali10 \
    --Description content-test
```

Output: 
```
{
    "Response": {
        "ContentId": "eocontent-27q0p1bali16",
        "RequestId": "3c140219-cff9-470e-b241-907877d6fb03"
    }
}
```

