**Example 1: 获取慧眼人脸核身照片**



Input: 

```
tccli essbasic DescribeFaceIdPhotos --cli-unfold-argument  \
    --Caller.ApplicationId 应用号ID \
    --Caller.SubOrganizationId  \
    --Caller.OperatorId  \
    --WbAppId 分配的慧眼业务ID \
    --OrderNumbers 订单号
```

Output: 
```
{
    "Response": {
        "RequestId": "请求ID,有异常时提供给电子签团队排查问题",
        "Photos": [
            {
                "Result": 0,
                "Description": "",
                "OrderNumber": "订单号",
                "Photo": ""
            }
        ]
    }
}
```

