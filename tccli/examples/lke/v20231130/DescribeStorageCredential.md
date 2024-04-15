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

