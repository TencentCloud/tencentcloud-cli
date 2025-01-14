**Example 1: 请求示例**

根据安全组反差关联的Flow信息。

Input: 

```
tccli mps DescribeGroupAttachFlowsById --cli-unfold-argument  \
    --Id abc
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "FlowId": "abc",
                "FlowName": "abc",
                "EventId": "abc",
                "FlowRegion": "abc",
                "OutputRegion": "abc",
                "EventName": "abc",
                "InputName": "abc",
                "OutputName": "abc",
                "InOutId": "abc",
                "InOutType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

