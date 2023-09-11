**Example 1: 通过AuthCode查询用户是否实名**

通过AuthCode查询用户是否实名，AuthCode 查询后作废，只能查询一次

Input: 

```
tccli ess DescribeThirdPartyAuthCode --cli-unfold-argument  \
    --AuthCode yDxAxU*******E4JGgr8S5
```

Output: 
```
{
    "Response": {
        "RequestId": "80905521-1203-41b1-9203-1eb2973cc488",
        "VerifyStatus": "VERIFIED"
    }
}
```

**Example 2: 通过AuthCode查询用户是否实名(失效AuthCode)**

AuthCode已经使用过过一次, 再次查询返回错误OperationDenied.AuthCodeInvalid

Input: 

```
tccli ess DescribeThirdPartyAuthCode --cli-unfold-argument  \
    --AuthCode yDxAxU*******E4JGgr8S5
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "OperationDenied.AuthCodeInvalid",
            "Message": "授权码已失效"
        },
        "RequestId": "c6a50bbc-fe84-4744-8c16-efe33f80d632"
    }
}
```

