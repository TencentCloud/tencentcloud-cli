**Example 1: 请求示例**

根据安全组反差关联的Flow信息。

Input: 

```
tccli mps DescribeGroupAttachFlowsById --cli-unfold-argument  \
    --Id 019202e96d9f09dc0f325e7f7a2a
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "FlowId": "01937702c54509dc0f3269ca341f",
                "FlowName": "test_flow",
                "EventId": "019202e96d9f09dc0f325e7f7a2a",
                "FlowRegion": "ap-shanghai",
                "OutputRegion": "ap-shanghai",
                "EventName": "test_live",
                "InputName": "pgm_srt",
                "OutputName": "pgm_rtmp",
                "InOutId": "01937722c54509dc0f3269ca356g",
                "InOutType": "input"
            }
        ],
        "RequestId": "01937702ecc509dc0f3269ca3420"
    }
}
```

