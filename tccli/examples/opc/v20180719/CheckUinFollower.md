**Example 1: 查询TCC中UIN的关联关系**

判断CheckUin和OAAccountId在TCC中是否有关联关系

Input: 

```
tccli opc CheckUinFollower --cli-unfold-argument  \
    --CheckUin 909619400 \
    --OAAccountId oaname
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

