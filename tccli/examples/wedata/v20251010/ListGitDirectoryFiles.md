**Example 1: 成功调用**



Input: 

```
tccli wedata ListGitDirectoryFiles --cli-unfold-argument  \
    --WorkspaceId 17625249429796397 \
    --ConfigType user \
    --ConfigItem git
```

Output: 
```
{
    "Response": {
        "Data": {
            "ContentUrl": "",
            "Branches": [
                "as",
                "master"
            ],
            "ChildPath": []
        },
        "RequestId": "da8f5999-845e-4a76-b226-0cd55f477a1d"
    }
}
```

