**Example 1: 删除 TWeSee 人员**

删除人员及其关联人脸。

Input: 

```
tccli iotexplorer DeleteTWeSeePerson --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --PersonId person-11111111-2222-3333-4444-555555555555 \
    --DeleteFaces True
```

Output: 
```
{
    "Response": {
        "RequestId": "req-delete-person-1"
    }
}
```

