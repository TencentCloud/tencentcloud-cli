**Example 1: DeleteImageTags**



Input: 

```
tccli tsf DeleteImageTags --cli-unfold-argument  \
    --ImageTags.0.RepoName tsf_1000000/images \
    --ImageTags.0.TagName consumer-demo \
    --RepoType tcr
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc-defg"
    }
}
```

