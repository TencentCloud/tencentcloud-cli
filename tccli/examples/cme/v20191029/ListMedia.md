**Example 1: 浏览媒体**

浏览媒体

Input: 

```
tccli cme ListMedia --cli-unfold-argument  \
    --Platform test \
    --ClassPath /a/b \
    --Owner.Id 1111 \
    --Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "ClassInfoSet": [],
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "ClassPath": "/test",
                    "CreateTime": "2019-11-20T02:43:29Z",
                    "MaterialId": "281921553743710047",
                    "MaterialType": "AUDIO",
                    "Name": "林俊杰 - 可惜没如果.wav",
                    "Owner": {
                        "Id": "6b6ef043-85f3-4614-b735-768bb466ae5b",
                        "Type": "PERSON"
                    },
                    "PreviewUrl": "",
                    "TagSet": [],
                    "UpdateTime": "2019-11-20T02:43:29Z"
                }
            }
        ],
        "MaterialTotalCount": 1,
        "RequestId": "7bf08361-4455-4cbd-afd6-423b62c54a05"
    }
}
```

