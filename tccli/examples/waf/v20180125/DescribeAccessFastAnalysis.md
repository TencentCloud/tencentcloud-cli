**Example 1: 访问日志快速分析**



Input: 

```
tccli waf DescribeAccessFastAnalysis --cli-unfold-argument  \
    --TopicId 1ae37c76-df99-4e2b-998c-20f39eba6226 \
    --From 1625395948532 \
    --To 1626000748532 \
    --Query * \
    --FieldName host
```

Output: 
```
{
    "Response": {
        "RequestId": "9b02bf9e-c89c-42c3-9ae1-685f968fa02d"
    }
}
```

