**Example 1: 提交视频审核任务**



Input: 

```
tccli ticm VideoModeration --cli-unfold-argument  \
    --VideoUrl https://test.mp4 \
    --CBUrl http://callback.test.com \
    --DeveloperId 123456 \
    --Extra 0001
```

Output: 
```
{
    "Response": {
        "RequestId": "seqqq948487111111",
        "VodTaskId": "1254418846-procedurev2-aefb7f39e6d3da0e66596b93e7e9e008t0"
    }
}
```

