**Example 1: 图库删除图片**



Input: 

```
tccli cms DeleteImageLibImage --cli-unfold-argument  \
    --UserAppID xx \
    --UserUin xx \
    --LibID 0 \
    --ImageIDs 0 \
    --UserSubUin xx
```

Output: 
```
{
    "Response": {
        "DeleteResult": [
            {
                "ImageName": "xx",
                "Label": "xx",
                "ErrMsg": "xx",
                "ImageID": 0
            }
        ],
        "Result": 0,
        "RequestId": "xx"
    }
}
```

