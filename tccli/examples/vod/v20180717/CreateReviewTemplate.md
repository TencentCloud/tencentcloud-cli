**Example 1: 创建开启检测多项违规标签的审核模板**

开启涉黄、涉暴、广告检测。

Input: 

```
tccli vod CreateReviewTemplate --cli-unfold-argument  \
    --Name test \
    --Comment 开启涉黄、涉暴、广告检测 \
    --Labels Porn Terror Ad
```

Output: 
```
{
    "Response": {
        "Definition": 20123,
        "RequestId": "88aee3e9-2qd3-4151-9d4b-4390a45228a9"
    }
}
```

