**Example 1: 个例详情**



Input: 

```
tccli rum DescribeFOOMProblemDetail --cli-unfold-argument  \
    --ProductId 0dc5283a55 \
    --ClientIdentify CDBD416C-17E3-45CB-857A-FBDE7E346BBA \
    --Feature 2556EFA7AF2E1E46D40397C7447BCA48 \
    --RequestHeader BEGIN{"X-ProductId": "0dc5283a55","X-Tc-Username": "cdx_test"}END
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": "{\"base_rsp\":{\"code\":0,\"msg\":\"success\"}}",
        "Message": "",
        "RequestId": "74907d31-da5e-42f1-a433-aa738f79fe0e"
    }
}
```

