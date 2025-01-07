**Example 1: 更新服务级账号**

更新服务级账号

Input: 

```
tccli tcr ModifyServiceAccount --cli-unfold-argument  \
    --RegistryId tcr-dg284imq \
    --Name tcr$service-account2 \
    --Description desc 1 \
    --Duration 10
```

Output: 
```
{
    "Response": {
        "RequestId": "44d9705a-dc93-41f8-b596-8552c4dd40d7"
    }
}
```

