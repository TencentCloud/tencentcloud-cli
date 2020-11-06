**Example 1: 平铺媒体资源**



Input: 

```
tccli cme FlattenListMedia --cli-unfold-argument  \
    --Platform test \
    --ClassPath /a/b \
    --Owner.Id 1111 \
    --Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "MaterialInfoSet": [
            {
                "BasicInfo": {
                    "MaterialId": "281921553743710210",
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

