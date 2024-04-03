**Example 1: 使用子账号长期密钥调用**

使用子账号长期密钥调用

Input: 

```
tccli sts GetCallerIdentity --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Type": "CAMUser",
        "AccountId": "1000262***",
        "UserId": "1000261***",
        "PrincipalId": "1000261****",
        "Arn": "qcs::cam:1000262***:uin/1000261***",
        "RequestId": "1c875b55-128b-4152-9e73-0984fd489ba2"
    }
}
```

**Example 2: 使用AssumeRole生成的临时凭证调用**

使用AssumeRole生成的临时凭证调用

Input: 

```
tccli sts GetCallerIdentity --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Type": "CAMRole",
        "AccountId": "1000262***",
        "UserId": "461168601842741***:roleSessionName",
        "PrincipalId": "1000261****",
        "Arn": "qcs::sts:1000262***:assumed-role/461168601842741***",
        "RequestId": "1c875b55-128b-4152-9e73-0984fd489ba2"
    }
}
```

**Example 3: 使用GetFederationToken生成的临时凭据调用**

使用GetFederationToken生成的临时凭据调用

Input: 

```
tccli sts GetCallerIdentity --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Type": "CAMUser",
        "AccountId": "1000262***",
        "UserId": "1000261****:federatedUserName",
        "PrincipalId": "1000261****",
        "Arn": "qcs::sts:1000262***:federated-user/1000261****",
        "RequestId": "1c875b55-128b-4152-9e73-0984fd489ba2"
    }
}
```

