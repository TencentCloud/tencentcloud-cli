**Example 1: 默认实例**

默认返回

Input: 

```
tccli mall DescribeDrawResourceList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ResourceDrawList": [
            {
                "Id": 1,
                "FlowId": 1,
                "ResourceId": "abc",
                "IndexId": "abc",
                "Uin": "abc",
                "BigDealId": "abc",
                "SmallOrderId": "abc",
                "ResourceNewStartTime": "abc",
                "ResourceNewEndTime": "abc",
                "ResourceStatus": 0,
                "Status": 1,
                "ResourceType": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

