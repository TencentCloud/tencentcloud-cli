**Example 1: 查看对象列表**



Input: 

```
tccli waf DescribeObjects --cli-unfold-argument  \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True
```

Output: 
```
{
    "Response": {
        "ClbObjects": [
            {
                "ObjectId": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "PreciseDomains": [
                    "abc"
                ],
                "Status": 0,
                "ClsStatus": 0,
                "VirtualDomain": "abc",
                "ObjectName": "abc",
                "PublicIp": [
                    "abc"
                ],
                "PrivateIp": [
                    "abc"
                ],
                "VpcName": "abc",
                "Vpc": "abc",
                "InstanceLevel": 0,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

