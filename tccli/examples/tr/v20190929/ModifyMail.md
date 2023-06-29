**Example 1: 修改邮寄地址**



Input: 

```
tccli tr ModifyMail --cli-unfold-argument  \
    --MailID 23456sdv \
    --Recipient aa \
    --Phone 186559278653 \
    --Province 福建省 \
    --Address 厦门海沧
```

Output: 
```
{
    "Response": {
        "Flag": true,
        "Msg": "修改成功",
        "RequestId": "1"
    }
}
```

