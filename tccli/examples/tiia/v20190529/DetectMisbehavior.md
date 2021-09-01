**Example 1: 不良行为识别调用成功**



Input: 

```
tccli tiia DetectMisbehavior --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "Confidence": 0.5,
        "Type": "赌博",
        "RequestId": "seqqq948487"
    }
}
```

