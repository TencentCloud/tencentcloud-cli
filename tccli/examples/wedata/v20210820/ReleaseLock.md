**Example 1: 请求demo**



Input: 

```
tccli wedata ReleaseLock --cli-unfold-argument  \
    --ResourcePath ds:test.sh
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Success": true,
        "ResourcePath": "ds:test.sh"
    }
}
```

**Example 2: 成功释放锁**



Input: 

```
tccli wedata ReleaseLock --cli-unfold-argument  \
    --ResourcePath 字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "e33ea8fa-1de1-45b8-a433-afb750589b5b",
        "Success": true,
        "ResourcePath": "字符串"
    }
}
```

