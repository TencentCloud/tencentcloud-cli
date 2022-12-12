**Example 1: 查询图库的图片**

{}

Input: 

```
tccli cms DescribeImageLibImage --cli-unfold-argument  \
    --UserAppID xx \
    --UserSubUin xx \
    --Label x \
    --LibID 0 \
    --PageSize 0 \
    --PageIndex 0 \
    --UserUin xx
```

Output: 
```
{
    "Response": {
        "Images": [
            {
                "ModifyUser": "xx",
                "ImageName": "xx",
                "ImageURL": "xx",
                "FileMD5": "xx",
                "Label": "xx",
                "LibID": 0,
                "ImageID": 0,
                "CreateTime": "xx"
            }
        ],
        "TotalCount": 0,
        "RequestId": "xx"
    }
}
```

