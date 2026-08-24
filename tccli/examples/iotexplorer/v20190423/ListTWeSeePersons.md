**Example 1: 查询 TWeSee 人员列表**

查询已标记为持久记忆的人员。

Input: 

```
tccli iotexplorer ListTWeSeePersons --cli-unfold-argument  \
    --ProductId PRODUCTID1 \
    --DeviceName dev001 \
    --ChannelId 0 \
    --IsRemembered True \
    --FaceLimit 3 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Offset": 0,
        "Limit": 20,
        "Persons": [
            {
                "PersonId": "person-11111111-2222-3333-4444-555555555555",
                "Name": "爸爸",
                "Source": 1,
                "IsRemembered": true,
                "Faces": []
            }
        ],
        "RequestId": "req-list-persons-1"
    }
}
```

