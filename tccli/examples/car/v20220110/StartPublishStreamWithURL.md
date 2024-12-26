**Example 1: 开始云端推流到指定URL示例**

开始云端推流到指定URL示例

Input: 

```
tccli car StartPublishStreamWithURL --cli-unfold-argument  \
    --UserId user_id \
    --PublishStreamURL rtmp://1.1.1.1:1935/live/my_live
```

Output: 
```
{
    "Response": {
        "RequestId": "25b6f399-bd7c-4e5e-99a3-9a6f4b11e1b7"
    }
}
```

