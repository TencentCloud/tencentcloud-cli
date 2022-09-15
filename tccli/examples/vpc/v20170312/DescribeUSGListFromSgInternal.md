**Example 1: 根据APPID查询安全组列表**



Input: 

```
tccli vpc DescribeUSGListFromSgInternal --cli-unfold-argument  \
    --GetUSGListFromSGRequest.0.ProjectList 4567 1234 \
    --GetUSGListFromSGRequest.0.EndNum 10 \
    --GetUSGListFromSGRequest.0.Default 0 \
    --GetUSGListFromSGRequest.0.StartNum 1 \
    --GetUSGListFromSGRequest.0.InstanceList sg-qwekasd sg-asdasd \
    --GetUSGListFromSGRequest.0.Project 123 \
    --GetUSGListFromSGRequest.0.InstanceId sg-asdasd \
    --GetUSGListFromSGRequest.0.SgId 12312312
```

Output: 
```
{
    "Response": {
        "GetUSGListFromSGResult": [
            {
                "SgId": "251197522",
                "Sys": 0,
                "UpdateTime": "2022-06-23 18:06:37",
                "ProjectId": "0",
                "SafeGroupId": "sg-dn7qcw21",
                "AppId": "251197522",
                "Os": 0,
                "SgName": "test_sdk",
                "SgRemark": "ream",
                "CreateTime": "2022-06-23 17:01:26"
            }
        ],
        "ReturnCode": 0,
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

