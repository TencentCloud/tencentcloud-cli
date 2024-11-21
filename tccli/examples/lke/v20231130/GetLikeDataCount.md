**Example 1: 点赞点踩数据统计**

点赞点踩数据统计

Input: 

```
tccli lke GetLikeDataCount --cli-unfold-argument  \
    --StartTime 1715396806 \
    --EndTime 1716435550 \
    --AppBizId 1 1778345918658510848 \
    --Type 1 \
    --LoginUin 600000562346 \
    --LoginSubAccountUin 600000562346
```

Output: 
```
{
    "Response": {
        "AppraisalTotal": 7,
        "DislikeRate": 0.57,
        "DislikeTotal": 4,
        "LikeRate": 0.43,
        "LikeTotal": 3,
        "ParticipationRate": 1.75,
        "RequestId": "cf081be6-ae5f-4840-9324-d60f748d60b6",
        "Total": 4
    }
}
```

