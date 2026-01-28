**Example 1: 照片人脸核身**



Input: 

```
tccli faceid ImageRecognition --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --ImageBase64 <ImageBase64>
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

