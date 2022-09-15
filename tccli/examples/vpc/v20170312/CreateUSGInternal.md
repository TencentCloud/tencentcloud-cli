**Example 1: 新建USG**



Input: 

```
tccli vpc CreateUSGInternal --cli-unfold-argument  \
    --CreateUSGRequest.0.ProjectId 123 \
    --CreateUSGRequest.0.UsgRemark remark \
    --CreateUSGRequest.0.Sys 1 \
    --CreateUSGRequest.0.UsgName test \
    --CreateUSGRequest.0.SgId 123123 \
    --CreateUSGRequest.0.Os 1
```

Output: 
```
{
    "Response": {
        "CreateUSGResult": [
            {
                "SgId": "251197522",
                "UsgId": "sg-ispsj3ah",
                "UsgName": "test_sdk"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

