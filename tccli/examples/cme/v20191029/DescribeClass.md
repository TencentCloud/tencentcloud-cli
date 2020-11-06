**Example 1: 获取分类列表**



Input: 

```
tccli cme DescribeClass --cli-unfold-argument  \
    --Platform test \
    --Owner.Id 1111 \
    --Owner.Type PERSON
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

