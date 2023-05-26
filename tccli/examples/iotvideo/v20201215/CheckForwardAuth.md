**Example 1: 判断是否开启转发的权限**

通用场景

Input: 

```
tccli iotvideo CheckForwardAuth --cli-unfold-argument  \
    --QueueType 1 \
    --Skey 1231523awe
```

Output: 
```
{
    "Response": {
        "Endpoint": "12321514",
        "QueueType": 1,
        "RequestId": "2172b7d1-9a49-4142-938a-ff4fa3d55881",
        "Productid": "PTROMP3AOB",
        "ErrMsg": "ok",
        "Result": 1
    }
}
```

