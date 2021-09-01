**Example 1: 获取客户所属门店列表接口 - 成功示例**



Input: 

```
tccli youmall DescribeShopInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 100,
        "ShopInfoSet": [
            {
                "City": "北京市",
                "CompanyId": "testCompany1",
                "CompanyName": "测试1",
                "Province": "北京市",
                "ShopCode": "xxx",
                "ShopId": 2,
                "ShopName": "门店XXX"
            },
            {
                "City": "成都市",
                "CompanyId": "testCompany1",
                "CompanyName": "测试1",
                "Province": "四川省",
                "ShopCode": "xxx1",
                "ShopId": 2,
                "ShopName": "门店XXX1"
            }
        ],
        "RequestId": "6ec80684-0879-405e-8932-72e7c0c48ef8"
    }
}
```

**Example 2: 获取客户所属门店列表接口 - 失败示例**



Input: 

```
tccli youmall DescribeShopInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.NoRight",
            "Message": "have no right access"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

