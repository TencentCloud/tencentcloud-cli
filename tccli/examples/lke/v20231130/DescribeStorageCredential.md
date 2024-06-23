**Example 1: 获取对象存储上传密钥**



Input: 

```
tccli lke DescribeStorageCredential --cli-unfold-argument  \
    --BotBizId 1727231073371148288
```

Output: 
```
{
    "Response": {
        "Bucket": "qidian-qbot-test-1251316161",
        "CorpUin": "0",
        "Credentials": {
            "TmpSecretId": "AKIDijguNrgnblHncqBKsJBrPV5_J6NCCuklAAvcQlNUiArDzMWbEA97tmXFbydKx839",
            "TmpSecretKey": "tI2ka75Gsqj46xx8/TbqhTa2VmUYm11Gi08EkAbkaVQ=",
            "Token": "FS9JPHeDJWa1fjOrV6X0l1XXfwsGUpIa929d1959a6973c640f2248598cf6b21fHmvd_Zw5Geld2CGSAdgsme916AxqAdp3fKBhlKEnTUaUeoFAEUxtiAdL2pL29U9hM8vuRyoY5BJJoH17ucJv5nAoXfR9kaf41NTw0nSUd1XI55EfTzPWUiqOQF7nAyASFeKZZnHq6Capdos04TqSfEYW9ZaODqh0Htc1MCl0rue9Vh9muCJQuMXaH8fkrtigvZHh2fX5yyX4xXJ0mcST1TDbFwFTz5cbUmKMeiwNE_DYXg9Qhbv1LaF9MMFbqCU7UMfWEngpcncHcUL2hPkMYvlZqKAMHjo_SsgaQB8Pg_9gudKUqEDtJhRUzMkyyYYpcZQggGYyPmtbUcGumdugaKPz1HUXiYQWQ_bBVBrqR3V0QiVKWTg8xtgxepJL8RLizOd8q0Oj_cAM9EncPpvjJanaO9xGu7tEjMtD770sbnr0YI2mu16WNgNkhFUucE1OEzeWibshpbCnzi--VArAFuwV30N9ChTobLPd_0rq3J3ekRRobQEMkLxHxS6vcUjCDnYawaVLe9aXtVMD-hy8pVOAydvoB2hxMpczOtHkeyQsy0F-OqCnSI0bhs17OOZfqhoNQhWWR7LI9cSvlP0N-g6QeGpqkAkATTN27W5iLGJoMne49llTDFsD1emH-KTpIL4KcrkPLH_NWN0C52PZByDmAq0xwGCZ5xNU0X9JzUzaMpjVSOlluJDf4_fSzdY8EmBOQCf0EaegY1vDyP3bXTOf8xkRF56AGkYXjm_xpl7zEgXuoojr5yGyOq7iNG4kTCcnkAasZvcbw1ZY9-b6Ae-VlkRnGA5nEUe-v5nsw1UQZAm_YKRDtReQ5vRefZpso76YohBocqbgF1ZF15W__8xVHhX6E4zVrZ9w7Um74fzCyc3_uZH45ockrLr2AH0qjdHE-T397390OXmsON1frQCr7u5Dvkqd4YCLQnuHsPSzB9YO9bXNwzHZU7cGsGliCSi53m1sV2JDu2h07a-i7JyocbHAp4jNW8vIbGjcnjz7qPkOnthztgmScAK1GkeVpOge542a-UEEVxMj6GNWD2D7BMJaxEWV4IG5QsHL13pt3jmlKbSqeovee8OXyn2v4y50zXxwHZdD6i9bVkb7ig"
        },
        "ExpiredTime": 1701429243,
        "FilePath": "/corp/137/doc/",
        "Region": "ap-guangzhou",
        "RequestId": "87d578f9-6de5-4515-906e-d28e56d33fe0",
        "StartTime": 1701425643,
        "Type": "cos"
    }
}
```

**Example 2: 获取文档上传密钥**

离线文档

Input: 

```
tccli lke DescribeStorageCredential --cli-unfold-argument  \
    --BotBizId 1779863007508561920 \
    --FileType md \
    --TypeKey offline
```

Output: 
```
{
    "Response": {
        "Bucket": "qidian-qbot-test-1251316161",
        "CorpUin": "0",
        "Credentials": {
            "TmpSecretId": "AKIDlL2FKlsigkCspNQyh2s0-IzKd8cBvmEM-r2e3qOu8ilXs66FFH_-CKmHeAZhFeEV",
            "TmpSecretKey": "Vlr4JmRzKR4Z1PJxzuSsMZ/O2VlxtmvJCEjPV7s5ruY=",
            "Token": "fPEfNWwNoY196OMrLtTdt1zsp8dImhWa14cca3e696eb04ac4dfc6f5f1a3a8b19paI6e-FWHCNPijFmf62yF1pPIhtrLz05W2RsGymutFYnsBGI9RfvYtrKTVScVeX_q-PQ5LXND8L78tPNkb39rakw_58aPIgJfZqpmdqQN-bFeJY0OiOJQgexT2V9doqZvy7LusVERxTQalEsTCnaB9juEBd7h_8O9Jc2GGTAs8hZYRTsqwqxfkrZm4oN5ndH0m53RloH2iSWm1BlplB1VlzbUFLsdxLcklcw8pyD0mzYOtW0HiMLRMVlGlmu0HZpSXtvYWFpLrZ-vRPNfxfuFywpU5ZmqHGubte2b8_3iOFPVPgsnT4zLL8tawSfV2qKLdN_lgAfNzguX6ROC_yP-hP5j7jkkBzWsvIcDzTdJmGvkS2vOgA3-uGkVDJwljsm0oPz1rEfxt-mI05z5YYCT7VVeJ-KVWi8UlH6ww9u1NUa9bKarH1XfDddBnh9Womlxb92uOzfv75q2PqIfvaN9BZWrRmfzooPbdIqE74oFaJw6tyZnMu2zAs0VbYRTN0CdiVB-IggNVaWoQulSFWLL7NRSIGUzjyoUyt_K2XYjV64sYG4Cwpiqe3BteV61p6m_IPEM4hEgb23hhIiytg8JmFWwJZNLJ3Uu6SB8kidb7wjTNGucfFGvDXgzOnqVbcQnTeva0PZ3XkjBNdplYd6RdWl7N54zawxk6R4Ib8pZ1hDuogXTJ5sjwVuQmmMYGUroQY39omyLMGl2zxEXm5uig"
        },
        "ExpiredTime": 1717063483,
        "FilePath": "",
        "ImagePath": "",
        "Region": "ap-guangzhou",
        "RequestId": "11b8fa96-4700-4f11-8eb0-421de37ed48d",
        "StartTime": 1717062883,
        "Type": "cos",
        "UploadPath": "/corp/1737374499879124992/1779863007508561920/doc/QUiGRdWFAFBkDKjhuxbd-1796118032488595456.md"
    }
}
```

