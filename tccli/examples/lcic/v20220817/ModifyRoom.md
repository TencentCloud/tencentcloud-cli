**Example 1: 示例**

修改类型

Input: 

```
tccli lcic ModifyRoom --cli-unfold-argument  \
    --RoomId 368760996 \
    --SdkAppId 3520371 \
    --InteractionMode 0 \
    --VideoOrientation 0 \
    --IsGradingRequiredPostClass 1 \
    --RoomType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "50034c8f-cd77-43f2-815e-afe990fb023d"
    }
}
```

**Example 2: 修改房间**

修改房间参数示例

Input: 

```
tccli lcic ModifyRoom --cli-unfold-argument  \
    --RoomId 301234567 \
    --StartTime 1704074400 \
    --EndTime 1704076200 \
    --TeacherId 2i5WfUzRRC2Eb2uNmLNv96gzxCv \
    --Name myClass \
    --Resolution 1 \
    --MaxMicNumber 1 \
    --AutoMic 1 \
    --AudioQuality 1 \
    --SubType videodoc \
    --DisableRecord 1 \
    --Assistants 2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc \
    --SdkAppId 1 \
    --GroupId 301234567 \
    --EnableDirectControl 1
```

Output: 
```
{
    "Response": {
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

