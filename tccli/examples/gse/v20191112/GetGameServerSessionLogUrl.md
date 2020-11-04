**Example 1: 获取游戏会话日志URL**

获取游戏会话日志URL

Input: 

```
tccli gse GetGameServerSessionLogUrl --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde
```

Output: 
```
{
    "Response": {
        "PreSignedUrl": "http://test/url-001",
        "RequestId": "s1596161996478632139"
    }
}
```

