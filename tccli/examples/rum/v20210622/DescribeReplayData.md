**Example 1: DescribeReplayData示例**



Input: 

```
tccli rum DescribeReplayData --cli-unfold-argument  \
    --AppId 1****2 \
    --ReplayId cd745a80dc454d1ea5f482758c36ca30 \
    --SessionId 427f1ec920614e579aafc99f726af883 \
    --SegmentId 0
```

Output: 
```
{
    "Response": {
        "Result": "{\"Events\":[{\"data\":{\"height\":1080,\"href\":\"https://app.example.com/user/profile\",\"width\":1920},\"timestamp\":1776651631842,\"type\":4},{\"data\":{\"node\":{\"childNodes\":[{\"name\":\"html\",\"publicId\":\"\",\"systemId\":\"\",\"type\":1},{\"attributes\":{\"lang\":\"zh-CN\"},\"childNodes\":[{\"attributes\":{},\"childNodes\":[],\"id\":3,\"tagName\":\"head\",\"type\":2},{\"attributes\":{},\"childNodes\":[{\"attributes\":{\"id\":\"app\"},\"childNodes\":[{\"id\":6,\"textContent\":\"TDEM-cont_**_00828\",\"type\":3}],\"id\":5,\"tagName\":\"div\",\"type\":2}],\"id\":4,\"tagName\":\"body\",\"type\":2}],\"id\":2,\"tagName\":\"html\",\"type\":2}],\"id\":1,\"type\":0}},\"timestamp\":1776651631942,\"type\":2}],\"Platform\":\"web\",\"ReplayFormat\":\"rrweb\",\"ReplayId\":\"cd745a80dc454d1ea5f482758c36ca30\",\"SegmentId\":0}",
        "RequestId": "1c48154d-15a6-42af-99c4-5f9cb563f184"
    }
}
```

