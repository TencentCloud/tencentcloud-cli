**Example 1: 访问示例**



Input: 

```
tccli bh AccessDevices --cli-unfold-argument  \
    --InstanceId ins-2ftyp2vu \
    --Account zhangsan \
    --Password  \
    --PrivateKey  \
    --PrivateKeyPassword  \
    --Exe web \
    --Drivers  \
    --Width 60 \
    --Height 80 \
    --IntranetAccess False
```

Output: 
```
{
    "Response": {
        "AccessInfo": {
            "AccessURL": "",
            "Ip": "11.11.11.11",
            "Password": "sHUbwq6nFm9mja05n10X6YZ1TbTr0mpS",
            "Port": 8322,
            "User": "root@FdfmcRltiJZ2nNam"
        },
        "RequestId": "3bd56f7b-6453-476d-b0fa-c97c164d68b8"
    }
}
```

