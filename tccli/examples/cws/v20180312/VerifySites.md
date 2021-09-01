**Example 1: 验证站点**

验证已经添加的站点

Input: 

```
tccli cws VerifySites --cli-unfold-argument  \
    --Urls http%3A%2F%2Fwww.qcloud.com
```

Output: 
```
{
    "Response": {
        "FailNumber": 2,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "SuccessNumber": 1
    }
}
```

