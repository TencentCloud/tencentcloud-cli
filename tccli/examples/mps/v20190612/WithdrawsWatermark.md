**Example 1: 发起提取水印任务**

提取视频中的暗水印。

Input: 

```
tccli mps WithdrawsWatermark --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Region ap-chongqing \
    --InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxx65-WithdrawsWatermark-bffb15f07530b57bc1aabb01fac74bca",
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

