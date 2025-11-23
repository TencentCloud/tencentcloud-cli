**Example 1: 添加网站资产**

添加http数据

Input: 

```
tccli ctem CreateHttp --cli-unfold-argument  \
    --CustomerId 100081 \
    --Url http://test.com \
    --Title test \
    --Code 200 \
    --Ip 1.1.1.1
```

Output: 
```
{
    "Response": {
        "RequestId": "3b83a04f-37c8-4ac4-9a4b-7343400508b4"
    }
}
```

