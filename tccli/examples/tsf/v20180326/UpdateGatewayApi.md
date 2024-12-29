**Example 1: 更改API**



Input: 

```
tccli tsf UpdateGatewayApi --cli-unfold-argument  \
    --ApiId api-zwua4plw \
    --Path /echo-user \
    --Method GET \
    --PathMapping /echo-user \
    --Host http://www.qq.com \
    --Description this is desc
```

Output: 
```
{
    "Response": {
        "RequestId": "c17753d4-a08b-4d4a-b8f5-a4160ff02c6d",
        "Result": true
    }
}
```

