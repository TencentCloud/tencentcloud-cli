**Example 1: 通过AuthCode查询用户是否实名**

通过AuthCode查询用户是否实名，AuthCode 查询后作废，只能查询一次

Input: 

```
tccli ess DescribeThirdPartyAuthCode --cli-unfold-argument  \
    --AuthCode xxxxxx*****code
```

Output: 
```
{
    "Response": {
        "RequestId": "s1629444337855318929",
        "VerifyStatus": "VERIFIED"
    }
}
```

**Example 2: 测试用例**

测试用例

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

