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
        "Infos": [
            {
                "EventName": "abc",
                "EventId": "abc",
                "CreateTime": "abc",
                "Description": "abc",
                "Status": 1,
                "AttachedFlowGroup": [
                    {
                        "FlowId": "abc",
                        "Region": "abc"
                    }
                ]
            }
        ],
        "PageNum": 0,
        "PageSize": 0,
        "TotalNum": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

