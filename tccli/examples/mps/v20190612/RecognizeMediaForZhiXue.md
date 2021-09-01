**Example 1: 发起媒体智能识别**

默认开启全部识别功能。

Input: 

```
tccli mps RecognizeMediaForZhiXue --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket TopRankVideo-125xxx88 \
    --InputInfo.CosInputInfo.Region ap-chongqing \
    --InputInfo.CosInputInfo.Object /movie/201907/WildAnimal.mov
```

Output: 
```
{
    "Response": {
        "TaskId": "125xxx65-RecognizeMediaForZhiXue-bffb15f07530b57bc1aabb01fac74bca",
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

