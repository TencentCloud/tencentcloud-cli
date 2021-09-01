**Example 1: 调用失败示例**



Input: 

```
tccli bda CreateTrace --cli-unfold-argument  \
    --PersonId 3333333333333 \
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
        "RequestId": "81ee3a85-1273-4d39-b7b2-2dea15859039"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda CreateTrace --cli-unfold-argument  \
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
        "TraceId": "testTrace123",
        "BodyModelVersion": "1.0",
        "InputRetCode": 0,
        "InputRetCodeDetails": [
            0
        ],
        "RequestId": "d86cada6-1b1a-4ac1-86a4-c1a6bbb3e54c"
    }
}
```

