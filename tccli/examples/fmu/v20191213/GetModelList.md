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
        "ModelInfos": [
            {
                "ModelId": "id1",
                "Description": "desc",
                "LUTFileUrl": "LUTFileUrl"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

