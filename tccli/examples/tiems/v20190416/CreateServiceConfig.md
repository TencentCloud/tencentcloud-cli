**Example 1: 创建服务配置**



Input: 

```
tccli tiems CreateServiceConfig --cli-unfold-argument  \
    --Name test \
    --Runtime pmml \
    --ModelUri cos://ti-example-125550209.cos.ap-beijing.myqcloud.com/models/pmml/ \
    --Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "63dccc5a-0084-4a3e-a9ae-cefb019fce9d",
        "ServiceConfig": {
            "Id": "aktst2r9fkmtpdf8",
            "Name": "test",
            "Runtime": "pmml",
            "ModelUri": "cos://ti-example-125550209.cos.ap-beijing.myqcloud.com/models/pmml/",
            "CreateTime": "2019-11-07T15:01:12+08:00",
            "UpdateTime": "2019-11-07T15:01:12+08:00",
            "Version": "1.0",
            "Description": "test"
        }
    }
}
```

