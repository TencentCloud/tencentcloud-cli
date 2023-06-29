**Example 1: 获取用户属性列表**



Input: 

```
tccli sag DescribeAttrUserList --cli-unfold-argument  \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Attr": 1,
                "Cond": 1
            }
        ],
        "RequestId": "xxx"
    }
}
```

