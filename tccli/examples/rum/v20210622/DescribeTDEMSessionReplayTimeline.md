**Example 1: 示例**



Input: 

```
tccli rum DescribeTDEMSessionReplayTimeline --cli-unfold-argument  \
    --AppId 1****2 \
    --SessionId c4d4b78baf9f467cb393cc4cdf123389 \
    --Limit 10000 \
    --Cursor 0
```

Output: 
```
{
    "Response": {
        "Result": "{\"HasMore\":false,\"NextCursor\":0,\"Replays\":[{\"ReplayId\":\"rep_7b043a235812c2df4f5fad22fa3db880\",\"StartTime\":1778843329995,\"EndTime\":1778843393978,\"FirstPageUrl\":\"http://9.135.33.202/\",\"FirstPageTitle\":\"\",\"EventCount\":239},{\"ReplayId\":\"rep_4b7410e51a0f8f605980866a8a462be0\",\"StartTime\":1778843337473,\"EndTime\":1778843359976,\"FirstPageUrl\":\"http://9.135.33.202/item/SN000004\",\"FirstPageTitle\":\"\",\"EventCount\":225},{\"ReplayId\":\"rep_34d62d906f726c899a4ad2bed3e48d4d\",\"StartTime\":1778843399978,\"EndTime\":1778843447024,\"FirstPageUrl\":\"http://9.135.33.202/\",\"FirstPageTitle\":\"\",\"EventCount\":342}],\"SessionEndTime\":1778843447024,\"SessionId\":\"c4d4b78baf9f467cb393cc4cdf123389\",\"SessionStartTime\":1778843329995,\"Timeline\":[],\"Truncated\":false}",
        "RequestId": "9fe18bc7-ac48-4d35-a953-f28b0a0fd814"
    }
}
```

