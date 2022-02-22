**Example 1: 获取慧眼人脸核身结果**



Input: 

```
tccli essbasic DescribeFaceIdResults --cli-unfold-argument  \
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
        "Results": [
            {
                "Result": 0,
                "Description": "",
                "OrderNumber": "订单号",
                "Name": "姓名",
                "IdCardType": "ID_CARD",
                "IdCardNumber": "110101190101011030",
                "LiveRate": 99,
                "Similarity": 99.99,
                "OccurredTime": 1234567890,
                "Photo": "",
                "Video": ""
            }
        ]
    }
}
```

