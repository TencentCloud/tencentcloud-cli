**Example 1: 修改tdsql3-6d3cbb0f的SSL状态**



Input: 

```
tccli tdmysql ModifyInstanceSSLStatus --cli-unfold-argument  \
    --InstanceId tdsql3-6d3cbb0f \
    --Enabled True
```

Output: 
```
{
    "Response": {
        "FlowId": 42666,
        "RequestId": "599821ef-838c-4050-acc6-386ed52e2de2"
    }
}
```

