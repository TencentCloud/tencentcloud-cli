**Example 1: 活体检测失败**

活体检测失败，没有检测到指定动作

Input: 

```
tccli faceid CompareFaceLiveness --cli-unfold-argument  \
    --ImageBase64 iVBORw0KGg...(total length:121036)s97n//2Q== \
    --VideoBase64 AAAAGGZ0eX...(total length:1651021)AAwAAAAEecg= \
    --LivenessType ACTION \
    --ValidateData 4,2
```

Output: 
```
{
    "Response": {
        "Result": "FailedOperation.ActionFirstAction",
        "Description": "The first motion is not detected.",
        "Sim": 0,
        "BestFrameBase64": "/9j/4AAQSk...(total length:161021)W/M7/M/9k=",
        "RequestId": "df5afd82-6469-4a4a-bd62-debf8c2ef94f"
    }
}
```

**Example 2: 活体人脸比对通过，判定为同一人**

活体检测以及人脸比对通过，判定为同一人

Input: 

```
tccli faceid CompareFaceLiveness --cli-unfold-argument  \
    --LivenessType SILENT \
    --ImageBase64 iVBORw0KGg...(total length:121036)s97n//2Q== \
    --VideoBase64 AAAAGGZ0eX...(total length:1651021)AAwAAAAEecg= \
    --ValidateData 
```

Output: 
```
{
    "Response": {
        "Result": "Success",
        "Description": "Success",
        "Sim": 100,
        "BestFrameBase64": "/9j/4AAQSk...(total length:142036)s97n//2Q==",
        "RequestId": "f89097ac-4003-4d73-acb3-696d4057b9eb"
    }
}
```

**Example 3: 活体人脸比对通过，判定不是同一人**

活体检测以及人脸比对通过，判定不是同一人

Input: 

```
tccli faceid CompareFaceLiveness --cli-unfold-argument  \
    --ImageBase64 iVBORw0KGg...(total length:121036)s97n//2Q== \
    --VideoBase64 AAAAGGZ0eX...(total length:1651021)AAwAAAAEecg= \
    --LivenessType ACTION \
    --ValidateData 1
```

Output: 
```
{
    "Response": {
        "Result": "FailedOperation.CompareLowSimilarity",
        "Description": "The comparison similarity did not reach the passing standard.",
        "Sim": 9.21,
        "BestFrameBase64": "/9j/4AAQSk...(total length:138021)8ASrH/2Q==",
        "RequestId": "6176fad1-f078-445b-8a4d-c8a903528b5a"
    }
}
```

