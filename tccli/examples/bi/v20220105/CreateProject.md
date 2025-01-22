**Example 1: 创建项目**

创建项目

Input: 

```
tccli bi CreateProject --cli-unfold-argument  \
    --Name 测试项目 \
    --Logo https://tencent.cloud.com/logo.png \
    --ColorCode #ffffff \
    --Mark 创建项目 \
    --IsApply True \
    --DefaultPanelType 1
```

Output: 
```
{
    "Response": {
        "Extra": "1",
        "Data": {
            "Id": 11010
        },
        "Msg": "成功",
        "RequestId": "dsjasdk121kdsfjksadk"
    }
}
```

