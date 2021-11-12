**Example 1: DescribeExclusiveInstances**



Input: 

```
tccli apigateway DescribeExclusiveInstances --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Result": {
            "InstanceId": "instance-0c96l2bo",
            "InstanceName": "test_instance",
            "InstanceDescription": "",
            "InstanceChargeType": "PREPAID",
            "InstanceState": "RUNNING",
            "InstanceType": "BASIC",
            "DealName": "xx",
            "ResourceId": "xx",
            "CreatedTime": "2018-10-30T04:24:19Z"
        },
        "RequestId": "e3705d00-bfe0-4fde-942c-cebd6b12431b"
    }
}
```

