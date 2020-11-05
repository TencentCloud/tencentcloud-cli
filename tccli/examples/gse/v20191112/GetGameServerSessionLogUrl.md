**Example 1: Getting the log URL of game session**

This example shows you how to get the log URL of a game session.

Input: 

```
tccli gse GetGameServerSessionLogUrl --cli-unfold-argument  \
    --GameServerSessionId qcs::gse:ap-shanghai:uin/1112222:gameserversession/fleet-qp3ga-p70zzzz/gssess-aaaa-ilqsssu/PlacementId-124ddda-4e28-1111-222b-abcde
```

Output: 
```
{
    "Response": {
        "PreSignedUrl": "http://test/url-001"
    }
}
```

