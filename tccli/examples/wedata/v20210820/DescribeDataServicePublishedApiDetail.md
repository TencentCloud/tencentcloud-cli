**Example 1: 查询数据服务API的发布态信息响应**

查询数据服务API的发布态信息响应示例

Input: 

```
tccli wedata DescribeDataServicePublishedApiDetail --cli-unfold-argument  \
    --Id 1848956796467621890 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApiDescription": "",
            "ApiId": "1792441377707995137",
            "ApiName": "test_0520",
            "ApiStatus": 1,
            "ApiTagNames": "",
            "AuthType": 1,
            "GatewayApiUrl": "http://service-xxxxxxx.bj.tencentapigw.cn;https://service-xxxxxxx.bj.tencentapigw.cn",
            "MaxAllowPageSize": 2000,
            "MaxAllowQps": 1,
            "OwnerName": "jaredlin",
            "PathUrl": "/test_0520",
            "RequestError": "{\"code\":\"FailedOperation\",\"message\":\"服务内部发生异常!\",\"requestId\":\"37f66f3c-d9e5-48be-a745-c15eb4b9f41d\"}",
            "RequestExample": "http://service-xxxxxxx.bj.tencentapigw.cn/test_0520?id=1",
            "RequestParam": [
                {
                    "BindField": "id",
                    "DefaultValue": "1",
                    "Description": "记录Id",
                    "ExampleValue": "1",
                    "NonEmpty": 0,
                    "Operator": "=",
                    "ParamName": "id",
                    "ParamPosition": "Query",
                    "ParamType": "Integer"
                }
            ],
            "RequestSuccess": "{\"code\":\"SUCCESS\",\"message\":\"查询成功\",\"data\":{\"totalCount\":1,\"dataSet\":[{\"name123\":\"李四\",\"id\":1}]},\"requestId\":\"94881ebe-01a8-4c45-b2bf-f2175ea2e093\"}",
            "RequestType": "GET",
            "ResponseParam": [
                {
                    "BindField": "name123",
                    "Description": "姓名",
                    "ExampleValue": "李四",
                    "ParamName": "name123",
                    "ParamType": "String"
                },
                {
                    "BindField": "id",
                    "Description": "Id",
                    "ExampleValue": "1",
                    "ParamName": "id",
                    "ParamType": "Integer"
                }
            ],
            "TimeoutPeriod": 5
        },
        "RequestId": "13684205-8efc-479e-9bdd-772c96df6fff"
    }
}
```

