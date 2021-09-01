**Example 1: 以图搜图**



Input: 

```
tccli ump SearchImage --cli-unfold-argument  \
    --GroupCode group_code \
    --MallId 1 \
    --Image imagebase64string \
    --ImageTime 1600427281051
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "FaceId": "face_id",
        "Results": [
            {
                "Image": "image base64 string",
                "PersonId": "person_id",
                "Similarity": 0.99
            }
        ]
    }
}
```

