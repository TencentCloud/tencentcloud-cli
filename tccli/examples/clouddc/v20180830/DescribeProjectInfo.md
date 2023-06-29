**Example 1: pms与计费中心接口示例**

通过项目编码获取简要的项目信息

Input: 

```
tccli clouddc DescribeProjectInfo --cli-unfold-argument  \
    --ProjectCode 2018091401522
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "JsonString": "[{\"ProjectName\":\"南宁市公安局警务云一期\",\"ProjectCode\":\"20190325114798\",\"ScenarioName\":null,\"ScenarioId\":null,\"SubScenarioName\":null,\"SubScenarioId\":null}]"
    }
}
```

