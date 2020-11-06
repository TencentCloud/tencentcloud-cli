**Example 1: 获取白盒密钥列表**



Input: 

```
tccli kms DescribeWhiteBoxKeyDetails --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "f6308605-f9d7-4a69-9401-c542cd414e00",
        "KeyInfos": [
            {
                "KeyId": "244dab8c-6dad-11ea-80c6-5254006d0810",
                "Alias": "xx",
                "CreateTime": 1585040099,
                "Description": "xx",
                "CreatorUin": 0,
                "OwnerUin": 0,
                "Status": "Disabled",
                "Algorithm": "SM4",
                "EncryptKey": "AAAAACL4R9T1M3r3/S9XpMbUbwHJUKbq/tll0Bop7LG90lHpj+DKmOiEE0Rs5rRrMNaCYIWzWJyU0SNQoX1WNn06QB2qrhDCXEPdwMwgJHx+YfJHUh/eSF5/LUEv27ltidqJyUk3HF5CZgjkN901hFEPf9ZCJcEo5XrORpopW7Ur6svPAjDtIPN3kUDCTqgTPC+FBX0cO/zEZFeMMAU2BPwe6f5O1x5BTrCBEf4qJDpZqT/WxXvSid8pFQ8uSxMqaf0ot57NzfuWG92oAe9HQ7bDCcfuBN7nXX+QipQIBxD/LVWk7zrHtLD/TJfAAoTuE7QKc/lSTOpI1xkTxJq/AFLd5K9EaBN7kpAkAsponZc20Tpk+KlyWE3NHdQrION9fsxtUBl5tz/l6T1j49SR5J2axZ2nnkA3o7L1WIGiv7r3tkd+",
                "DecryptKey": "AAAAACL4R9T1M3r3/S9XpMbUbwHJUKbq/tll0Bop7LG90lHpj+DKmOiEE0Rs5rRrMNaCYIWzWJyU0SNQoX1WNn06QB2qrhDCXEPdwMwgJHx+YfJHUh/eSF5/LUEv27ltidqJyUk3HF5CZgjkN901hFEPf9ZCJcEo5XrORpopW7Ur6svPAjDtIPN3kUDCTqgTPC+FBX0cO/zEZFeMMAU2BPwe6f5O1x5BTrCBEf4qJDpZqT/WxXvSid8pFQ8uSxMqaf0ot57NzfuWG92oAe9HQ7bDCcfuBN7nXX+QipQIBxD/LVWk7zrHtLD/TJfAAoTuE7QKc/lSTOpI1xkTxJq/AFLd5K9EaBN7kpAkAsponZc20Tpk+KlyWE3NHdQrION9fsxtUBl5tz/l6T1j49SR5J2axZ2nnkA3o7L1WIGiv7r3tkd+"
            },
            {
                "KeyId": "3d2de9cd-6daf-11ea-af24-5254006d0810",
                "Alias": "xxx",
                "CreateTime": 1585041000,
                "Description": "xx",
                "CreatorUin": 0,
                "OwnerUin": 0,
                "Status": "Enabled",
                "Algorithm": "SM4",
                "EncryptKey": "AAAAAE2+4Kz2XEgQkdJk2tZuDunuvGOrGd2lbD6tIZESi2sBNR/aTF2Bx/GWdl5sBNlfUKTIsrwxONNABo65mm6x1KmTUIZT/3aVVqK7PLINZ51g0t7i0gERdiimLxjVwQUstPLFqR2hrfcVR+TvheGskQgYJEpdQ1wthcOlm37SRjAvd6OdDx7gQtdutgf49SZ9YCVoYRf5phQDrKSc2WfxI96UwO2zoTCKD+aRB9u3hTzd7Z305kMJ6e+thcgUd+zzCy8KR/nAMeZ/8PKDsrQW/UsugZJLEBdrVk0vD0dQUCYGG7nSTjzS877+570H+WvyNfCCvzLvfu50PA7gLvyXLodppwqWJPOhqfPw9muoec9BD6vA1jxDnhlF6nb0GEh5V6QsAJUyVXzWMXJEce99u1DzeS4pRsc09/7GQ0HauJRz",
                "DecryptKey": "AAAAAE2+4Kz2XEgQkdJk2tZuDunuvGOrGd2lbD6tIZESi2sBNR/aTF2Bx/GWdl5sBNlfUKTIsrwxONNABo65mm6x1KmTUIZT/3aVVqK7PLINZ51g0t7i0gERdiimLxjVwQUstPLFqR2hrfcVR+TvheGskQgYJEpdQ1wthcOlm37SRjAvd6OdDx7gQtdutgf49SZ9YCVoYRf5phQDrKSc2WfxI96UwO2zoTCKD+aRB9u3hTzd7Z305kMJ6e+thcgUd+zzCy8KR/nAMeZ/8PKDsrQW/UsugZJLEBdrVk0vD0dQUCYGG7nSTjzS877+570H+WvyNfCCvzLvfu50PA7gLvyXLodppwqWJPOhqfPw9muoec9BD6vA1jxDnhlF6nb0GEh5V6QsAJUyVXzWMXJEce99u1DzeS4pRsc09/7GQ0HauJRz"
            }
        ]
    }
}
```

