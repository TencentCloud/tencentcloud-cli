**Example 1: 人脸特效-人脸试妆-拉起素材列表**



Input: 

```
tccli fmu GetModelList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "ModelIdNum": 1,
        "ModelInfos": [
            {
                "ModelId": "mo_0_111111140461_1259088222_3",
                "Description": "",
                "LUTFileUrl": "https://liudehua-9527.cos.ap-guangzhou.myqcloud.com/result.jpeg?q-sign-algorithm=sha1&q-ak=AKID********EXAMPLE&q-sign-time=8888;9999&q-key-time=8888;9999&q-header-list=&q-url-param-list=&q-signature=7de87f7bf9cfd23df9da32f46661e7cf97a5603c"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

