**Example 1: 根据TaskId查询克隆形象列表**



Input: 

```
tccli live DescribeLiveAvatarCloneFigureList --cli-unfold-argument  \
    --TaskId 7501606042561581056
```

Output: 
```
{
    "Response": {
        "CloneFigureList": [
            {
                "AvatarKey": "966163fdc71b4d31b031ae03ffe5587b",
                "CreateTime": "2026-09-04 19:44:13",
                "EstimatedCompleteTime": "",
                "ExpireTime": "",
                "FailReason": "",
                "FigureImg": "",
                "FigureName": "图生测试形象",
                "Gender": "UNKNOWN",
                "IsExpired": false,
                "MaterialUrl": "https://wsh-test-1303333058.cos.ap-guangzhou.myqcloud.com/%E6%95%B0%E5%AD%97%E4%BA%BA%E6%B5%8B%E8%AF%95/%E6%95%B0%E5%AD%97%E4%BA%BA%E5%A5%B3%E4%B8%BB%E6%92%AD.png",
                "PhotoVersion": 1,
                "Progress": 100,
                "RenewStatus": "UNKNOWN",
                "SceneType": "PHOTO",
                "Status": "SUCCESS",
                "TaskId": "7501606042561581056",
                "UpdateTime": "2026-09-04 19:49:04"
            }
        ],
        "TotalCount": 1,
        "RequestId": "dc5e6604-e6e9-427e-ae39-57ef6f903b8b"
    }
}
```

