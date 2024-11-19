**Example 1: 照片人脸核身成功示例**



Input: 

```
tccli faceid ImageRecognitionV2 --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "成功",
        "Sim": 89.88,
        "RequestId": "f904f4cf-75db-4f8f-a5ec-dc4f942c7f7a"
    }
}
```

**Example 2: 照片人脸核身比对相似度未达标示例**



Input: 

```
tccli faceid ImageRecognitionV2 --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --ImageBase64 /9j/4AAQSkZJRg.....s97n//2Q
```

Output: 
```
{
    "Response": {
        "Description": "比对相似度未达到通过标准",
        "RequestId": "e9e198e4-4fa8-49f0-a67e-f8053bc49201",
        "Result": "FailedOperation.CompareLowSimilarity",
        "Sim": 26.04
    }
}
```

