**Example 1: 下架歌曲接口**

供TME侧进行下架歌曲

Input: 

```
tccli ame TakeMusicOffShelves --cli-unfold-argument  \
    --TakeMusicOffShelves.0.MusicIds E4CC97317AFDB8BA5569BB40AF7AEF08 \
    --TakeMusicOffShelves.0.SaleStatus 2
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

