**Example 1: 修改 TWeSee 人员**

修改人员名称并标记为持久记忆。

Input: 

```
tccli iotexplorer ModifyTWeSeePerson --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --PersonId person-66666666-7777-8888-9999-000000000000 \
    --Name 妈妈 \
    --IsRemembered True
```

Output: 
```
{
    "Response": {
        "RequestId": "req-modify-person-1"
    }
}
```

