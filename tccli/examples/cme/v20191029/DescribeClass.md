**Example 1: 获取分类列表**



Input: 

```
tccli cme DescribeClass --cli-unfold-argument  \
    --Owner.Type PERSON \
    --Owner.Id c9bf9e57-1685-4c89-bafb-ff5af830be8a \
    --Platform 1000000009
```

Output: 
```
{
    "Response": {
        "RequestId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        "ClassInfoSet": [
            {
                "Owner": {
                    "Id": "c9bf9e57-1685-4c89-bafb-ff5af830be8a",
                    "Type": "PERSON"
                },
                "ClassPath": "/a/b"
            }
        ]
    }
}
```

