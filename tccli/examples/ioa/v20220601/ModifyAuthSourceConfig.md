**Example 1: 修改认证源**

修改认证源

Input: 

```
tccli ioa ModifyAuthSourceConfig --cli-unfold-argument  \
    --Description abc \
    --WelcomeText abc \
    --TypeName abc \
    --FactorTypes.0.AdditionalAuthAvailable True \
    --FactorTypes.0.ChallengeAuthAvailable True \
    --FactorTypes.0.PrimaryAuthAvailable True \
    --FactorTypes.0.Name abc \
    --FactorTypes.0.Platforms abc \
    --FactorTypes.0.Type abc \
    --Type abc \
    --Id abc \
    --Name abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

