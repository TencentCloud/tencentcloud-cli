**Example 1: 查询 DNSSEC 信息**



Input: 

```
tccli teo DescribeDnssec --cli-unfold-argument  \
    --Id xx
```

Output: 
```
{
    "Response": {
        "Status": "xx",
        "ModifiedOn": "2020-09-22T00:00:00+00:00",
        "Name": "xx",
        "Dnssec": {
            "KeyTag": 0,
            "Algorithm": "xx",
            "DigestAlgorithm": "xx",
            "KeyType": "xx",
            "DS": "xx",
            "PublicKey": "xx",
            "Flags": 0,
            "DigestType": "xx",
            "Digest": "xx"
        },
        "RequestId": "xx",
        "Id": "xx"
    }
}
```

