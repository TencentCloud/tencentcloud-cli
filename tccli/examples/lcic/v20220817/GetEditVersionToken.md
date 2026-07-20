**Example 1: 获取信令剪辑token**



Input: 

```
tccli lcic GetEditVersionToken --cli-unfold-argument  \
    --SdkAppId 3520371 \
    --RoomId 326744409 \
    --UserId 3CQjnjDYLVGVl6OGR7eItiwQS3W \
    --ExpireSeconds 0
```

Output: 
```
{
    "Response": {
        "RoomId": 326744409,
        "Token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbGFzc19pZCI6MzI2NzQ0NDA5LC*leH**OjQ5MzQwNTc4MzQsInVzZ*JfaWQiOiIzQ1FqbmpEWUxWR1ZsNk*HUj*lSXRpd1FTM1ciLCJzY2VuZSI6**VkaXQifQ.SiuIPIRHUe6HgccsOdr*BIe1ecevFUjs6BsQfM59_PQ",
        "UserId": "3CQjnjDYLVGVl6OGR7eItiwQS3W",
        "RequestId": "e88f49f8-2268-4546-b58a-745fa523f933"
    }
}
```

