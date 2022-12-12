**Example 1: CreateImageLibImage**



Input: 

```
tccli cms CreateImageLibImage --cli-unfold-argument  \
    --UserAppID xx \
    --UserUin xx \
    --LibID 0 \
    --ImageData.0.Content xx \
    --ImageData.0.Url  \
    --ImageData.0.Index xx \
    --ImageData.0.ImageName xx \
    --ImageData.0.FileMD5 xx \
    --ImageData.0.Label xx \
    --UserSubUin xx
```

Output: 
```
{
    "Response": {
        "CreateResult": [
            {
                "Url": "xx",
                "Status": 0,
                "Index": "xx",
                "ImageID": 0
            }
        ],
        "Result": 0,
        "RequestId": "xx"
    }
}
```

