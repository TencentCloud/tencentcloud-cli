**Example 1: 查询支持开启 HTTPS 的实例**



Input: 

```
tccli lighthouse DescribeSupportHttpsInstances --cli-unfold-argument  \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "SupportHttpsInstanceSet": [
            {
                "InstanceId": "lhins-aaaabbbb",
                "InstanceName": "insname",
                "PublicAddresses": [
                    "1.2.3.4"
                ],
                "AutomationAgentStatus": "Offline"
            }
        ],
        "RequestId": "cb31e424-0b5f-4f25-8cfc-76121aed5b58"
    }
}
```

