**Example 1: 获取购车意向评级**

以MD5 IMEI号为参数获取购车意向评分

Input: 

```
tccli apcas PredictRating --cli-unfold-argument  \
    --Type 8 \
    --Id 9aa40fe5e32938e34f767cc0f9f58702
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "RatingData": {
            "Rank": 1
        }
    }
}
```

