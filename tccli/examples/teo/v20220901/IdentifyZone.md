**Example 1: 认证站点**

认证站点

Input: 

```
tccli teo IdentifyZone --cli-unfold-argument  \
    --ZoneName example.com
```

Output: 
```
{
    "Response": {
        "Ascription": {
            "Subdomain": "edgeonereclaim",
            "RecordType": "TXT",
            "RecordValue": "reclaim-a24aba2420cf4ce8b7bff7c8be6d337f"
        },
        "FileAscription": {
            "IdentifyPath": "/.well-known/teo-verification/vd4ewuqa9n.txt",
            "IdentifyContent": "88v24mnnljwbhaohrpfx80f63duhdnjx"
        },
        "RequestId": "9kl50bew-89ga-44f4-91ce-78125d53vd2a"
    }
}
```

