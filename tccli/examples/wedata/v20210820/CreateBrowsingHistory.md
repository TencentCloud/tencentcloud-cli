**Example 1: 创建用户数据开发浏览历史**

创建用户数据开发浏览历史

Input: 

```
tccli wedata CreateBrowsingHistory --cli-unfold-argument  \
    --ProjectId abc \
    --Title abc \
    --ResourceType abc \
    --ExtraInfo abc \
    --ResourceId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

