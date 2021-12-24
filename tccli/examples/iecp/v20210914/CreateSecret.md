**Example 1: CreateSecret**



Input: 

```
tccli iecp CreateSecret --cli-unfold-argument  \
    --EdgeUnitID 1 \
    --SecretName iecp \
    --SecretNamespace default \
    --SecretType DockerConfigJson \
    --DockerConfigJson 
```

Output: 
```
{
    "Response": {
        "RequestId": "137ac961-6173-4250-995f-4769cd41c945"
    }
}
```

