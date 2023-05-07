**Example 1: 不良行为识别调用成功**

输入图片URL，识别不良行为信息。

Input: 

```
tccli tiia DetectMisbehavior --cli-unfold-argument  \
    --ImageUrl http://www.test.com/a.jpg
```

Output: 
```
{
    "Response": {
        "Confidence": 0.5,
        "Type": "赌博",
        "RequestId": "7a975d0d-1ebe-4ee3-bde7-f1541fe5b135"
    }
}
```

