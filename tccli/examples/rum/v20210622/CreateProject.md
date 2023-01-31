**Example 1: 创建 RUM 应用**

创建 RUM 应用

Input: 

```
tccli rum CreateProject --cli-unfold-argument  \
    --Name '测试项目' \
    --InstanceID "taw-123" \
    --Repo 'http://github.com/xxx' \
    --URL 'http://www.qq.com' \
    --Rate "10" \
    --EnableURLGroup 1 \
    --Type web \
    --Desc '项目描述'
```

Output: 
```
{
    "Response": {
        "ID": 1,
        "Key": "RlOmCVbPrKd4",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

