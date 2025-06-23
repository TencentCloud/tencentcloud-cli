**Example 1: 仓库镜像列表**

仓库镜像列表

Input: 

```
tccli csip DescribeRepositoryImageAssets --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AppId": 0,
                "Uin": "abc",
                "NickName": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "InstanceCreateTime": "abc",
                "InstanceSize": "abc",
                "BuildCount": 0,
                "InstanceType": "abc",
                "AuthStatus": 0,
                "InstanceVersion": "abc",
                "Region": "abc",
                "RepositoryUrl": "abc",
                "RepositoryName": "abc"
            }
        ],
        "Total": 0,
        "RegionList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

