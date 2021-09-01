**Example 1: 批量禁止CMK**

对指定的CMK 列表进行批量禁止。

Input: 

```
tccli kms DisableKeys --cli-unfold-argument  \
    --KeyIds 23e80852-1e38-11e9-b129-5cb9019b4b01 23e80852-1e38-11e9-b129-5cb9019b4b02
```

Output: 
```
{
    "Response": {
        "RequestId": "1b580852-1e38-11e9-b129-5cb9019b4b00"
    }
}
```

