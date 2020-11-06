**Example 1: 创建自定义运行环境**



Input: 

```
tccli tiems CreateRuntime --cli-unfold-argument  \
    --Name test \
    --Framework test \
    --Image ccr.ccs.tencentyun.com/testrepo/testimage:v1 \
    --Description test \
    --HealthCheckOn false
```

Output: 
```
{
    "Response": {
        "RequestId": "e8717195-6b62-4fcc-99fe-e29d2aecb21e",
        "Runtime": {
            "Name": "test",
            "Framework": "test",
            "Description": "字符串",
            "Public": false,
            "HealthCheckOn": false,
            "Image": "ccr.ccs.tencentyun.com/testrepo/testimage:v1",
            "CreateTime": "2019-11-07T14:47:49+08:00"
        }
    }
}
```

