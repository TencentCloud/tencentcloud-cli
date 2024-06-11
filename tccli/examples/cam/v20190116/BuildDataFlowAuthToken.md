**Example 1: 生成AuthToken**

生成AuthToken

Input: 

```
tccli cam BuildDataFlowAuthToken --cli-unfold-argument  \
    --ResourceId cdb-12dd3d \
    --ResourceRegion ap-shanghai \
    --ResourceAccount ReadOnly
```

Output: 
```
{
    "Response": {
        "Credentials": {
            "CurrentTime": 12332343423,
            "LastRotationTimeCost": 343,
            "NextRotationTime": 10,
            "RotationMessage": "success",
            "RotationStatus": "success",
            "Token": "944a***mtHS"
        },
        "RequestId": "5bc7f0df-18a3-426b-84ce-ddbc8d1c95d1"
    }
}
```

