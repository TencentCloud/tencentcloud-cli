**Example 1: 查询独享实例列表**

查询当前用户专享实例列表

Input: 

```
tccli apigateway DescribeExclusiveInstancesStatus --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 2,
            "InstanceSet": [
                {
                    "InstanceId": "instance-9ot9druo",
                    "InstanceName": "",
                    "InstanceDescription": "",
                    "InstanceChargeType": "POSTPAID",
                    "CreatedTime": "2022-06-10T01:41:24Z",
                    "InstanceType": "basic",
                    "InstanceState": "RUNNING",
                    "DealName": "20220610784016110174871"
                },
                {
                    "InstanceId": "instance-17hzlblu",
                    "InstanceName": "",
                    "InstanceDescription": "",
                    "InstanceChargeType": "POSTPAID",
                    "CreatedTime": "2022-06-10T01:41:07Z",
                    "InstanceType": "basic",
                    "InstanceState": "RUNNING",
                    "DealName": "20220610784016110117441"
                }
            ]
        },
        "RequestId": "06737236380502816"
    }
}
```

