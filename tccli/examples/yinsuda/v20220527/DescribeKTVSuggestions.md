**Example 1: 获取曲库联想词**

获取曲库联想词

Input: 

```
tccli yinsuda DescribeKTVSuggestions --cli-unfold-argument  \
    --UserId 11113451 \
    --KeyWord 等 \
    --AppName test
```

Output: 
```
{
    "Response": {
        "KTVSuggestionInfoSet": [
            {
                "Suggestion": "等"
            },
            {
                "Suggestion": "等一分钟"
            },
            {
                "Suggestion": "等的太久"
            },
            {
                "Suggestion": "等你归来"
            },
            {
                "Suggestion": "等不来花开"
            },
            {
                "Suggestion": "等你等了那么久"
            },
            {
                "Suggestion": "等你下课"
            },
            {
                "Suggestion": "等什么君"
            },
            {
                "Suggestion": "等不到花开"
            },
            {
                "Suggestion": "等风来"
            }
        ],
        "RequestId": "bddc6a88-eec8-485b-aa12-6a133cd3268d"
    }
}
```

