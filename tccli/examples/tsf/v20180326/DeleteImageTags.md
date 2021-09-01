**Example 1: DeleteImageTags**



Input: 

```
tccli tsf DeleteImageTags --cli-unfold-argument  \
    --ImageTags.0.RepoName xx \
    --ImageTags.0.TagName xx \
    --RepoType xx
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "xx"
    }
}
```

