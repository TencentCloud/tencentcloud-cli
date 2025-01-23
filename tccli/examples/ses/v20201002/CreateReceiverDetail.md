**Example 1: 创建单个收件人**



Input: 

```
tccli ses CreateReceiverDetail --cli-unfold-argument  \
    --ReceiverId 1 \
    --Emails example@gmail.com example@qq.com
```

Output: 
```
{
    "Response": {
        "EmptyEmailCount": 0,
        "RepeatCount": 1,
        "RequestId": "b7ba8907-7b5f-4750-be7e-573d3f75bf8c",
        "TooLongCount": 0,
        "TotalCount": 2,
        "ValidCount": 1
    }
}
```

