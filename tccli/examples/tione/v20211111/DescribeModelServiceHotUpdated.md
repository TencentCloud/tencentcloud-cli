**Example 1: 查询模型服务能否开启热更新**

查询模型服务能否开启热更新

Input: 

```
tccli tione DescribeModelServiceHotUpdated --cli-unfold-argument  \
    --ImageInfo.ImageType CCR \
    --ImageInfo.ImageUrl ccr.ccs.tencentyun.com/tiemsdev/hellotest:latest
```

Output: 
```
{
    "Response": {
        "HotUpdatedFlag": "Forbidden",
        "Reason": "为选择模型，无法开启热更新",
        "RequestId": "5d067ec5-def2-44f9-bed2-9b1f75b7067d"
    }
}
```

