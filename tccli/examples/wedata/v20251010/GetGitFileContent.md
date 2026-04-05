**Example 1: 成功调用**



Input: 

```
tccli wedata GetGitFileContent --cli-unfold-argument  \
    --WorkspaceId 17625249429796397 \
    --ConfigType user \
    --ConfigItem git \
    --GitType gitLab \
    --Url http://21.77.151.63/root/wedata_git_test.git \
    --Path / \
    --Branch main \
    --AccessToken None
```

Output: 
```
{
    "Response": {
        "Data": {
            "GitFileInfo": {
                "Path": "/"
            }
        },
        "RequestId": "da8f5999-845e-4a76-b226-0cd55f477a1d"
    }
}
```

