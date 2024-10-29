**Example 1: 获取数据服务API的发布态信息列表**

获取数据服务API的发布态信息列表示例

Input: 

```
tccli wedata DescribeDataServicePublishedApiList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 2 \
    --ProjectId 1470547050521227264 \
    --Filters.Keyword 
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "ApiFolderName": "test",
                "ApiId": "1753335714101014529",
                "ApiName": "test_gss_0202",
                "ApiStatus": 1,
                "ApiTagNames": "test_001",
                "AuthType": 1,
                "ConfigType": 1,
                "CreateTime": "2024-04-25 10:14:29",
                "Id": "1783318630750957569",
                "OwnerName": "v_vgssgan"
            },
            {
                "ApiFolderName": "test",
                "ApiId": "1746830093602308097",
                "ApiName": "test_gss_0116",
                "ApiStatus": 1,
                "ApiTagNames": "",
                "AuthType": 0,
                "ConfigType": 0,
                "CreateTime": "2024-01-15 18:41:28",
                "Id": "1746845044760952833",
                "OwnerName": "v_vgssgan"
            }
        ],
        "RequestId": "39313658-20fe-4f38-ae42-17fca1853cf1",
        "TotalCount": 39
    }
}
```

