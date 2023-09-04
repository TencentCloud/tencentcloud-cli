**Example 1: 获取视频扩展信息**

成功响应

Input: 

```
tccli weilingwith DescribeCameraExtendInfo --cli-unfold-argument  \
    --WID c0e3f641-6ec6-444e-8ac9-3cfecc755cb0 \
    --WorkspaceId 1016 \
    --ApplicationToken ct5E8QNPQEZZqNW7ShPAJQVzrTV9xIbL
```

Output: 
```
{
    "Response": {
        "RequestId": "825de5ec-46bd-4682-b4fc-84e807ce2eed",
        "Result": {
            "HistoryResolution": 0,
            "LiveResolution": 480,
            "SaveDay": 0,
            "SaveType": "nvr"
        }
    }
}
```

