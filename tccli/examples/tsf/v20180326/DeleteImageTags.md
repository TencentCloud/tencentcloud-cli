**Example 1: DeleteImageTags**



Input: 

```
tccli tsf DeleteImageTags --cli-unfold-argument  \
    --ImageTags.0.RepoName tsf_410xxxxxx/test \
    --ImageTags.0.TagName 20190529xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "8fdd6706-7447-4c00-8717-e834f470dd43",
        "Result": true
    }
}
```

