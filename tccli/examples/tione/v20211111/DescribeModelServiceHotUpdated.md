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
        "RequestId": "5d067ec5-def2-44f9-bed2-9b1f75b7067d"
    }
}
```

