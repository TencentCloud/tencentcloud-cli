**Example 1: 请求详细印章列表信息**

查询企业印章的列表，需要操作者具有查询印章权限
客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；入参InfoType控制印章是否携带授权人信息，为1则携带，为0则返回的授权人信息为空数组。接口调用成功返回印章的信息列表还有企业印章的总数。

Input: 

```
tccli ess DescribeOrganizationSeals --cli-unfold-argument  \
    --InfoType 1 \
    --Limit 1 \
    --Offset 0 \
    --Operator.UserId yDRt***gygqb1n5zUuO4zjEwzVL5XuTW
```

Output: 
```
{
    "Response": {
        "RequestId": "901***5e-7113-4f50-a472-11eb9fe61d9a",
        "Seals": [
            {
                "AuthorizedUsers": [
                    {
                        "UserId": "yDR1fUUgygj9ic***uO4zjEvDps0boOj"
                    },
                    {
                        "UserId": "yDxojUUgydjfd2x8UuO4zjEEwSQl****"
                    }
                ],
                "CreateOn": 1628061951,
                "Creator": "yDRtSUUgygqb1n5zUuO4zjEwzVL5****",
                "FailReason": "",
                "IsAllTime": true,
                "SealId": "yDxMjUyKQDN7EkUuO4zjEBpGXvHE****",
                "SealName": "深圳市腾讯计算机系统有限公司企业公章企业公章",
                "SealPolicyId": "",
                "SealStatus": "SUCCESS",
                "SealType": "",
                "Url": "https://*********80"
            }
        ],
        "TotalCount": 40
    }
}
```

