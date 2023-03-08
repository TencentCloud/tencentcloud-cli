**Example 1: 获取分类列表**



Input: 

```
tccli cme DescribeClass --cli-unfold-argument  \
    --Owner.Type PERSON \
    --Owner.Id 1111 \
    --Platform test
```

Output: 
```
{
    "Response": {
        "RequestId": "requestId",
        "ClassInfoSet": [
            {
                "Owner": {
                    "Id": "1111",
                    "Type": "PERSON"
                },
                "ClassPath": "/a/b"
            }
        ]
    }
}
```

