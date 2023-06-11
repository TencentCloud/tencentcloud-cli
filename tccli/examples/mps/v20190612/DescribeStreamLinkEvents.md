**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkEvents --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalPage": 1,
        "PageNum": 1,
        "PageSize": 10,
        "RequestId": "xx",
        "Infos": [
            {
                "EventId": "xx",
                "Status": 1,
                "Description": "xx",
                "EventName": "xx",
                "AttachedFlowGroup": [
                    {
                        "FlowId": "xx",
                        "Region": "xx"
                    }
                ],
                "CreateTime": "xx"
            }
        ],
        "TotalNum": 1
    }
}
```

