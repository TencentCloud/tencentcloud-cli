**Example 1: 上架歌曲接口**

供TME侧进行歌曲上架

Input: 

```
tccli ame PutMusicOnTheShelves --cli-unfold-argument  \
    --MusicIds E4CC97317AFDB8BA5569BB40AF7AEF08
```

Output: 
```
{
    "Response": {
        "FailedNum": 0,
        "SuccessNum": 0,
        "FailedMusicIds": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

