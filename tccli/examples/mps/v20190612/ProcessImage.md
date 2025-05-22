**Example 1: 发起图片增强**

发起图片增强

Input: 

```
tccli mps ProcessImage --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket bucket-test \
    --InputInfo.CosInputInfo.Region ap-shanghai \
    --InputInfo.CosInputInfo.Object /image/test.png \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket bucket-test \
    --OutputStorage.CosOutputStorage.Region ap-shanghai \
    --ImageTask.EncodeConfig.Format jpeg \
    --ImageTask.EncodeConfig.Quality 75 \
    --ImageTask.EnhanceConfig.SuperResolution.Switch ON
```

Output: 
```
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "TaskId": "3pg2p4jEfbFHYo2rgB0Kzl0esg4NeBItcZyllxO4HNJXdNeRUhk9GjDMjCj1auPv"
    }
}
```

**Example 2: 发起图片擦除**

发起图片擦除

Input: 

```
tccli mps ProcessImage --cli-unfold-argument  \
    --InputInfo.Type COS \
    --InputInfo.CosInputInfo.Bucket bucket-test \
    --InputInfo.CosInputInfo.Region ap-shanghai \
    --InputInfo.CosInputInfo.Object /image/test.png \
    --OutputStorage.Type COS \
    --OutputStorage.CosOutputStorage.Bucket bucket-test \
    --OutputStorage.CosOutputStorage.Region ap-shanghai \
    --ImageTask.EncodeConfig.Format jpeg \
    --ImageTask.EncodeConfig.Quality 75 \
    --ImageTask.EraseConfig.ImageEraseLogo.Switch ON \
    --ImageTask.EraseConfig.ImageEraseLogo.ImageAreaBoxes.0.Type logo \
    --ImageTask.EraseConfig.ImageEraseLogo.ImageAreaBoxes.0.AreaCoordSet 101 85 111 95
```

Output: 
```
{
    "Response": {
        "RequestId": "03b25aab-8883-497e-838f-d760c3e220f6",
        "TaskId": "3pg2p4jEfbFHYo2rgB0Kzl0esg4NeBItcZyllxO4HNJXdNeRUhk9GjDMjCj1auPv"
    }
}
```

