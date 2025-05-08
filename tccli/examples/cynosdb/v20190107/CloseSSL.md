**Example 1: 关闭SSL加密**

关闭SSL加密

Input: 

```
tccli cynosdb CloseSSL --cli-unfold-argument  \
    --ClusterId cynosdbmysql-jd510000 \
    --InstanceId cynosdbmysql-ins-906n0000
```

Output: 
```
{
    "Response": {
        "FlowId": 1,
        "RequestId": "42d79173-6d36-4239-b7ad-5b993559a5c6",
        "TaskId": 1
    }
}
```

