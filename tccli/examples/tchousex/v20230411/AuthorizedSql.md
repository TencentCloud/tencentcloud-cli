**Example 1: 示例**

示例

Input: 

```
tccli tchousex AuthorizedSql --cli-unfold-argument  \
    --ApiType warehouse \
    --InstanceId test \
    --UserName aueer
```

Output: 
```
{
    "Response": {
        "ErrorMsg": "ApiType must be one of the follow choices：Login,LoginTest,LoginOut,SwitchLogin",
        "InstanceId": "test",
        "RequestId": "65c8365a-0fdc-4dd6-95e7-83dc1850bd52",
        "ReturnData": "null"
    }
}
```

**Example 2: AuthorizedSql**

授权sql工作区

Input: 

```
tccli tchousex AuthorizedSql --cli-unfold-argument  \
    --ApiType abcde \
    --InstanceId abcde \
    --UserName abcsss \
    --SqlToken abcss \
    --Pwd abcss
```

Output: 
```
{
    "Response": {
        "InstanceId": "abcss",
        "ErrorMsg": "abcss",
        "ReturnData": "abcss",
        "RequestId": "abcss"
    }
}
```

