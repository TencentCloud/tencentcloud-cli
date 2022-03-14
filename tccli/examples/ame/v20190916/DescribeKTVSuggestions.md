**Example 1: 获取直播互动曲库联想词**



Input: 

```
tccli ame DescribeKTVSuggestions --cli-unfold-argument  \
    --KeyWord zhou
```

Output: 
```
{
    "Response": {
        "KTVSuggestionInfoSet": [
            {
                "Suggestion": "周杰伦"
            }
        ],
        "RequestId": "xx"
    }
}
```

