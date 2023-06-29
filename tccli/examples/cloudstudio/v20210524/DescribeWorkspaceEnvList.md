**Example 1: DescribeWorkspaceEnvList**



Input: 

```
tccli cloudstudio DescribeWorkspaceEnvList --cli-unfold-argument  \
    --CloudStudioSessionTeam xx
```

Output: 
```
{
    "Response": {
        "Data": {},
        "RequestId": "xx"
    }
}
```

**Example 2: DescribeWorkspaceStatusList**



Input: 

```
tccli cloudstudio DescribeWorkspaceEnvList --cli-unfold-argument  \
    --CloudStudioSessionTeam cloudstudio-devops
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "2",
                "Name": "All in One",
                "Tag": "20210719.1",
                "Description": "支持 Java、Go、Python 等多种语言",
                "DescriptionCN": "支持 Java、Go、Python 等多种语言",
                "IconUrl": "https://cs-res.codehub.cn/workspace/assets/icons/all-in-one.svg",
                "Author": "admin",
                "Visible": "PUBLIC",
                "WorkspaceVersion": 2,
                "Sort": 99999
            }
        ],
        "RequestId": "d4bb9a0f-5d27-4780-81c4-4ca88690eddb"
    }
}
```

