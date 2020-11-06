**Example 1: 检索素材**



Input: 

```
tccli cme SearchMaterial --cli-unfold-argument  \
    --Platform test \
    --SearchScopes.0.Owner.Id 1111 \
    --SearchScopes.0.Owner.Type PERSON \
    --SearchScopes.0.ClassPath /a/b
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "123456789",
                    "MaterialType": "VIDEO",
                    "Name": "9Qvacao2r7EA",
                    "CreateTime": "2019-12-31T03:59:14Z",
                    "UpdateTime": "2019-12-31T03:59:14Z",
                    "ClassPath": "/a/b",
                    "TagSet": null,
                    "PreviewUrl": "http://1810000002.vod2.myqcloud.com/8d388656vodtranscq1810000002/accfa04c5285890797261730431/coverBySnapshot/1577764755_4069421039.100_0.jpg",
                    "Owner": {
                        "Type": "PERSON",
                        "Id": "1111"
                    }
                }
            }
        ],
        "RequestId": "requestId"
    }
}
```

