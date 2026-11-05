**Example 1: 开启rw的Serverless弹性配置**



Input: 

```
tccli cynosdb SetInstanceServerlessQuota --cli-unfold-argument  \
    --ClusterId cynosdbmysql-9tbxdtfl \
    --ServerlessQuotaConfigs.0.InstanceType rw \
    --ServerlessQuotaConfigs.0.MaxCcu 4 \
    --ServerlessQuotaConfigs.0.Enabled True
```

Output: 
```
{
    "Response": {
        "TaskId": 64769,
        "RequestId": "c15bbd12-5021-4b8f-b955-95605a49c6b4"
    }
}
```

