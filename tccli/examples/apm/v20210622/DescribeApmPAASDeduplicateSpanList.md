**Example 1: 调用失败示例**

调用失败示例

Input: 

```
tccli apm DescribeApmPAASDeduplicateSpanList --cli-unfold-argument  \
    --StartTime 1741246244000 \
    --EndTime 1741246784000 \
    --InstanceId apm-CVfliqa8U
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation",
            "Message": "post status code:400, result={\"code\":230000,\"msg\":\"java.lang.RuntimeException: 数据查询错误\",\"data\":null,\"request_id\":\"9f26a420183f9e3d137fedb9621824f3\"}"
        },
        "RequestId": "4c8f1ec7-5053-4688-b91f-687be243ed25"
    }
}
```

