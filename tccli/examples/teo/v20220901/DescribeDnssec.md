**Example 1: 查询 DNSSEC 信息**



Input: 

```
tccli teo DescribeDnssec --cli-unfold-argument  \
    --ZoneId zone-25ryyvog1qih
```

Output: 
```
{
    "Response": {
        "Status": "enabled",
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "RequestId": "2ccgtb24-7dc5-46s2-9r3e-95825d53dwe3a",
        "DnssecInfo": {
            "KeyTag": 0,
            "Algorithm": "13",
            "DigestAlgorithm": "SHA256",
            "KeyType": "ECDSAP256SHA256",
            "DS": "example.com. 3600 IN DS 16953 13 2 48E939042E82C22542CB377B580DF",
            "PublicKey": "oXiGYrSTO+LSCJ3mohc8EP+CzF9KxBj8/ydXJ22pKuZP3VAC3/Md/k7xZfz470Co",
            "Flags": 257,
            "DigestType": "2",
            "Digest": "48E939042E82C22542CB377B580DFDC52A361CEFDC72E7F9107E2B6BD9306A45"
        }
    }
}
```

