**Example 1: 请求示例**



Input: 

```
tccli live DescribeCasterTransitionTypes --cli-unfold-argument  \
    --CasterId 10
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "TransitionTypes": [
            {
                "Index": 1,
                "SourceUrl": "http://www.example.com/url/example",
                "TransitionType": "heart"
            }
        ]
    }
}
```

