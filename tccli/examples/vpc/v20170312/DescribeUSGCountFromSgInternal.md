**Example 1: 根据APPID查询安全组数量(测试时注意)**



Input: 

```
tccli vpc DescribeUSGCountFromSgInternal --cli-unfold-argument  \
    --GetUSGCountFromSGRequest.0.SgId 132131231
```

Output: 
```
{
    "Response": {
        "GetUSGCountFromSGResult": [
            {
                "SgId": "251197522",
                "USGCount": 17
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

