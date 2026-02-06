**Example 1: 获取数据服务API的发布态信息列表**

获取数据服务API的发布态信息列表示例

Input: 

```
tccli wedata DescribeDataServicePublishedApiList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ProjectId 1470547050521227264
```

Output: 
```
{
    "Response": {
        "DataSet": [
            {
                "ApiFolderName": "根目录",
                "ApiId": "1792441377707995137",
                "ApiName": "test_0520",
                "ApiStatus": 1,
                "ApiTagNames": "",
                "AuthType": 1,
                "ConfigType": 0,
                "CreateTime": "2024-10-24 15:47:09",
                "Id": "1849356941592047617",
                "OwnerName": "jaredlin"
            }
        ],
        "RequestId": "356df7a2-8e3c-4914-abe8-3a6c33a211d8",
        "TotalCount": 53
    }
}
```

