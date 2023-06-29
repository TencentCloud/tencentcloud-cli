**Example 1: 示例1**



Input: 

```
tccli keewidb DescribeInstanceParamRecords --cli-unfold-argument  \
    --InstanceId kee-9clk**** \
    --Limit 100 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "InstanceParamHistory": [
            {
                "ModifyTime": "2022-03-10 12:41:24",
                "NewValue": "no",
                "ParamName": "auto-failback",
                "PreValue": "yes",
                "Status": 2
            }
        ],
        "RequestId": "10b66e77-e729-4708-84a4-2f542677b604",
        "TotalCount": 1
    }
}
```

