**Example 1: DescribeInstanceAgentList 返回示例**

探针详情列表展示返回

Input: 

```
tccli cfg DescribeInstanceAgentList --cli-unfold-argument  \
    --InstanceType 1 \
    --Filters.0.Name InstanceId \
    --Filters.0.Value *** \
    --Page 1 \
    --PageSize 1 \
    --AgentScene 1
```

Output: 
```
{
    "Response": {
        "InstanceAgent": [
            {
                "InstanceAgentItem": [
                    {
                        "Name": "InstanceId",
                        "Value": "ins-********"
                    },
                    {
                        "Name": "Version",
                        "Value": "tchaos-cvm-1.0"
                    },
                    {
                        "Name": "Status",
                        "Value": "2"
                    }
                ]
            }
        ],
        "RequestId": "f5eac377-07f6-4f49-8e4e-44c9f92b08e7",
        "TotalCount": 4
    }
}
```

