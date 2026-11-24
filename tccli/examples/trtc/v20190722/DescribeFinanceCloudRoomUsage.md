**Example 1: 查询金融云房间维度用量**

查询金融云房间维度用量

Input: 

```
tccli trtc DescribeFinanceCloudRoomUsage --cli-unfold-argument  \
    --SdkAppId 1500000000 \
    --StartTime 2026-11-15 16:53 \
    --EndTime 2026-11-16 16:13
```

Output: 
```
{
    "Response": {
        "Data": "RoomId,Duration\n123035,452\n123036,1128\nhli_036,120\n",
        "RequestId": "570a54ce-2e76-4fef-ae9b-bf98a568c61e"
    }
}
```

