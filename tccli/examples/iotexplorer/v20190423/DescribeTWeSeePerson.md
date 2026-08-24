**Example 1: 查询 TWeSee 人员详情**

查询人员详情及其代表人脸。

Input: 

```
tccli iotexplorer DescribeTWeSeePerson --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --PersonId person-11111111-2222-3333-4444-555555555555 \
    --FaceLimit 3
```

Output: 
```
{
    "Response": {
        "Person": {
            "PersonId": "person-11111111-2222-3333-4444-555555555555",
            "Name": "爸爸",
            "Source": 1,
            "IsRemembered": true,
            "Faces": []
        },
        "RequestId": "req-describe-person-1"
    }
}
```

