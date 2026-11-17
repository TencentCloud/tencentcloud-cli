**Example 1: 编辑项目基本信息**



Input: 

```
tccli makers ModifyProject --cli-unfold-argument  \
    --ZoneId zone-************ \
    --ProjectId makers-************ \
    --Name ************** \
    --RootDir / \
    --OutputDir dist \
    --BuildCmd npm run build \
    --InstallCmd npm install \
    --Framework Other \
    --CoverUrl ************************************************************** \
    --NodeJsVersion 22.11.0
```

Output: 
```
{
    "Response": {
        "RequestId": "63fb7e9d-cb30-43c0-8e1a-868412477911"
    }
}
```

