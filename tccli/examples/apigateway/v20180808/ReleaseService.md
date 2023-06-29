**Example 1: ReleaseService**

发布服务


Input: 

```
tccli apigateway ReleaseService --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --EnvironmentName prepub \
    --ReleaseDesc 'Released By Serverless'
```

Output: 
```
{
    "Response": {
        "Result": {
            "ReleaseDesc": "Released By Serverless",
            "ReleaseVersion": "2020022502411672fae6e9-9726-4caa-8867-6366cd3f1ba5"
        },
        "RequestId": "c5b4711b-8044-43eb-97cc-e755c5df1420"
    }
}
```

