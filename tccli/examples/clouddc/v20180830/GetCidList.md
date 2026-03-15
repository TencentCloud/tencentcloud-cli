**Example 1: 示例**

示例

Input: 

```
tccli clouddc GetCidList --cli-unfold-argument  \
    --CustomerType 1 \
    --CustomerName DEV经营测试账号4547 \
    --IdCard 202101084547
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AuthState": 3,
                "BusinessManager": "aalexzhu",
                "Cid": "0031685e04f73d9b5dcb7e69f8aa9c01",
                "CountryCode": "CN",
                "CustomerName": "南京云帐房网络科技有限公司",
                "CustomerType": 1,
                "Duns": "",
                "MdMID": ""
            }
        ],
        "RequestId": "f77f21ce-40b6-482d-8c09-812747a53d3c"
    }
}
```

