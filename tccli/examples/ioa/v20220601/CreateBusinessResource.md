**Example 1: 创建业务资源测试用例**

测试用例

Input: 

```
tccli ioa CreateBusinessResource --cli-unfold-argument  \
    --AreaId 3684 \
    --Protocol 1 \
    --ServiceName test资源 \
    --ServiceType domain \
    --ServicePort 8080 \
    --Levels 12312 \
    --ServiceAddress *.12312.com \
    --DirectConn 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "ServiceId": 4391
        },
        "RequestId": "20a21cd8-cbc5-4d70-a14d-9c6aafcbd8ab"
    }
}
```

