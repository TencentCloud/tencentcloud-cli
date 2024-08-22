**Example 1: DescribeMNPOfflinePackageURL**



Input: 

```
tccli tcmpp DescribeMNPOfflinePackageURL --cli-unfold-argument  \
    --MNPId mpjl3td541qppx9k \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Data": "http127.0.0.1/T04257DS9431720WTAG/mpp/mpjl3td541qppx9k_1.0.321.apkg"
        },
        "RequestId": "c4547fc8-050e-4d47-93c4-df783d309345"
    }
}
```

