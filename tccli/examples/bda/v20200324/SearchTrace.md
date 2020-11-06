**Example 1: 调用失败示例**



Input: 

```
tccli bda SearchTrace --cli-unfold-argument  \
    --GroupId 12311111111 \
    --Trace.Urls http://i2.sinaimg.cn/ty/nba/2015-07-05/U10236P6T12D7648505F44DT20150705114547.jpg \
    --Trace.BodyRects.0.X 260 \
    --Trace.BodyRects.0.Y 1 \
    --Trace.BodyRects.0.Width 272 \
    --Trace.BodyRects.0.Height 365 \
    --MaxPersonNum 2
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.GroupIdNotExist",
            "Message": "人体库ID不存在。"
        },
        "RequestId": "1a5de4e8-02a0-4b4e-8c9a-e66e6f26d12a"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda SearchTrace --cli-unfold-argument  \
    --GroupId 12311111111 \
    --Trace.Urls http://i2.sinaimg.cn/ty/nba/2015-07-05/U10236P6T12D7648505F44DT20150705114547.jpg \
    --Trace.BodyRects.0.X 260 \
    --Trace.BodyRects.0.Y 1 \
    --Trace.BodyRects.0.Width 272 \
    --Trace.BodyRects.0.Height 365 \
    --MaxPersonNum 2
```

Output: 
```
{
    "Response": {
        "Candidates": [
            {
                "PersonId": "testG10P1",
                "TraceId": "3517452339320503246",
                "Score": 99.99
            },
            {
                "PersonId": "testG10P40",
                "TraceId": "3516549744519331668",
                "Score": 99.99
            }
        ],
        "BodyModelVersion": "1.0",
        "InputRetCode": 0,
        "InputRetCodeDetails": [
            0
        ],
        "RequestId": "0301e30d-e83c-43c7-b78c-29eafea4762d"
    }
}
```

