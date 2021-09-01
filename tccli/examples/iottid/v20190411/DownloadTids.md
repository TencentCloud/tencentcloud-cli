**Example 1: 下载TID**



Input: 

```
tccli iottid DownloadTids --cli-unfold-argument  \
    --OrderId p8ZcXGuqus \
    --Quantity 1
```

Output: 
```
{
    "Response": {
        "RequestId": "006b23f0-d768-439e-99e9-1c09af0432af",
        "TidSet": [
            {
                "PrivateKey": "5c1c4318562efb748d6d70a06ab15919453a7f55ffb7cccc6a8041b720c5c664",
                "Psk": "7ac9f2ef19bd5b753b85e1b7ad62282fbc219b96d4aec7e09946074f68d7c68e",
                "PublicKey": "6e10d5b47fe15166048cc1035bdab17a763dbbe97bbf232eab4b1416356c56a392ec7a997a671277b27f25dc97a2a24fccfc021c37465c4028ad19cefda76211",
                "Tid": "000001035D0C97E3D2A46283D27BC612"
            }
        ]
    }
}
```

