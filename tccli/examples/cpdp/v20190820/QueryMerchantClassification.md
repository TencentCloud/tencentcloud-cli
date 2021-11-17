**Example 1: 查询商户分类接口成功示例**

查询商户分类接口成功

Input: 

```
tccli cpdp QueryMerchantClassification --cli-unfold-argument  \
    --OpenId f2cc268b9c95fbbb230a19397fe35f8d \
    --OpenKey e30051d527bd4e621e7090c9392739ec
```

Output: 
```
{
    "Response": {
        "RequestId": null,
        "ErrCode": "0",
        "ErrMessage": "查询成功",
        "Result": [
            {
                "Code": "100",
                "Name": "川菜",
                "Parent": "0"
            }
        ]
    }
}
```

