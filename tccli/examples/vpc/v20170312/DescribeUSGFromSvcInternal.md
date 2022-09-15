**Example 1: 查询SVC关联的USG**



Input: 

```
tccli vpc DescribeUSGFromSvcInternal --cli-unfold-argument  \
    --GetUsgFromSvcRequest.0.SvcId vpce-kifyia9o
```

Output: 
```
{
    "Response": {
        "GetUsgFromSvcResult": [
            {
                "SvcId": "vpce-kifyia9o",
                "UsgIdList": [
                    "sg-h4q2qsjv"
                ],
                "UsgInfo": [
                    {
                        "Sys": 0,
                        "UpdateTime": "2021-12-02 15:37:28",
                        "ProjectId": "0",
                        "SafeGroupId": "sg-h4q2qsjv",
                        "AppId": "251197522",
                        "Os": 0,
                        "SgName": "test_pro",
                        "SgRemark": "自定义",
                        "CreateTime": "2021-12-02 11:03:42"
                    }
                ]
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

