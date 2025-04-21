**Example 1: 示例1**



Input: 

```
tccli ioa CreateAuthSourceConfig --cli-unfold-argument  \
    --Description xx \
    --WelcomeText xx \
    --TypeName xx \
    --FactorTypes.0.Name xx \
    --FactorTypes.0.PrimaryAuthAvailable True \
    --FactorTypes.0.Platforms xx \
    --FactorTypes.0.AdditionalAuthAvailable True \
    --FactorTypes.0.ChallengeAuthAvailable True \
    --FactorTypes.0.Type xx \
    --Type xx \
    --Id xx \
    --Name xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

