**Example 1: 修改别名示例**

对指定的CMK修改别名。

Input: 

```
tccli kms UpdateAlias --cli-unfold-argument  \
    --KeyId 23e80852-1e38-11e9-b129-5cb9019b4b01 \
    --Alias NewAlias
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

