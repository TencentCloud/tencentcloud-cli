**Example 1: 删除人脸成功示例**



Input: 

```
tccli iai DeleteFace --cli-unfold-argument  \
    --PersonId 1001 \
    --FaceIds 2875186538564559728
```

Output: 
```
{
    "Response": {
        "SucDeletedNum": 1,
        "SucFaceIds": [
            "2875186538564559728"
        ],
        "RequestId": "38f96439-d5ea-48ea-899b-44a284708f6b"
    }
}
```

**Example 2: 删除人脸失败示例**



Input: 

```
tccli iai DeleteFace --cli-unfold-argument  \
    --PersonId 5001 \
    --FaceIds 2875186538564559728
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceNotFound.ErrorPersonNotExisted",
            "Message": "个体不存在。"
        },
        "RequestId": "e2b603e5-51d0-4a8a-8319-2df026ae7518"
    }
}
```

