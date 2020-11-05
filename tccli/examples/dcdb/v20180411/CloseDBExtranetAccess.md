**Example 1: Disabling public network access for TencentDB instance**



Input: 

```
tccli dcdb CloseDBExtranetAccess --cli-unfold-argument  \
    --InstanceId dcdbt-avw0207d
```

Output: 
```
{
    "Response": {
        "RequestId": "2d1e21a2-b29a-490a-8be0-b61287d92e28",
        "FlowId": 3024
    }
}
```

