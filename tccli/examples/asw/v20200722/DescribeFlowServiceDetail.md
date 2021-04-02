**Example 1: 查询状态机详情**



Input: 

```
tccli asw DescribeFlowServiceDetail --cli-unfold-argument  \
    --FlowServiceResource qrn:qcs:asw:sh:1300074211:http:json:flowmachine:flowservicetest:bcrlj428
```

Output: 
```
{
    "Response": {
        "FlowServiceName": "flowservicetest",
        "FlowServiceChineseName": "状态机中文名称",
        "Status": "Online",
        "Definition": "{\"Comment\":\"An example of the Amazon States Language using a map state to process elements of an array with a max concurrency of 2.\",\"StartAt\":\"Map\",\"States\":{\"Map\":{\"Type\":\"Map\",\"ItemsPath\":\"$.job-spec\",\"ResultPath\":\"$.array\",\"MaxConcurrency\":2,\"Next\":\"Final State\",\"Iterator\":{\"StartAt\":\"My Stage\",\"States\":{\"My Stage\":{\"Type\":\"Task\",\"Resource\":\"arn:aws:states:::lambda:invoke\",\"Parameters\":{\"FunctionName\":\"arn:aws:lambda:us-east-1:<>:function:some-lambda:$LATEST\",\"Payload\":{\"Input.$\":\"$.array\"}},\"End\":true}}}},\"Final State\":{\"Type\":\"Pass\",\"End\":true}}}",
        "RoleResource": "qrn:qcs:asw:sh:1300074211:http:qrn",
        "Type": "EXPRESS",
        "CreateDate": "1595227100",
        "Description": "这是一个用来做演示的状态机",
        "RequestId": "ab1b30fc-3503-4b27-96dc-94c14d2fd43w",
        "EnableCLS": 1,
        "CLSUrl": "https://console.cloud.tencent.com/cls",
        "FlowInput": "xx"
    }
}
```

