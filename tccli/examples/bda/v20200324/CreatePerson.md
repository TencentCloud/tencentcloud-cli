**Example 1: 调用失败示例**



Input: 

```
tccli bda CreatePerson --cli-unfold-argument  \
    --GroupId testG3 \
    --PersonName testG3P1 \
    --PersonId testG3P1 \
    --Trace.Urls IamNotUrl \
    --Trace.BodyRects.0.X 1 \
    --Trace.BodyRects.0.Y 2 \
    --Trace.BodyRects.0.Width 3 \
    --Trace.BodyRects.0.Height 4
```

Output: 
```
{
    "Response": {
        "TraceId": "",
        "BodyModelVersion": "",
        "InputRetCode": -1001,
        "InputRetCodeDetails": [
            -1102
        ],
        "RequestId": "78b14df0-9ca6-45e0-b5d4-f053db01f9bb"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda CreatePerson --cli-unfold-argument  \
    --GroupId testG3 \
    --PersonName testG3P1 \
    --PersonId testG3P1 \
    --Trace.Urls http://i2.sinaimg.cn/ty/nba/2015-07-05/U10236P6T12D7648505F44DT20150705114547.jpg \
    --Trace.BodyRects.0.X 1 \
    --Trace.BodyRects.0.Y 2 \
    --Trace.BodyRects.0.Width 3 \
    --Trace.BodyRects.0.Height 4
```

Output: 
```
{
    "Response": {
        "TraceId": "testCreatePerson123",
        "BodyModelVersion": "1.0",
        "InputRetCode": 0,
        "InputRetCodeDetails": [
            0
        ],
        "RequestId": "2d44289d-eeb1-4109-8c2e-3c3e514094b9"
    }
}
```

